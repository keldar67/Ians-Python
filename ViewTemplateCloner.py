# Python Shell Pad. Write code snippets here and hit F5 to run.

from System.Collections.Generic import ICollection

app = uiapp.Application

VTypes = 0
VTemplates = 0

#Note: The location of the BVNDH Template is version specific and is hard coded here
templatefile = "F:\\InfoTech\\cad\\RevitStandards2014\\01_Template\\BVN Donovan Hill Documentation Template.rte"

# Source Document is an open file named target.rvt
sourceDoc = app.NewProjectDocument(templatefile)

# Target document is the active document
targetDoc = uiapp.ActiveUIDocument.Document

# Element Ids for all instances of ViewFamilyType class
viewFamilyTypeIds = FilteredElementCollector(sourceDoc).OfClass(ViewFamilyType).ToElementIds()

# Element Ids of the View Templates used in the View Types
templateIds = list()

#Dictionary of <ViewFamilyType,DeaultViewTemplate>
ssList = {}

#-------------------------------------------------------------------------#
#                                                                         #
# Read the ViewTypes and Associated Templates from the Temporary File.    #
#                                                                         #
#-------------------------------------------------------------------------#
ViewTypes = FilteredElementCollector(sourceDoc).OfClass(ViewFamilyType)
for vft in ViewTypes:
  #ElementId of the view Template used in this View Type
  defaultTemplateId = vft.get_Parameter(BuiltInParameter.DEFAULT_VIEW_TEMPLATE).AsElementId()
  
  #Increment The ViewType Counter
  VTypes = VTypes + 1
  
  #Skip if there is no View Template assigned to this view type.
  if defaultTemplateId == ElementId.InvalidElementId:
    continue
  
  templateIds.Add(defaultTemplateId)
  
  ssList.Add(Element.Name.GetValue(vft), sourceDoc.GetElement(defaultTemplateId).Name)
  
  #Increment The View Templates Counters
  VTemplates = VTemplates + 1
  
#-------------------------------------------------------------------------#
#                                                                         #
# Write the ViewTypes and Associated Templates to the current File.       #
#                                                                         #
#-------------------------------------------------------------------------#

options = CopyPasteOptions()

#Set up the Transaction and start it.
t = Transaction(targetDoc,"Copy View Types")
t.Start()

try:

  #Workaround to select the correct Overload for ElementTransformUtils.CopyElements()
  CopyElementsDocVersion = ElementTransformUtils.CopyElements.Overloads.Item[Document, ICollection[ElementId], Document, Transform, CopyPasteOptions]
  
  #Copy The View Types
  CopyElementsDocVersion(sourceDoc, viewFamilyTypeIds.ToList[ElementId](), targetDoc, Transform.Identity, options)

  #Copy The View Templates
  CopyElementsDocVersion(sourceDoc, templateIds.ToList[ElementId](), targetDoc, Transform.Identity, options)
  
  #Match up the View Templates to the View Types.
  for k, v in ssList.items():
    # Find the ViewFamilyType that matches the current position in our list
    vft = FilteredElementCollector(targetDoc).OfClass(ViewFamilyType).Where(lambda q: Element.Name.GetValue(q) == k).FirstOrDefault()
    # Find the View Template that matches the above ViewFamilyType in the BVNDH Template File so we can make our current project match.
    template = FilteredElementCollector(targetDoc).OfClass(View).Where(lambda q: q.IsTemplate and Element.Name.GetValue(q) == v).FirstOrDefault()
    # Apply the View Template as the default for this View Family Type.
    # Note:
    # This will only work for new views of this type... if the user selects an existing view and changes it to one of these types, they
    # will also need to manually apply the View Template as well.
    vft.get_Parameter(BuiltInParameter.DEFAULT_VIEW_TEMPLATE).Set(template.Id)
    
  t.Commit()
  
except TypeError, e:
  print "Rolling Back due to Type Error"
  print e.message
  t.RollBack()
  sourceDoc.Close(False)


#Close the temporary file without saving. We no longer need this because all we were doing was collecting the 
#current ViewFamilyType information from it.
sourceDoc.Close(False)

print "Sucess", VTypes, "View Types copied and", VTemplates, "View Templates copied across."







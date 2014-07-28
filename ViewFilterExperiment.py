

app = uiapp.Application

# Uncomment the template location to suit either network or local working
templatefile = "F:\\InfoTech\\cad\\RevitStandards2014\\01_Template\\BVN Donovan Hill Documentation Template.rte"
#templatefile = "C:\\000 BVN Backup info\\Drive F\\InfoTech\\cad\\RevitStandards2014\\01_Template\\BVN Donovan Hill Documentation Template.rte"

sourceDoc = app.NewProjectDocument(templatefile)
#sourceDoc = doc

targetDoc = doc

templateElements = FilteredElementCollector(sourceDoc).OfClass(View).Where(lambda q: q.IsTemplate)
for t in templateElements: print t.Name

#This finds all of the ViewFilter Elements in the Project
filtsnew = FilteredElementCollector(sourceDoc).OfClass(ParameterFilterElement)
filtsold = FilteredElementCollector(targetDoc).OfClass(ParameterFilterElement)

#In order to Cull the list to only new View Types
for f in filtsnew:
  if f.Name == "searchstring": #Replace "searchstring" with a variable representing the Name to remove.
    filtsnew.Remove(f)

sourceDoc.Close(False)
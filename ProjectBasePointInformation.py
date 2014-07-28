# Interrogate the Project Base Point of the Project.
def PrintProjectBasePointInfo():
  pbp = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_ProjectBasePoint)
  print "---------Project Base Point-----------"
  for p in pbp:
    #print "Workset: " + p.get_Parameter("Workset").AsValueString()
    print "E: " + format(int(p.get_Parameter("E/W").AsValueString()), ',d')
    print "N: " + format(int(p.get_Parameter("N/S").AsValueString()), ',d')
    print "Z: " + format(int(p.get_Parameter("Elev").AsValueString()), ',d')
    print "Angle from True North: " + p.get_Parameter("Angle to True North").AsValueString()
  
  srv = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_SharedBasePoint)
  print "-------------Survey Point-------------"
  for s in srv:
    #print "Workset: " + p.get_Parameter("Workset").AsValueString()
    print "E: " + format(int(s.get_Parameter("E/W").AsValueString()), ',d')
    print "N: " + format(int(s.get_Parameter("N/S").AsValueString()), ',d')
    print "Z: " + format(int(s.get_Parameter("Elev").AsValueString()), ',d')
  print "--------------------------------------"
  
  z = int(p.get_Parameter("Elev").AsValueString())
  if z != 0:
    dialog = TaskDialog("Attention")
    dialog.MainInstruction = "The Project Base Point is not at a datum level of 0"
    dialog.MainContent = "To fix this press the 'OK' Button"
    #dialog.CommonButtons = Autodesk.Revit.UI.TaskDialogCommonButtons.OK | Autodesk.Revit.UI.TaskDialogCommonButtons.Cancel
    result = dialog.Show()
    if result == Autodesk.Revit.UI.TaskDialogResult.Close:
      print "Transaction should happen"
      #ResetProjectBasePointZ()
    else:
      print "Cancel was pressed"
      
    

def ResetProjectBasePointZ():
  
  pbp = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_ProjectBasePoint)
  for p in pbp:
    print "Before: Z= " + format(int(p.get_Parameter("Elev").AsValueString()), ',d')
    t = Transaction(doc)
    t.Start("Project Base Point z = 0")
    p.get_Parameter("Elev").Set(0)
    t.Commit()
    print "After: Z= " + format(int(p.get_Parameter("Elev").AsValueString()), ',d')

PrintProjectBasePointInfo()

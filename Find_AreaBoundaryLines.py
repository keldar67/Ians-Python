#Find Area Boundary Lines matching the level names that they belong to
#For Example: FindAreaBoundaryLines("Building A")
#Finds Area Boundary Lines for all lines belonging to Levels with 
#the name "Building A" in them

print chr(10) * 30 #30 Blank Lines
print "-" *75

def FindAreaBoundaryLines(searchstring):
  fec = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_AreaSchemeLines)
  i = 0
  ids = {}
  for a in fec:
    plan = a.SketchPlane.Name
    if plan.Contains(searchstring):
      print plan + ":\t" +  a.Id.ToString()
      ids[i] = a.Id.ToString()
      i += 1
  
  print "-" *75
  print "Paste These ID's into Revit's 'Find By ID' Tool"
  print
  print "".Join(",",ids.Values) 
  print
  print "-" *75


FindAreaBoundaryLines("HIN")
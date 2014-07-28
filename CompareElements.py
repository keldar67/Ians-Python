#Quickly compares a few specific parameters of pre-selected elements

#--Workset--
#--Design Option--
#--Level-- (/SketchPlane)

#--More than one level (ie Walls, Stairs multi Story??)

elems = list(uidoc.Selection.Elements).ToArray()

#Simply comparing 2 elements. Note: No error checking for more than 2
a = elems[0]
b = elems[1]

print "+"+("-"*78)+"+"

print "-- WORKSET --"
if a.get_Parameter("Workset").AsValueString() != b.get_Parameter("Workset").AsValueString():
  print "\t\tA: ",a.get_Parameter("Workset").AsValueString()
  print "\t\tB: ",b.get_Parameter("Workset").AsValueString()
else:
  print "                   both = ",a.get_Parameter("Workset").AsValueString()

print "-- Design Option --"
if a.get_Parameter(BuiltInParameter.DESIGN_OPTION_PARAM).AsString() != b.get_Parameter(BuiltInParameter.DESIGN_OPTION_PARAM).AsString():
  print "\t\tA: ",a.get_Parameter(BuiltInParameter.DESIGN_OPTION_PARAM).AsString()
  print "\t\tB: ",b.get_Parameter(BuiltInParameter.DESIGN_OPTION_PARAM).AsString()
else:
  print "\tBoth = ",a.get_Parameter(BuiltInParameter.DESIGN_OPTION_PARAM).AsString()


#Just some experimentation with the Element Parameters.
print "~" * 50  
for p in a.Parameters:
  if p.HasValue:
    if p.AsString() == None:
      print p.Definition.Name,":",p.AsValueString()
    else:
      print p.Definition.Name,":",p.AsString()
  else:
    print "________________", p.Definition.Name
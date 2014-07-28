b = BuiltInCategory.OST_ProjectBasePoint
pbp = FilteredElementCollector(doc).OfCategory(b).FirstElement()
selection.Add(pbp)
print "+------Project Base Point Parameters------+"
#print "Workset:",pbp.get_Parameter("Workset").AsValueString()
print "Northing:","{0:.2f}".format(float(pbp.get_Parameter("N/S").AsValueString()))
print "Easting:",format(int(pbp.get_Parameter("E/W").AsValueString()), 'd')
print "Datum:",format(int(pbp.get_Parameter("Elev").AsValueString()), 'd')
print "Rotation:",pbp.get_Parameter("Angle to True North").AsValueString()
print "Design Option:",pbp.get_Parameter("Design Option").AsValueString()
print "+-----------------------------------------+"
Snoop(pbp)








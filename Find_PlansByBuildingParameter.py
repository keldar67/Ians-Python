# Revit Python Shell Pad. Write code snippets here and hit F5 to run.

fec = FilteredElementCollector(doc).OfClass(ViewPlan)
for p in fec:
  if p.get_Parameter("Building").AsValueString() =="50B":
    print p.Name
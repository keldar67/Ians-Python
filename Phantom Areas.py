#-------------------------------------------------------------------------------
#
# Ian James
#
# Work In Progress
#
# Script to Search for Areas without a valid Area Plan and list those that 
# need attention.
#
#-------------------------------------------------------------------------------
# Global Variables
global theAreaPlans
global theLevelNames
global count
global lost
global found
global plans

#-------------------------------------------------------------------------------
#Function that takes an Area Plan Name and a Level Name and returns
#A Boolean Value:-
#  True = Area Plan Found
# False = No Area Plan Found
def AreaSchemeHasPlan(Scheme,LevelName):
  for ap in theAreaPlans:
    x = ap.AreaScheme.Name.ToString()
    y = ap.SketchPlane.Name
    if ((x == Scheme) & (y == LevelName)):
      return True
  
  return False
#-------------------------------------------------------------------------------
def GetAreaPlans(doc):
  #Filter variables taken from: http://thebuildingcoder.typepad.com/blog/2010/06/parameter-filter.html
  id = ElementId(BuiltInParameter.AREA_SCHEME_NAME)
  provider = ParameterValueProvider(id)
  evaluator = FilterStringEquals()
  sParamValue = "SearchStringHere"
  rule = FilterStringRule(provider, evaluator, sParamValue, False)

  fec = FilteredElementCollector(doc).OfClass(ViewPlan).WherePasses(filter)
#-------------------------------------------------------------------------------

plans = count = lost = found = 0
things = [0][0]

#Thanks to Captain Dan for the help filtering Area Plans for other ViewPlan views
theAreaPlans = [plan for plan in FilteredElementCollector(doc).OfClass(ViewPlan) if plan.AreaScheme != None]
for ap in theAreaPlans:
  plans = plans + 1
  
theAreas = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Areas)
for a in theAreas:
  count = count + 1
  
  result = AreaSchemeHasPlan(a.AreaScheme.Name, a.Level.Name)
  if result == False:
    print a.Id.ToString() + " :", a.Level.Name + " :", a.AreaScheme.Name
    lost = lost + 1
  else:
    found = found +1

print "-" * 10
print plans, "Area Plans in the Project"
print count, "Areas in the Project"
print lost, "Areas are Lost on Deleted Area Plans"
print found, "Areas belong to current Area Plans"
print (lost + found), ": Accounted For"
#------------------------------------------------------------------------------+
#
# Ian James : Started 1st March 2014
#
# Work In Progress: Script to find and list areas and if possible area boundary
#                   lines that don't have an area scheme and are phantom within
#                   the project
#
#------------------------------------------------------------------------------+

asNames = []
asIds = []
lvls = []
lvlIds = []

#Get all of the Area Schemes in the Project
theAreaSchemes = FilteredElementCollector(doc).OfClass(AreaScheme)
for s in theAreaSchemes:
  asNames.Add(s.Name)
  asIds.Add(s.Id.ToString())

print asNames
print asIds
print "-" * 75

#Get all of the Building Levels in the Project
theLevels = FilteredElementCollector(doc).OfClass(Level)
for lvl in theLevels:
  lvls.Add(lvl.Name)
  lvlIds.Add(lvl.Id.ToString())

#print lvls
#print lvlIds


#Test Each Area to see if it belongs to a level and an Area Scheme that has an Area Plan
theAreas = FilteredElementCollector(doc).OfClass(SpatialElement)
#for a in theAreas:
  #print a.ToString()
  #for p in a.parameters:
    #print p




#Looking for the following file
#
# <C:\Users\ijames\AppData\Roaming\Autodesk\Revit\Autodesk Revit 2014\Revit.ini>
#
# Then looking for the entry
#
# [Graphics]
# ...
# UseGraphicsHardware=0 
# ...
#
#
# UseGraphicsHardware=0 - Graphics Acceleration is OFF
# UseGraphicsHardware=1 - Graphics Acceleration is ON
#
#
#>>>doc.Application.Username returns the username as in 'ijames'
#needs to be accessed from the Application object as doc won't exist.
#
#
#


import clr
clr.AddReference("System.Core")
from System.IO import Path

def CheckGraphicsHardwareAcceleration():
  u = uiapp.Application.Username
  
  fp = Path.Combine(r"C:\Users", u, r"AppData\Roaming\Autodesk\Revit\Autodesk Revit 2014\Revit.ini")
  
  if System.IO.File.Exists(fp):
    stream = System.IO.File.OpenRead(fp)
    contents = stream.ToString()
    stream.Close
    print contents
    
  print fp
  
CheckGraphicsHardwareAcceleration()
  
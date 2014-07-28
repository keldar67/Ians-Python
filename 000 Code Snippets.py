#Snippets

#-------------------Getting the Name Property.

Element.Name.GetValue(thing)

#--------------------------------------------------------------

#-------------------Getting parameter values by Type.
Basically the methods of retrieving parameters are as follows
Element.get_Parameter("ParameterName").Value
Element.get_Parameter("ParameterName").AsValue()
Element.get_Parameter("ParameterName").AsValueString()
Element.get_Parameter("ParameterName").AsString()

Element.Name.GetValue(thing)


Converting numbers stored as strings
format(int(p.get_Parameter("E/W").AsValueString()), ',d')

#--------------------------------------------------------------


#-------------------Using Windows Message Boxes.
import clr
clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import MessageBox

MessageBox.Show("Hello World")
#--------------------------------------------------------------


#-------------------Using Dan's Logging Utility.
# Create a simple log file
log = LogFile("happydays", r"C:\000 Ian")

#Write a simple message
log.WriteMessage("hi")

#Write a dictionary
log.WriteMessage({ "name": "Ian J", "status": "awesome", "age": 18})

#Writing lots of things while keeping the file open
log.Open()
log.WriteMessage("hi")
#... many operations
log.Close()
#--------------------------------------------------------------













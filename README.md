# python-property-decorator
Repository for example demonstrating the use of the Python @property decorator 

The @property decorator is used to add accessor method to a class attribute without requiring a user to make changes to existing code. An attribute previously accessed using the standard syntax "object.attribute", can still be used in this  way, however, the attribute is now accessed through the accessor methods.

PlayerCharacter.py contains a simple example of using the @property decorator to create accessor methods to an attribute which is subsequently used. These setter methods contain a check which will raise a value in case an invalid value is being passed. Note that even in the "\_\_init\_\_" function uses these accessor methods.

Another excellent resource on the topic can be found at: https://www.programiz.com/python-programming/property 

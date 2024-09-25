#magic methods
# Built in classes define many magic methods, dir() function can show you magic methods inherited by a class.
# This code displays the magic methods inherited by int class.
print(dir(int))

# __new__: To get called in an object’s instantiation.
# __init__: To get called by the __new__ method.
# __del__: It is the destructor.
# destructor__str__(self): Defines behavior for when str() is called on an instance of your class.
# __repr__(self): To get called by built-int repr() method to return a machine readable representation of a type.
# __eq__(self, other): Defines behavior for the equality operator, ==.
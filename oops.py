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

# A Sample class with init method
class Person:

    # init method or constructor
    def __init__(self, name):
        self.name = name

    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)


p = Person('Nikhil')
p.say_hi()


# Creating a Parent Class
# A parent class is a class whose properties are inherited by the child class.
class Person(object):
  
  # Constructor
  def __init__(self, name, id):
    self.name = name
    self.id = id

  def Display(self):
    print(self.name, self.id)


emp = Person("Satyam", 102)
emp.Display()

# Creating a Child Class
# A child class is a class that drives the properties from its parent class.
class Emp(Person):
  
  def Print(self):
    print("Emp class called")
    
Emp_details = Emp("Mayank", 103)

Emp_details.Display()

Emp_details.Print()

# A Python program to demonstrate inheritance

# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"


class Person(object):

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name


    def isEmployee(self):
        return False

class Employee(Person):
    def isEmployee(self):
        return True



emp = Person("Geek1")  
print(emp.getName(), emp.isEmployee())

emp = Employee("Geek2")
print(emp.getName(), emp.isEmployee())


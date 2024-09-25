# employee.py

from person import Person

class Employee(Person):
    def isEmployee(self):
        return True

    def display(self):
        print(f'Employee: {self.name}, Employee: {self.isEmployee()}')

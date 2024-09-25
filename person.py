# person.py

class Person:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def isEmployee(self):
        return False

    def display(self):
        print(f'Person: {self.name}, Employee: {self.isEmployee()}')

class Person(object):
    def __init__(self, name, age): # Parent class constructor.
        self.name = name
        self.age = age

    def __str__(self): # Overriding __str__ from parent class **object**.
        return f'Name: {self.name}\nAge: {self.age}'

       
class Employee(Person):
    def __init__(self, name, age, wage):
        super().__init__(name, age) # super() is used to call parent class constructor.
        self.wage = wage

    def __str__(self):
        return f'{super().__str__()}\nWage: {self.wage}' # Using super() to access parent class. In this case, Person class.

# When declaring an object with inherence, parent object
# attributes should also be declared

# employee1 = employee(5000)

# test

"""
employee1 = Employee('John', 28, 5000)
print(employee1.name)
print(employee1.age)
print(employee1.wage)
"""

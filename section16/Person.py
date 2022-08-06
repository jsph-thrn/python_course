class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __add__(self, other): # other can have other name but it refers to the other object using a + operator.
        return self._name + other._name

    def __sub__(self, other):
        return self._age - other._age


person1 = Person('John', 15)
person2 = Person('Joseph', 23)

print(person1 + person2)
print(person1 - person2)

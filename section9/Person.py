# Locale zh_CN.UTF-8
# 2022年 06月 27日 星期一 22:20:56 CDT
# José Luis Yáñez Páez

# Object files (a template)

"""
class Person:
    def __init__(self): # init method, default argument self, initializer
        self.name = 'John' # defined in hard code
        self.surname = 'Perez'
        self.age = 28
"""

class Person:   # Class definition
    def __init__(self, name, surname, age):  # Constructor
        self.name = name
        self.surname = surname
        self.age = age

    def showDetail(self):   # Declare new method
        print(f'Person: {self.name} {self.surname} {self.age}')

        

ren = Person('José Luis', 'Yáñez', '23')  # creating an object of Person 
                                          # class w/o parameters
"""
print(ren.name) # access value of name attribute
print(ren.surname)
print(ren.age)
"""

ren.showDetail()    # using method directly to object, more common
Person.showDetail(ren)  # using method but from class and passing an object as
                        # arg
ren.phoneNumber = '+52555555555' # an attribute specific to the object
                                 # second object has not phoneNumber   

"""
ren.name = 'Vicente'  # Modify attribute of object ren, not recommended.
print(ren.name) 
print(ren.surname)
print(ren.age)
"""

hito = Person('Scillia', 'Carter-Wells', 45) # Second object
"""
print(hito.name)
print(hito.surname)
print(hito.age)
"""
hito.showDetail()

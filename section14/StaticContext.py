class StaticContext:
    
    classVar = 'Class attirbute' # Class attribute. This is a universal variable shared between objects created with this class. It's value will be the same always.

    def __init__(self, instanceVar): # Constructor
        self.instanceVar = instanceVar # An instance variable. This is unique for any object created with this class.

    @staticmethod   # Decorator to set a static method so it's associated with the class and not with the objects or instances. So it cannot get any instance attributes.
    def static_method(): # It cannot access self objects.
        print(StaticContext.classVar) # However, it can access class attributes.

    @classmethod # Decorator to set a class method so it's associated with the class and not with the objects.
    def class_method(cls):  # cls is the recommended reference to the class itself.
        print(cls.classVar)

    def instance_method(self):
        self.class_method(): 
        self.static_method(): # Dynamic context can access static context. This is, an object can access to the parent class' attributes but not viceversa. Class cannot access object (instance) attributes.

# The main difference between a class method and a static method is that class method can make a direct reference to the class attributes whereas a static method should specify the class name. Kinda like if it was an addon rather than a part of the class itself.

staticObject = StaticContext('Instance attribute')
staticObject1 = StaticContext('Yet another instance attribute')
StaticContext.static_method()
StaticContext.class_method()
print('First Object')
print(staticObject.classVar)
print(staticObject.instanceVar)

StaticContext.yetAnotherClassAttribute = 'New attribute declared outside of the class declaration' # Declared on-the-fly. Possible because in python a class is an object.
print(StaticContext.yetAnotherClassAttribute)

print('Second Object')
print(staticObject1.classVar) # This should print the same as staticObject.classVar
print(staticObject1.instanceVar)



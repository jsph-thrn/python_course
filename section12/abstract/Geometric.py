from abc import ABC, abstractmethod # ABC stands for Abstract Base Class, abstractmethod is a decorator

# This class will now be turned into an abstract class

class Geometric:
    def __init__(self, height, width):
        self._height = height # _ to use it within the class
        self._width = width

    @property   # @property is a decorator to state this method is accessing a incapsulated attribute.
    def height(self):
        return self._height
    
    @property
    def width(self):
        return self._width

    @height.setter
    def height(self, height):
        self._height = height

    @width.setter
    def width(self, width):
        self._width = width

    @abstractmethod
    def math_surface(self):
        pass # This states the method is declared but not implemented so it passes to the remaining code.

    def __str__(self):
       return f'Height: {self.height} units\nWidth: {self.width}'


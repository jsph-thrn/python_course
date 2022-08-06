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

    def __str__(self):
       return f'Height: {self.height} units\nWidth: {self.width}'


#Multple inherence
from Geometric import Geometric
from Color import Color

class Rectangle(Geometric, Color):
    def __init__(self, height, width, color):
        # By using super(), just one parent would be get, so will not be used.
        # For multiple inherence, it is as follows:
        Geometric.__init__(self, height, width)
        Color.__init__(self, color)

    def __str__(self):
        return f'Rectangle:\n{Geometric.__str__(self)}\n{Color.__str__(self)}'
        # return f'Height: {self.height} units\nWidth: {self.width} units\nColor: {self.color}\n'

    def math_surface(self):
        return self.height * self.width # self.side is not used because it is just used to initizalize the object and nothing else.

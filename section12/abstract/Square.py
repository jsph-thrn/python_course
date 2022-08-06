#Multple inherence
from Geometric import Geometric
from Color import Color

class Square(Geometric, Color):
    def __init__(self, side, color):
        # By using super(), just one parent would be get, so will not be used.
        # For multiple inherence, it is as follows:
        Geometric.__init__(self, side, side)
        Color.__init__(self, color)

    def __str__(self):
        return f'Square:\n{Geometric.__str__(self)}\n{Color.__str__(self)}'
        # return f'Side lenght: {self.height} units\nColor: {self.color}'

    def math_surface(self):
        return self.height * self.width # self.side is not used because it is just used to initizalize the object and nothing else.

from Square import Square
from Rectangle import Rectangle

square1 = Square(6, 'Red')
print(square1)
print(square1.math_surface())

# MRO Method Resolution Order: to find which method is resolved first 

# print(Square.mro())

rec1 = Rectangle(6, 5, 'Blue')
print(rec1)
print(rec1.math_surface())

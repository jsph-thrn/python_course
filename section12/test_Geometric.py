from Square import Square

square1 = Square(6, 'Red')
print(square1.height)
print(square1.width)
print(square1.color)
print(square1.math_surface())

# MRO Method Resolution Order: to find which method is resolved first 

print(Square.mro())

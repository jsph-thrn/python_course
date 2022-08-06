from Order import *
from Product import *

product1 = Product('Shirt', 5)
print(product1)
:product2 = Product('Pants', 8)
print(product2)
order1 = Order([product1, product2])
print(order1)
order2 = Order([product1, product2])
print(order2)

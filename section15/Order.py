from Product import *

class Order:
    orderCount = 0

    @classmethod
    def _generate_new_order_id(cls):
        cls.orderCount +=1
        return cls.orderCount

    def __init__(self, productList):
        self._orderID = Order._generate_new_order_id()
        self._productList = productList

    def add_product(self, product):
        self._productList.append(product)

    def grand_total(self):
        grandTotal = 0
        for i in self._productList:
            grandTotal += i.productValue
        return grandTotal

    def __str__(self):
        productListString = ''
        for i in self._productList:
            productListString += i.__str__() + '\n'
        
        return f'Order {self._orderID} \n{productListString}\nGrand Total {self.grand_total()} USD'


if __name__ == '__main__':
    product1 = Product('Shirt', 5)
    print(product1)
    product2 = Product('Pants', 8)
    print(product2)
    order1 = Order([product1, product2])
    print(order1)
    order2 = Order([product1, product2])
    print(order2)

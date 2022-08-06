from Computer import *

class Order:

    countOrder = 0

    @classmethod
    def generate_new_order_id(cls):
        cls.countOrder += 1
        return cls.countOrder

    def __init__(self, computerList):
        self._orderID = Order.generate_new_order_id()
        self._computerList = computerList

    def add_computer(self, computer):
        self._computerList.append(computer)
        
    def display_order_detail(self):
        self.orderDetail = ''
        for i in self._computerList:
            self.orderDetail += i.__str__() + ''

        return self.orderDetail

    def __str__(self):
        return f'Order ID: {self._orderID}\n \n{self.display_order_detail()}'


if __name__ == '__main__':
    keyboard1 = Keyboard('USB', 'Logitech')
    keyboard2 = Keyboard('USB', 'Acer')
    keyboard3 = Keyboard('USB', 'HP')
    mouse1 = Mouse('USB', 'Okuma')
    mouse2 = Mouse('USB', 'HP')
    mouse3 = Mouse('USB', 'Acer')
    mouse4 = Mouse('USB', 'Logitech')
    display1 = Display('Sony', 48, 'LED')
    display2 = Display('Dell', 20, 'LCD')
    display3 = Display('Samsung', 18, 'LCD')
    display4 = Display('Acer', 24, 'LED')
    name1 = 'Ikaria'
    name2 = 'Pasadena'
    name3 = 'Morgana'
    computer1 = Computer(name1, keyboard1, mouse1, display1)
    computer2 = Computer(name2, keyboard1, mouse2, display3)
    computer3 = Computer(name3, keyboard2, mouse4, display4)
    order1 = Order([computer1, computer2])
    order2 = Order([computer1, computer2])
    order2.add_computer(computer3)
    print(order1)
    print(order2)

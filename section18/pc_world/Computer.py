from Display import *
from Keyboard import *
from Mouse import *

class Computer:

    computerCount = 0

    @classmethod
    def generate_new_computer_id(cls):
        cls.computerCount += 1
        return cls.computerCount

    def __init__(self, name, keyboard, mouse, display):
        self._computerID = Computer.generate_new_computer_id()
        self._name = name
        self._keyboard = keyboard
        self._mouse = mouse
        self._display = display

    @property
    def keyboard(self):
        return self._keyboard

    @keyboard.setter
    def keyboard(self, keyboard):
        self._keyboard = keyboard

    @property
    def mouse(self):
        return self._mouse
    
    @mouse.setter
    def mouse(self, mouse):
        self._mouse = mouse

    @property
    def display(self):
        return self._display()
    
    @display.setter
    def display(self, display):
        self._display = display

    def __str__(self):
        return f'Computer ID: {self._computerID} Name: {self._name}\n{self._keyboard}\n{self._mouse}\n{self._display}\n\n'

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
    print(computer1)
    print(computer2)
    print(computer3)


from InputDevice import *

class Mouse:

    mouseCount = 0    

    @classmethod
    def generate_new_mouse_id(cls):
        cls.mouseCount +=1
        return cls.mouseCount

    def __init__(self, interface, vendor):
        self._mouseID = Mouse.generate_new_mouse_id()
        self._inputDevice = InputDevice(interface, vendor)

    def __str__(self):
        return f'Mouse ID: {self._mouseID} Info: [{self._inputDevice}]'

if __name__ == '__main__':

    newMouse = Mouse('USB', 'Logitech')
    print(newMouse)
    anotherMouse = Mouse('PS/2', 'Microsoft')
    print(anotherMouse)

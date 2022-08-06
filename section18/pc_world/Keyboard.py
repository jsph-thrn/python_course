from InputDevice import *

class Keyboard:

    keyboardCount = 0    

    @classmethod
    def generate_new_keyboard_id(cls):
        cls.keyboardCount +=1
        return cls.keyboardCount

    def __init__(self, interface, vendor):
        self._keyboardID = Keyboard.generate_new_keyboard_id()
        self._inputDevice = InputDevice(interface, vendor)
        

    def __str__(self):
        return f'Keyboard ID: {self._keyboardID} Info: [{self._inputDevice}]'

if __name__ == '__main__':

    newKeyboard = Keyboard('USB', 'Logitech')
    print(newKeyboard)
    anotherKeyboard = Keyboard('PS/2', 'Microsoft')
    print(anotherKeyboard)

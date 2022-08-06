class InputDevice:

    def __init__(self, interface, vendor):
        self._interface = interface
        self._vendor = vendor

    @property
    def interface(self):
        return self._interface

    @interface.setter
    def kind(self, interface):
        self._interface = interface

    @property
    def vendor(self):
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        self._vendor = vendor

    def __str__(self):
        return f'Interface: {self._interface} Vendor: {self._vendor}'

if __name__ == '__main__':
    newDevice = InputDevice('USB', 'HP')
    print(newDevice)

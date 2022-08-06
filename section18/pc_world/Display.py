class Display:

    displayCount = 0

    @classmethod
    def generate_new_display_id(cls):
        cls.displayCount += 1
        return cls.displayCount

    def __init__(self, vendor, size, kind):
        self._displayID = Display.generate_new_display_id()
        self._vendor = vendor
        self._size = size
        self._kind = kind

    @property
    def vendor(self):
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        self._vendor = vendor

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    @property
    def kind(self):
        return self._kind

    @kind.setter
    def kind(self, kind):
        self._kind = kind

    def __str__(self):
        return f'Display ID: {self._displayID} Info: [Vendor: {self._vendor} Size: {self._size} in Type: {self._kind}]'


if __name__ == '__main__':
    newDisplay = Display('Dell', 18, 'LCD')
    print(newDisplay)
    anotherDisplay = Display('Sony', 48, 'LED TV')
    print(anotherDisplay)

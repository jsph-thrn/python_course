class Product:
    productCounter = 0

    @classmethod
    def generate_new_product_id(cls):
        cls.productCounter +=1
        return cls.productCounter

    def __init__(self, productConcept, productValue):
        self._productID = self.generate_new_product_id()
        self._productConcept = productConcept
        self._productValue = productValue

    @property
    def productID(self):
        return self._productID

    @productID.setter
    def productID(self, productID):
        self._productID = productID

    @property
    def productConcept(self):
        return self._productConcept

    @productConcept.setter
    def productConcept(self, productConcept):
        self._productConcept = productConcept

    @property
    def productValue(self):
        return self._productValue

    @productValue.setter
    def productValue(self, productValue):
        self._productValue = productValue
    
    def __str__(self):
        return f'ID: {self._productID} Concept: {self._productConcept} Price: {self._productValue} USD'

if __name__ == '__main__':
    product1 = Product('Shirt', 5)
    print(product1)
    product2 = Product('Pants', 8)
    print(product2)

class Car:
    carCounter = 0
    
    @classmethod
    def _generate_new_id(cls):
        cls.carCounter += 1
        return cls.carCounter

    def __init__(self, model, releaseYear):
        # Car.carCounter +=1 directly increasing the counter.
        # self.carID = Car.carCounter
        self.carID = self._generate_new_id()
        self.model = model
        self.releaseYear = releaseYear

    def __str__(self):
        return f'Car {self.carID}: [Model: {self.model}, Release year: {self.releaseYear}]'

# When issuing a new object, the counter will be increased by 1

car1 = Car('Versa', '2016')
print(car1)
car2 = Car('Topaz', '1993')
print(car2)
car3 = Car('270z Fairlady', 1986)
print(car3)

print(f'Count: {Car.carCounter}')

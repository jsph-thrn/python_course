"""
Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Coche y Bicicleta,
las cuales heredan de la clase Padre Vehiculo.
La clase padre debe tener los siguientes atributos y métodos

Vehiculo (Clase Padre):
-Atributos (color, ruedas)
-Métodos ( __init__() y __str__ )

Coche  (Clase Hija de Vehículo) (Además de los atributos y métodos heradados de Vehículo):
-Atributos ( velocidad (km/hr) )
-Métodos ( __init__() y __str__() )

Bicicleta  (Clase Hija de Vehículo) (Además de los atributos y métodos heradados de Vehículo):
-Atributos ( tipo (urbana/montaña/etc )
-Métodos ( __init__() y __str__() )
"""

class Vehicle(object): # This line can be declared without **(object)**, as, by default, it takes inherence from object class.
    def __init__(self, color, wheels):
        self.color = color
        self.wheels = wheels

    def __str__(self):
        return f'Color: {self.color}\n# of wheels: {self.wheels}'

class Car(Vehicle):
    def __init__(self, color, wheels, speed):
        super().__init__(color, wheels)
        self.speed = speed
    
    def __str__(self):
        return f'{super().__str__()}\nSpeed: {self.speed} km/h' # Remember append () at the end of super().__str__()

class Bycicle(Vehicle):
    def __init__(self, color, wheels, kind):
        super().__init__(color, wheels)
        self.kind = kind

    def __str__(self):
        return f'{super().__str__()}\nType: {self.kind}'


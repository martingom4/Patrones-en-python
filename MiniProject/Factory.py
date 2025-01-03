from abc import ABC, abstractmethod

#producto abstracto

class factoryCar(ABC):
    @abstractmethod
    def createCar(self):
        pass


class gasolineCar(factoryCar):
    def __init__(self):
        self.velocidad_maxima = 180
        self.tipo_combustible = "Gasolina"


    def createCar(self):
        return f"Velocidad Maxima: {self.velocidad_maxima} Tipo de Combustible: {self.tipo_combustible}"


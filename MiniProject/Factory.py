from abc import ABC, abstractmethod

# Clases Abstractas y Concretas de Vehículos
class Vehiculo(ABC):
    @abstractmethod
    def descripcion(self):
        pass

class AutoElectrico(Vehiculo):
    def __init__(self):
        self.velocidad_maxima = 150
        self.tipo_bateria = "Litio"

    def descripcion(self):
        return f"Auto eléctrico con batería {self.tipo_bateria}, velocidad máxima {self.velocidad_maxima} km/h"

class AutoCombustion(Vehiculo):
    def __init__(self):
        self.velocidad_maxima = 200
        self.tipo_motor = "Gasolina"

    def descripcion(self):
        return f"Auto de combustión con motor {self.tipo_motor}, velocidad máxima {self.velocidad_maxima} km/h"

# Factory de Vehículos
class VehiculoFactory:
    @staticmethod
    def crear_vehiculo(tipo, categoria):
        if tipo == "auto" and categoria == "electrico":
            return AutoElectrico()
        elif tipo == "auto" and categoria == "combustion":
            return AutoCombustion()
        else:
            raise ValueError(f"Tipo o categoría no válidos: {tipo}, {categoria}")

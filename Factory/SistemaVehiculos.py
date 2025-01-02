from abc import ABC, abstractmethod

# Producto Abstracto
class Carros(ABC):
    @abstractmethod
    def crear(self):
        pass

# Productos Concretos
class crearauto(Carros):
    def crear(self):
        return "Auto creado"

class crearbus(Carros):
    def crear(self):
        return "Bus creado"

class crearbicicleta(Carros):
    def crear(self):
        return "Bicicleta creada"

# Factory
class CarrosFactory:
    @staticmethod
    def crear_carros(tipo):
        if tipo == "auto":
            return crearauto()
        elif tipo == "bus":
            return crearbus()
        elif tipo == "bicicleta":
            return crearbicicleta()
        else:
            raise ValueError("Tipo de vehículo no válido")

# Cliente
factory = CarrosFactory()

auto = factory.crear_carros("auto")
print(auto.crear())  # Auto creado

bus = factory.crear_carros("bus")
print(bus.crear())  # Bus creado

bicicleta = factory.crear_carros("bicicleta")
print(bicicleta.crear())  # Bicicleta creada


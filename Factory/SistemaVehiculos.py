from abc import ABC, abstractmethod

# Producto Abstracto
""" se utiliza para definir métodos abstractos en una clase base abstracta. Un método abstracto es un método que se declara en una clase base, pero no se implementa. Las subclases que heredan de esta clase base deben proporcionar una implementación concreta de estos métodos abstractos."""
class Carros(ABC):
    @abstractmethod
    def crear(self):
        pass

    def mover(self):
        pass

    def detenerse(self):
        pass

#tambien podemos crear clases abstractas para poder heredar de ellas y poder sobreescribir los metodos pero se heredan de la prinsipal que es Carros(ABC) y se sobreescriben en las clases hijas que son los productos concretos que son crearauto, crearbus, crearbicicleta


# Productos Concretos
class crearauto(Carros):
    def __init__(self):
        self.velocidad_maxima = 200
        self.combustible = "Gasolina"

    def crear(self):
        return "Auto creado"

    def mover(self):
        return "Auto en movimiento"

    def detenerse(self):
        return "Auto detenido"


class crearbus(Carros):
    def crear(self):
        return "Bus creado"

    def mover(self):
        return "Auto en movimiento"

    def detenerse(self):
        return "Auto detenido"

class crearbicicleta(Carros):
    def crear(self):
        return "Bicicleta creada"

    def mover(self):
        return "Auto en movimiento"

    def detenerse(self):
        return "Auto detenido"


class AutoElectrico(VehiculoElectrico):
    def crear(self):
        return "Auto eléctrico creado"

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
print(auto.mover())  # El auto está en movimiento
print(auto.detenerse())  # El auto se ha detenido



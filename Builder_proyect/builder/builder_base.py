#aca vamos a poner las clases abstractas
from abc import ABC, abstractmethod
from producto import Vehiculo

class builder_vehiculo(ABC):
    def __init__(self):
        self.vehiculo = Vehiculo() #creamos un objeto de tipo vehiculo

    @abstractmethod
    def agregar_motor(self):
        pass

    @abstractmethod
    def agregar_puertas(self):
        pass

    @abstractmethod
    def agregar_audio_premium(self):
        pass

    def obtener_vehiculo(self):
        return self.vehiculo #retornamos el vehiculo construido

    "retornamos los vehiculos construidos pasados por el constructor de la clase builder correspondiente a cada vehiculo"

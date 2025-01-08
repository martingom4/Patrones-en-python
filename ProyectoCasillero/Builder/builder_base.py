from abc import ABC, abstractmethod
from ProyectoCasillero.paquetes import paquete
'''
Propósito: Crear diferentes configuraciones de paquetes.

Requisitos:

Implementa un Builder Abstracto para definir los pasos básicos:

Configurar dimensiones.

Configurar peso.

Configurar estado inicial.

Calcular costo estimado.

Crea Builders Concretos para diferentes tipos de paquetes:

Estándar: Dimensiones y peso típicos.

Grande: Dimensiones y peso mayores.

Frágil: Dimensiones normales, pero con un costo adicional por ser frágil.

'''
class builder_paquete(ABC):
    def __init__(self):
        self.vehiculo = paquete() # creamos un objeto de tipo paquete que ya esta definido en el archivo paquete.py
    #aca podemos agregar los metodos que queramos para agregar los paquetes como agregar_dimensiones agregar_peso agregar_destino etc

    #metodos abstracto que se va a implementar en las clases hijas
    @abstractmethod
    def configurar_dimensiones(self):
        pass

    @abstractmethod
    def configurar_peso(self):
        pass

    @abstractmethod
    def calcular_precio(self):
        pass





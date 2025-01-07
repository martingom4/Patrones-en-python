#aca pondremos las clases dedicadas a cada tipo de vehiculo
from builder.builder_base import builder_vehiculo

class builder_bus(builder_vehiculo):
    def agregar_motor(self):
        self.vehiculo.agregar_pieza("Motro de 500 caballos de fuerza")

        

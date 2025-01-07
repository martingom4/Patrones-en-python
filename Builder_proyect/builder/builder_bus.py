#aca pondremos las clases dedicadas a cada tipo de vehiculo
from builder.builder_base import builder_vehiculo

class builder_bus(builder_vehiculo):
    def agregar_motor(self):
        self.vehiculo.agregar_pieza("motor de bus 5000cc")

    def agregar_puerta(self):
        self.vehiculo.agregar_pieza("4 puertas")

    def agregar_audio_premium(self):
        self.vehiculo.agregar_pieza("audio premium")

        

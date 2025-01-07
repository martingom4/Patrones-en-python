#aca pondremos las clases dedicadas a cada tipo de vehiculo
from builder.builder_base import builder_vehiculo

class builder_coche(builder_vehiculo):
    def agregar_motor(self):
        self.vehiculo.agregar_pieza("Motro de 500 caballos de fuerza")
    def agregar_puertas(self):
        self.vehiculo.agregar_pieza("3 Puertas")
    def agregar_audio_premium(self):
        self.vehiculo.agregar_pieza("Sistema de audio premium")

    


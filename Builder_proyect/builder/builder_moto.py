from builder.builder_base import builder_vehiculo

class builder_moto(builder_vehiculo):
    def agregar_motor(self):
        self.vehiculo.agregar_pieza("motor de moto 500cc")

    def agregar_puertas(self):
        self.vehiculo.agregar_pieza("0 puertas")

    def agregar_audio_premium(self):
        self.vehiculo.agregar_pieza("audio premium")
        

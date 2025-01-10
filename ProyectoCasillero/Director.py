class Director:
    def __init__(self, builder):
        self.builder = builder  # Builder concreto

    def construir_paquete(self):
        self.builder.dimensiones()
        self.builder.peso()
        self.builder.calcular_precio()

    def obtener_paquete(self):
        return self.builder.obtener_paquete()

from Builder.builder_base import builder_paquete

class builder_estandar(builder_paquete):
    def dimensiones(self):
        self.paquete.ancho = 10
        self.paquete.alto = 10
        self.paquete.largo = 10


    def peso(self):
        self.paquete.peso = 4

    def calcular_precio(self):
        volumen = self.paquete.ancho * self.paquete.alto * self.paquete.largo
        self.paquete.precio = volumen * self.paquete.peso




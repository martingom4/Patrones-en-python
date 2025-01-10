from Builder.builder_base import builder_paquete
from ProyectoCasillero.paquetes import paquetes

class builder_estandar(builder_paquete):
    def configurar_dimensiones(self):
        prueba = self.paquete.dimensiones(10, 10, 10)
        paquetes.agregar_paquete(prueba)

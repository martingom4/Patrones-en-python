# Clase director
# director.py
class Director:
    def __init__(self, builder):
        self.builder = builder

    def construir_vehiculo(self, pasos):
        for paso in pasos:
            if hasattr(self.builder, paso):
                getattr(self.builder, paso)()
            else:
                print(f"El builder no tiene el método: {paso}")

    def obtener_vehiculo(self):
        return self.builder.obtener_vehiculo()

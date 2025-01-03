from Factory import VehiculoFactory  # Importa la Factory
from Singleton import RegistroVehiculos  # Importa el Singleton

class VehiculoApp:
    def __init__(self):
        self.factory = VehiculoFactory()
        self.registro = RegistroVehiculos()

    def crear_y_registrar(self, tipo, categoria):
        try:
            vehiculo = self.factory.crear_vehiculo(tipo, categoria)
            self.registro.registrar_vehiculo(vehiculo)
            print(f"Vehículo registrado: {vehiculo.descripcion()}")
        except ValueError as e:
            print(e)

    def listar_vehiculos(self):
        vehiculos = self.registro.listar_vehiculos()
        if vehiculos:
            print("Vehículos registrados:")
            for v in vehiculos:
                print(f"- {v}")
        else:
            print("No hay vehículos registrados.")

# Pruebas
if __name__ == "__main__":
    app = VehiculoApp()

    # Crear y registrar vehículos
    app.crear_y_registrar("auto", "electrico")
    app.crear_y_registrar("auto", "combustion")
    app.crear_y_registrar("bus", "electrico")  # Esto fallará como ejemplo de error

    # Listar vehículos
    app.listar_vehiculos()

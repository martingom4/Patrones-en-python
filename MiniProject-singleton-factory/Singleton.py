class RegistroVehiculos:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.vehiculos = []
        return cls._instance

    def registrar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def listar_vehiculos(self):
        return [v.descripcion() for v in self.vehiculos]

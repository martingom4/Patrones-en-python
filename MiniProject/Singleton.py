class Register:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.vheicle = [] #aca se guardan los vehiculos unicos creados para poder listarlos despues en el menu
        return cls._instance

    def addVehicle(self, vehicle):
        self.vheicle.append(vehicle)

    def listVehicle(self):
        for vehicle in self.vehicle:
            print(vehicle)





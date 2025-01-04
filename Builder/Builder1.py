'''
Supongamos que necesitas construir un vehículo con características opcionales como tipo de motor, número de puertas, sistema de audio, y más.'''

class Vehiculo: #clase base para los vehiculos
    def __init__(self):
        self.piezas = [] # guardo todas las piezas que voy a agregar en el vehiculo en una lista que se ira llenando progresivamente

    def agregar_pieza(self, pieza ):
        self.piezas.append(pieza)# pieza va a ser lo que el cliente le va agregar al vehiculo

    def especificaciones(self):
        return f"Vehiculo contruido con: {', '.join(self.piezas)}" # se usa el join para unir las piezas que se van agregando al vehiculo y listarlas


'''una vez que se tiene la clase base se puede crear una clase Builder que va a ser la encargada de construir el vehiculo con las piezas que el cliente le va a agregar'''

#primero sera la clase abstracta Builder

class BuilderVehiculo:
    def __init__(self):
        self.vehiculo = Vehiculo() # se crea un objeto de la clase vehiculo para poder agregarle las piezas

    '''todas estas son las piezas que se le pueden agregar al vehiculo, pero no se le agregan directamente al vehiculo sino que se le agregan al Builder'''

    def agregar_motor(self):
        pass
    def agregar_puertas(self):
        pass
    def agregar_audio_premium(self):
        pass

    def obtener_vehiculo(self):
        return self.vehiculo # se retorna el vehiculo con las piezas que se le agregaron

'''despues vamos a crear una clase Builder concreta que va a ser la encargada de agregar las piezas'''

class BuilderCoche(BuilderVehiculo):
    def agregar_motor(self):
        self.vehiculo.agregar_pieza("Motor de 4 cilindros") # se agrega la pieza al vehiculo a traves de la clase Builder y no directamente al vehiculo como tal

    def agregar_puertas(self):
        self.vehiculo.agregar_pieza("4 puertas ")

    def agregar_audio_premium(self):
        self.vehiculo.agregar_pieza("Sistema de audio premium")

# apartir de el mismo builder abstracto se pueden crear mas tipos de vehiculos con las piezas que el cliente le va a agregar

class BuilderMoto(BuilderVehiculo):
    def agregar_motor(self):
        self.vehiculo.agregar_pieza("Motor de 2 cilindros")
    def agregar_puertas(self):
        self.vehiculo.agregar_pieza("0 puertas")
    def agregar_llanta(self):
        self.vehiculo.agregar_pieza("Llantas de 20 pulgadas")

class BuilderBus(BuilderVehiculo):
    def agregar_motor(self):
        self.vehiculo.agregar_pieza("Motor de 8 cilindros")
    def agregar_puertas(self):
        self.vehiculo.agregar_pieza("2 puertas")
    def agregar_llanta(self):
        self.vehiculo.agregar_pieza("Llantas de 30 pulgadas")
    def Agregar_capacidad(self):
        self.vehiculo.agregar_pieza("Capacidad para 80 personas")

class BuilderCamioneta(BuilderVehiculo):
    def agregar_motro(self):
        self.vehiculo.agregar_pieza("Motor de 6 cilindros")
    def agregar_puertas(self):
        self.vehiculo.agregar_pieza("4 puertas")
    def agregar_llantas(self):
        self.vehiculo.agregar_pieza("Llantas de 25 pulgadas")
    def agregar_caja(self):
        self.vehiculo.agregar_pieza("Caja de 2 metros")



'''se puede ver que no se retorna nada porque el Builder ya tiene un metodo que retorna el vehiculo con las piezas que se le agregaron ademas solo estamos agregando las piezas al vehiculo a traves de la clase Builder y no directamente al vehiculo como tal'''

'''una vez que se tiene la clase Builder concreta se puede crear la clase Director que va a ser la encargada de construir el vehiculo con las piezas que el cliente le va a agregar'''


class Director:
    def __init__(self, builder):
        self.builder = builder

    def construir_vehiculo(self):
        self.builder.agregar_motor()
        self.builder.agregar_puertas()
        self.builder.agregar_audio_premium()
        '''se llama a los metodos de la clase Builder para agregar las piezas al vehiculo segun lo que el cliente le va a agregar'''
    def construir_moto(self):
        self.builder.agregar_motor()
        self.builder.agregar_puertas()
        self.builder.agregar_llanta()
    def contruir_bus(self):
        self.builder.agregar_motor()
        self.builder.agregar_puertas()
        self.builder.agregar_llanta()
        self.builder.Agregar_capacidad()
    def contruir_camioneta(self):
        self.builder.agregar_motor()
        self.builder.agregar_puertas()
        self.builder.agregar_llantas()
        self.builder.agregar_caja()

    def obtener_vehiculo(self):
        return self.builder.obtener_vehiculo() # se retorna el vehiculo con las piezas que se le agregaron




'''una vez que se tiene la clase Director se puede crear el cliente que va a ser el encargado de construir el vehiculo con las piezas que el cliente le va a agregar'''

builder = BuilderCoche() # se crea un objeto de la clase Builder concreta
director = Director(builder) # se crea un objeto de la clase Director
director.construir_vehiculo() # se llama al metodo de la clase Director para construir el vehiculo con las piezas que el cliente le va a agregar
vehiculo = director.obtener_vehiculo() # se guarda el vehiculo con las piezas que se le agregaron
print(vehiculo.especificaciones()) # se imprime el vehiculo con las piezas que se le agregaron


builder = BuilderMoto() # se crea un objeto de la clase Builder concreta
director = Director(builder)
director.construir_moto()
vehiculo = director.obtener_vehiculo()
print(vehiculo.especificaciones())


builder = BuilderBus()
director = Director(builder)
director.contruir_bus()
vehiculo = director.obtener_vehiculo()
print(vehiculo.especificaciones())


builder = BuilderCamioneta()
director = Director(builder)
director.contruir_camioneta()
vehiculo = director.obtener_vehiculo()
print(vehiculo.especificaciones())

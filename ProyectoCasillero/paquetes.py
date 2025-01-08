# esta clase es para unir muchos paquetes que se van a crear a medida que el cliente lo va solicitando

# y esta clase es la que se encarga de crear los paquetes que se van a enviar
class paquetes:
    def __init__(self):
        self.paquetes = [] #lista de paquetes con el metodo append se agregan los paquetes a la lista

    def agregar_paquete(self, paquetes):
        self.paquetes.append(paquetes)

    def especificaciones(self):
        return f"El paqute contiene {','.join(self.paquetes )}" #esto lo que hace es juntar todo lo que tendra el paquete y lo separa por comas




# terminada la clase paquete se procede a crear la clase Builder para el patron Builder

#clase Vehiculo
class Vehiculo:
    def __init__(self):
        self.piezas = []

    def agregar_pieza(sefl, pieza):
        sefl.piezas.append(pieza)

    def especificaciones(sefl):
        return f"Vehiculo construido con {', '.join(sefl.piezas)}"



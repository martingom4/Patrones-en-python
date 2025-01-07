#clase usuario
class usuario:
    def __init__(self,nombre, email,tipo,limite_paquetes):
        self.nombre = nombre
        self.email = email
        self.tipo = tipo
        self.limite_paquetes = limite_paquetes


    def __str__(self):
        return f"Nombre: {self.nombre}, Email: {self.email}, Tipo: {self.tipo}, Limite de paquetes: {self.limite_paquetes}"

    

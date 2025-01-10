#aca sera el paquete que se va a enviar 1 a 1
'''
ropósito: Representar a un usuario en el sistema.

Requisitos:

Cada usuario debe tener los siguientes atributos:

Nombre completo (nombre).

Email (email).

Tipo (tipo): Personal o Corporativo.

Límite de paquetes (limite_paquetes).

Implementa un método que retorne una descripción clara del usuario en formato de texto (por ejemplo: __str__).
'''

class Paquete:
    def __init__(self,nombre, email,tipo,limite_paquetes,ancho,alto,largo,peso):
        #aca estoy definiendo las variables a usar en la clase
        self.nombre = nombre
        self.email = email
        self.tipo = tipo
        self.limite_paquetes = limite_paquetes
        self.ancho = ancho
        self.alto = alto
        self.largo = largo
        self.peso = peso

    def __str__(self):
        return f"Nombre: {self.nombre}, Email: {self.email}, Tipo: {self.tipo}, Limite de paquetes: {self.limite_paquetes} Ancho: {self.ancho} Alto: {self.alto} Largo: {self.largo} Peso: {self.peso}"

#entonces esto lo que hace es que crea un objeto de tipo paqute con los atributos que le pasamos en el constructor

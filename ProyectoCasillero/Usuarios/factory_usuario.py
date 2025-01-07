#aca vamos a crear dos tipos de usuarios para probar el sistema
'''
Propósito: Crear instancias de usuarios según su tipo.

Requisitos:

La Factory debe ser capaz de crear usuarios de dos tipos:

Personal: Con un límite básico de paquetes (por ejemplo, 5 paquetes).

Corporativo: Con un límite mayor de paquetes (por ejemplo, 50 paquetes).

Valida que el tipo proporcionado sea válido. Si no lo es, lanza una excepción o devuelve un mensaje claro.


'''
from Usuarios.usuario import usuario

class factory_usuario:
    @staticmethod
    def crear_usuario(tipo, nombre, email):
        if tipo == "personal":
            return usuario(nombre, email, "personal", limite_paquetes=5)
        elif tipo == "corporativo":
            return usuario(nombre, email, "corporativo", limite_paquetes=50)
        else:
            raise ValueError(f"Tipo de usuario '{tipo}' no es válido")



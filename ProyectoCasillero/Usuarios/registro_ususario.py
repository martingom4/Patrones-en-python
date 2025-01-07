#singleton para gestionar los usuarios

'''
Propósito: Mantener un registro único de usuarios en el sistema.

Requisitos:

Usa el patrón Singleton para asegurar que solo exista una instancia del registro.

El registro debe:

Permitir agregar usuarios al sistema.

Evitar duplicados (por ejemplo, basándote en el email).

Listar todos los usuarios registrados.

Implementa un método para buscar un usuario por su email y devolver su información.


'''


class registro_usuario:
    _instance = None # Variable de clase para almacenar la instancia única
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def listar_usuarios(self):
        return [str(usuario) for usuario in self.usuarios]



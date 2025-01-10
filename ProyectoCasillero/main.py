from Usuarios.factory_usuario import factory_usuario
from Usuarios.registro_ususario import registro_usuario
from Builder.builder_estandar import builder_estandar
from Director import Director
from paquetes import paquetes

def main():
    # *** Gestión de Usuarios ***
    # Crear usuarios
    usuario1 = factory_usuario.crear_usuario("personal", "Juan Pérez", "juan@example.com")
    usuario2 = factory_usuario.crear_usuario("corporativo", "Empresa ABC", "contacto@empresa.com")

    # Registrar usuarios
    registro_usuarios = registro_usuario()
    registro_usuarios.agregar_usuario(usuario1)
    registro_usuarios.agregar_usuario(usuario2)

    # Listar usuarios registrados
    print("Usuarios Registrados:")
    usuarios = registro_usuarios.listar_usuarios()
    for u in usuarios:
        print(u)

    # *** Gestión de Paquetes ***
    # Crear registro de paquetes
    registro_paquetes = paquetes()

    # Crear un paquete para Juan Pérez
    print("\nCreando un paquete para Juan Pérez:")
    builder = builder_estandar()
    director = Director(builder)
    director.construir_paquete()
    paquete1 = director.obtener_paquete()

    # Agregar el paquete al registro global
    registro_paquetes.agregar_paquete(paquete1)

    # Crear otro paquete para Empresa ABC
    print("\nCreando un paquete para Empresa ABC:")
    director = Director(builder)
    director.construir_paquete()
    paquete2 = director.obtener_paquete()

    # Agregar el paquete al registro global
    registro_paquetes.agregar_paquete(paquete2)

    # Listar todos los paquetes registrados
    print("\nPaquetes Registrados:")
    paquetess = registro_paquetes.especificaciones()
    print(paquetess)

if __name__ == "__main__":
    main()

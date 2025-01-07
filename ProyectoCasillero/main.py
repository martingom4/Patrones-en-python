#punto de entrada de el programa
from Usuarios.factory_usuario import factory_usuario
from Usuarios.registro_ususario import registro_usuario

def main():
    # Crear usuarios
    usuario1 = factory_usuario.crear_usuario("personal", "Juan Pérez", "juan@example.com")
    usuario2 = factory_usuario.crear_usuario("corporativo", "Empresa ABC", "contacto@empresa.com")

    # Registrar usuarios
    registro = registro_usuario()
    registro.agregar_usuario(usuario1)
    registro.agregar_usuario(usuario2)

    # Listar usuarios
    usuarios = registro.listar_usuarios()
    for u in usuarios:
        print(u)

if __name__ == "__main__":
    main()

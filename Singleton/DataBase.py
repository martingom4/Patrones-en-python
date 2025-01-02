class DataBaseConnection:
    _instance = None
    _initialized= False

    def __new__(cls, *args, **kwars):
        if not cls._instance:
            print("Creando una nueva instancia de conexion a la base de datos")
            cls._instance = super().__new__(cls, *args, **kwars)
        return cls._instance

    def __init__(self):
        if not DataBaseConnection._initialized:
            print("Inicializando la conexion a la base de datos")
            self.status = "Conexion cerrada"
            DataBaseConnection._initialized = True

    def connect(self):
        if self.status == "Connected":
            print("Ya esta conectado a la base de datos")
        else:
            print("Conectando a la base de datos")
            self.status = "Connected"

    def disconnect(self):
        if self.status == "Connected":
            print("La conexion esta cerrada")
        else:
            print("Cerrando la conexion a la base de datos")
            self.status = "Disconnected"


# Crear dos instancias
db1 = DataBaseConnection()
db2 = DataBaseConnection()

# Verificar que ambas son la misma instancia
print(db1 is db2)  # True

# Conectar usando la primera instancia
db1.connect()  # Conectando a la base de datos...

# Intentar conectar de nuevo con la segunda instancia
db2.connect()  # Ya estás conectado a la base de datos.

# Desconectar usando la segunda instancia
db2.disconnect()  # Cerrando conexión a la base de datos...

# Verificar el estado final
print(db1.status)  # Disconnected
print(db2.status)  # Disconnected

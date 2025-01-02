class ConfigManager:
    _instance = None  # Variable de clase para almacenar la instancia única
    _initialized = False  # Controla si la instancia ha sido inicializada

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not ConfigManager._initialized:
            self.config = {}  # Diccionario para almacenar configuraciones
            ConfigManager._initialized = True

    def load_config(self, file_path):
        """
        Carga configuraciones desde un archivo clave-valor.
        """
        try:
            with open(file_path, "r") as file:
                for line in file:
                    line = line.strip()
                    if "=" in line and not line.startswith("#"):
                        key, value = line.split("=", 1)
                        self.config[key.strip()] = value.strip()
        except FileNotFoundError:
            print(f"Error: El archivo {file_path} no existe.")
        except Exception as e:
            print(f"Error al cargar configuraciones: {e}")

    def get_config(self, key):
        """
        Devuelve el valor asociado a una clave en la configuración.
        Si la clave no existe, devuelve None.
        """
        return self.config.get(key, None)

    def set_config(self, key, value):
        """
        Agrega o actualiza una configuración con la clave y el valor proporcionados.
        """
        self.config[key] = value

    def save_config(self, file_path):
        """
        Guarda las configuraciones actuales en un archivo de texto.
        Cada configuración se escribe en formato clave=valor.
        """
        try:
            with open(file_path, "w") as file:
                for key, value in self.config.items():
                    file.write(f"{key}={value}\n")
            print(f"Configuraciones guardadas en {file_path}")
        except Exception as e:
            print(f"Error al guardar configuraciones: {e}")



# Crear instancia y cargar configuraciones
config_manager = ConfigManager()
config_manager.load_config("config.txt")

# Obtener una configuración
print(config_manager.get_config("db_host"))  # localhost
print(config_manager.get_config("debug"))  # True
print(config_manager.get_config("missing_key"))  # None

# Actualizar y agregar configuraciones
config_manager.set_config("debug", "False")
config_manager.set_config("new_key", "new_value")

# Guardar las configuraciones actualizadas
config_manager.save_config("config_updated.txt")

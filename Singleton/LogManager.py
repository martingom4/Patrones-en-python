class logManager:
    _instance = None # Variable de clase para almacenar la instancia única
    _initialized = False # Variable de clase para almacenar si la instancia ha sido inicializada
    _log_file = "log.txt" # Variable de clase para almacenar el nombre del archivo de registro

    def __new__(cls, *args, **kwargs):
        if not cls._instance: # si no existe la instancia
            print("Creando la instancia principal de logManager")
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not logManager._initialized:
            print(f"Iniciando el LogManager con el archivo: {self._log_file}")
            self._log_file = logManager._log_file
            logManager._initialized = True

    def write_log(self,message, level="INFO"): #abrir el archivo y escribir el mensaje con el nivel de log
        with open(self._log_file, "a") as file:
            file.write(f"[{level}] {message}\n")



log1 = logManager()
log2 = logManager()

# Verifica que ambas son la misma instancia
print(log1 is log2)  # True

# Escribe logs con diferentes niveles
log1.write_log("Este es un mensaje informativo.", level="INFO")
log2.write_log("Este es un mensaje de advertencia.", level="WARNING")
log1.write_log("Este es un mensaje de error.", level="ERROR")

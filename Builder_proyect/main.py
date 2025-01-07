#punto de entrada de la aplicacion
# main.py
from builder.builder_coche import builder_coche
from builder.builder_bus import builder_bus
from builder.builder_moto import builder_moto
from director import Director

def main():
    # Crear un coche
    builder = builder_coche()
    director = Director(builder)
    director.construir_vehiculo(["agregar_motor", "agregar_puertas", "agregar_audio_premium"])
    coche = director.obtener_vehiculo()
    print(coche.especificaciones())

    # Crear un bus
    builder = builder_bus()
    director = Director(builder)
    director.construir_vehiculo(["agregar_motor", "agregar_puertas", "agregar_audio_premium"])
    bus = director.obtener_vehiculo()
    print(bus.especificaciones())

    # Crear una moto
    builder = builder_moto()
    director = Director(builder)
    director.construir_vehiculo(["agregar_motor", "agregar_puertas", "agregar_audio_premium"])
    moto = director.obtener_vehiculo()
    print(moto.especificaciones())

if __name__ == "__main__":
    main()

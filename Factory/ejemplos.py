from abc import ABC, abstractmethod

# Producto Abstracto
class Notificacion(ABC):
    @abstractmethod #creamos una clase abstracta de la que se pueden derivar varias funcionalidades 
    def enviar(self, mensaje):
        pass

# Productos Concretos
class EmailNotificacion(Notificacion):
    def enviar(self, mensaje):
        print(f"Enviando Email: {mensaje}")

class SMSNotificacion(Notificacion):
    def enviar(self, mensaje):
        print(f"Enviando SMS: {mensaje}")

class PushNotificacion(Notificacion):
    def enviar(self, mensaje):
        print(f"Enviando Push: {mensaje}")

# Clase Factory
class NotificacionFactory:
    @staticmethod
    def crear_notificacion(tipo):
        if tipo == "email":
            return EmailNotificacion()
        elif tipo == "sms":
            return SMSNotificacion()
        elif tipo == "push":
            return PushNotificacion()
        else:
            raise ValueError("Tipo de notificación no válido")

# Uso del Factory
factory = NotificacionFactory()
notificacion = factory.crear_notificacion("email")
notificacion.enviar("Hola desde el patrón Factory!")

notificacion_sms = factory.crear_notificacion("sms")
notificacion_sms.enviar("Hola desde SMS!")

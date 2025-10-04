from datetime import datetime

class Actividad:
    def __init__(self, id_actividad, nombre, duracion_min):
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        if duracion_min < 1:
            raise ValueError("La duración mínima es de 1 minuto.")
        
        self.id_actividad = id_actividad
        self.__nombre = nombre
        self.__duracion_min = duracion_min
        self.__historial_eventos = []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def duracion_min(self):
        return self.__duracion_min

    @property
    def historial_eventos(self):
        return self.__historial_eventos.copy()

    def actualizar_nombre(self, nuevo_nombre):
        if not nuevo_nombre:
            raise ValueError("El nuevo nombre no puede estar vacío.")
        evento = {
            "fecha": datetime.now(),
            "campo": "nombre",
            "anterior": self.__nombre,
            "nuevo": nuevo_nombre
        }
        self.__nombre = nuevo_nombre
        self.__historial_eventos.append(evento)

    def actualizar_duracion(self, nueva_duracion):
        if nueva_duracion < 1:
            raise ValueError("La duración mínima es de 1 minuto.")
        evento = {
            "fecha": datetime.now(),
            "campo": "duracion_min",
            "anterior": self.__duracion_min,
            "nuevo": nueva_duracion
        }
        self.__duracion_min = nueva_duracion
        self.__historial_eventos.append(evento)
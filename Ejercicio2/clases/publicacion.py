from datetime import datetime

class Publicacion:
    def __init__(self, id_publicacion, titulo, anio):
        if not titulo:
            raise ValueError("El título no puede estar vacío.")
        if anio < 1450:
            raise ValueError("El año debe ser igual o mayor a 1450.")
        
        self.id_publicacion = id_publicacion
        self.__titulo = titulo
        self.__anio = anio
        self.__historial_eventos = []

    @property
    def titulo(self):
        return self.__titulo

    @property
    def anio(self):
        return self.__anio

    @property
    def historial_eventos(self):
        return self.__historial_eventos.copy()

    def actualizar_titulo(self, nuevo_titulo):
        if not nuevo_titulo:
            raise ValueError("El nuevo título no puede estar vacío.")
        evento = {
            "fecha": datetime.now(),
            "campo": "titulo",
            "anterior": self.__titulo,
            "nuevo": nuevo_titulo
        }
        self.__titulo = nuevo_titulo
        self.__historial_eventos.append(evento)

    def actualizar_anio(self, nuevo_anio):
        if nuevo_anio < 1450:
            raise ValueError("El año debe ser igual o mayor a 1450.")
        evento = {
            "fecha": datetime.now(),
            "campo": "anio",
            "anterior": self.__anio,
            "nuevo": nuevo_anio
        }
        self.__anio = nuevo_anio
        self.__historial_eventos.append(evento)
from datetime import datetime
from clases.actividad import Actividad

class Carrera(Actividad):
    def __init__(self, id_actividad, nombre, duracion_min):
        super().__init__(id_actividad, nombre, duracion_min)
        self.__distancia_km = None
        self.__eventos_registro = []

    @property
    def distancia_km(self):
        return self.__distancia_km

    @property
    def eventos_registro(self):
        return self.__eventos_registro.copy()

    def registrar_distancia(self, nueva_distancia):
        if nueva_distancia <= 0:
            raise ValueError("La distancia debe ser mayor a 0.")
        self.__distancia_km = nueva_distancia
        evento = {
            "fecha": datetime.now(),
            "distancia": nueva_distancia,
            "duracion": self.duracion_min
        }
        self.__eventos_registro.append(evento)

    def calcular_ritmo(self):
        if self.__distancia_km is None or self.__distancia_km <= 0:
            raise Exception("Debe registrar una distancia válida antes de calcular el ritmo.")
        ritmo = self.duracion_min / self.__distancia_km
        return round(ritmo, 2)  # minutos por km
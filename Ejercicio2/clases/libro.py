from datetime import datetime
from clases.publicacion import Publicacion

class Libro(Publicacion):
    def __init__(self, id_publicacion, titulo, anio, paginas_totales):
        super().__init__(id_publicacion, titulo, anio)
        if paginas_totales <= 0:
            raise ValueError("El número de páginas debe ser mayor a 0.")
        
        self.__paginas_totales = paginas_totales
        self.__paginas_leidas = 0
        self.__eventos_lectura = []

    @property
    def paginas_totales(self):
        return self.__paginas_totales

    @property
    def paginas_leidas(self):
        return self.__paginas_leidas

    @property
    def eventos_lectura(self):
        return self.__eventos_lectura.copy()

    def leer(self, paginas):
        if paginas <= 0:
            raise ValueError("No se pueden leer páginas negativas o cero.")
        if self.__paginas_leidas + paginas > self.__paginas_totales:
            raise ValueError("No se pueden leer más páginas que las disponibles.")
        
        self.__paginas_leidas += paginas
        evento = {
            "fecha": datetime.now(),
            "paginas_leidas": paginas,
            "acumulado": self.__paginas_leidas
        }
        self.__eventos_lectura.append(evento)

    def consultar_progreso(self):
        progreso = (self.__paginas_leidas / self.__paginas_totales) * 100
        return round(progreso, 2)
from datetime import datetime

class CuerpoCeleste:
    def __init__(self, id_celeste, nombre, masa_kg):
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        if masa_kg <= 0:
            raise ValueError("La masa debe ser mayor a 0.")
        
        self.id_celeste = id_celeste
        self.__nombre = nombre
        self.__masa_kg = masa_kg
        self.__historial_eventos = []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def masa_kg(self):
        return self.__masa_kg

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

    def actualizar_masa(self, nueva_masa):
        if nueva_masa <= 0:
            raise ValueError("La masa debe ser mayor a 0.")
        evento = {
            "fecha": datetime.now(),
            "campo": "masa_kg",
            "anterior": self.__masa_kg,
            "nuevo": nueva_masa
        }
        self.__masa_kg = nueva_masa
        self.__historial_eventos.append(evento)

    def consultar_ficha(self):
        return {
            "id": self.id_celeste,
            "nombre": self.__nombre,
            "masa_kg": self.__masa_kg,
            "últimos_eventos": self.__historial_eventos[-3:]
        }
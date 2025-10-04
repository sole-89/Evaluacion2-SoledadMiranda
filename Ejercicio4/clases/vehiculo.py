from datetime import datetime

class Vehiculo:
    def __init__(self, id_vehiculo, patente, peso_kg):
        if not patente:
            raise ValueError("La patente no puede estar vacía.")
        if peso_kg <= 0:
            raise ValueError("El peso debe ser mayor a 0.")
        
        self.id_vehiculo = id_vehiculo
        self.patente = patente
        self.__peso_kg = peso_kg
        self.estado = "habilitado"
        self.__historial_eventos = []

    @property
    def peso_kg(self):
        return self.__peso_kg

    @property
    def historial_eventos(self):
        return self.__historial_eventos.copy()

    def actualizar_peso(self, nuevo_peso_kg, usuario="sistema"):
        if self.estado != "habilitado":
            raise Exception("No se puede actualizar peso si el vehículo está inhabilitado.")
        if nuevo_peso_kg <= 0:
            raise ValueError("El peso debe ser mayor a 0.")
        evento = {
            "fecha": datetime.now(),
            "usuario": usuario,
            "tipo_evento": "actualizar_peso",
            "detalle": f"{self.__peso_kg} → {nuevo_peso_kg}"
        }
        self.__peso_kg = nuevo_peso_kg
        self.__historial_eventos.append(evento)

    def habilitar(self, motivo, usuario="sistema"):
        self.estado = "habilitado"
        self.__historial_eventos.append({
            "fecha": datetime.now(),
            "usuario": usuario,
            "tipo_evento": "habilitar",
            "detalle": motivo
        })

    def inhabilitar(self, motivo, usuario="sistema"):
        self.estado = "inhabilitado"
        self.__historial_eventos.append({
            "fecha": datetime.now(),
            "usuario": usuario,
            "tipo_evento": "inhabilitar",
            "detalle": motivo
        })

    def consultar_ficha(self):
        return {
            "id": self.id_vehiculo,
            "patente": self.patente,
            "peso_kg": self.__peso_kg,
            "estado": self.estado,
            "últimos_eventos": self.__historial_eventos[-3:]
        }

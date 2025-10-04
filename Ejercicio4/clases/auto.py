from datetime import datetime
from clases.vehiculo import Vehiculo

class Auto(Vehiculo):
    def __init__(self, id_vehiculo, patente, peso_kg, asientos_totales, sistema_retencion_infantil="no"):
        super().__init__(id_vehiculo, patente, peso_kg)
        if asientos_totales < 1:
            raise ValueError("Debe tener al menos un asiento.")
        
        self.__asientos_totales = asientos_totales
        self.__ocupantes_actuales = 0
        self.sistema_retencion_infantil = sistema_retencion_infantil
        self.__eventos_ocupacion = []

    @property
    def asientos_totales(self):
        return self.__asientos_totales

    @property
    def ocupantes_actuales(self):
        return self.__ocupantes_actuales

    @property
    def eventos_ocupacion(self):
        return self.__eventos_ocupacion.copy()

    def subir_personas(self, n):
        if self.estado != "habilitado":
            raise Exception("El vehículo está inhabilitado.")
        if n < 1 or self.__ocupantes_actuales + n > self.__asientos_totales:
            raise ValueError("No se pueden subir esa cantidad de personas.")
        ocupantes_antes = self.__ocupantes_actuales
        self.__ocupantes_actuales += n
        self.__eventos_ocupacion.append({
            "fecha": datetime.now(),
            "accion": "subir",
            "cantidad": n,
            "ocupantes_antes": ocupantes_antes,
            "ocupantes_despues": self.__ocupantes_actuales
        })

    def bajar_personas(self, n):
        if self.estado != "habilitado":
            raise Exception("El vehículo está inhabilitado.")
        if n < 1 or self.__ocupantes_actuales - n < 0:
            raise ValueError("No se pueden bajar esa cantidad de personas.")
        ocupantes_antes = self.__ocupantes_actuales
        self.__ocupantes_actuales -= n
        self.__eventos_ocupacion.append({
            "fecha": datetime.now(),
            "accion": "bajar",
            "cantidad": n,
            "ocupantes_antes": ocupantes_antes,
            "ocupantes_despues": self.__ocupantes_actuales
        })

    def reconfigurar_asientos(self, nuevo_total, motivo):
        if nuevo_total < 1 or nuevo_total < self.__ocupantes_actuales:
            raise ValueError("No se puede reducir los asientos por debajo de los ocupantes actuales.")
        evento = {
            "fecha": datetime.now(),
            "tipo_evento": "reconfigurar_asientos",
            "detalle": f"{self.__asientos_totales} → {nuevo_total} | Motivo: {motivo}"
        }
        self.__asientos_totales = nuevo_total
        self.historial_eventos.append(evento)

    def vaciar_auto(self, motivo):
        ocupantes_antes = self.__ocupantes_actuales
        self.__ocupantes_actuales = 0
        self.__eventos_ocupacion.append({
            "fecha": datetime.now(),
            "accion": "vaciar",
            "motivo": motivo,
            "ocupantes_antes": ocupantes_antes,
            "ocupantes_despues": 0
        })

    def consultar_ocupacion(self):
        libres = self.__asientos_totales - self.__ocupantes_actuales
        tasa = round((self.__ocupantes_actuales / self.__asientos_totales) * 100, 2)
        return {
            "ocupantes": self.__ocupantes_actuales,
            "asientos_libres": libres,
            "tasa_ocupacion": f"{tasa}%"
        }
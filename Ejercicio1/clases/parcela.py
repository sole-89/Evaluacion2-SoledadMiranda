from datetime import datetime

class Parcela:
    def __init__(self, id_parcela, superficie_ha, cultivo_actual):
        if superficie_ha <= 0:
            raise ValueError("La superficie debe ser mayor a 0.")
        if not cultivo_actual:
            raise ValueError("El cultivo no puede estar vacío.")
        
        self.id_parcela = id_parcela
        self.__superficie_ha = round(superficie_ha, 2)
        self.__cultivo_actual = cultivo_actual
        self.estado = "activa"
        self.__historial_eventos = []

    @property
    def superficie_ha(self):
        return self.__superficie_ha

    @property
    def cultivo_actual(self):
        return self.__cultivo_actual

    @property
    def historial_eventos(self):
        return self.__historial_eventos.copy()

    def actualizar_cultivo(self, nuevo_cultivo):
        if self.estado != "activa":
            raise Exception("No se puede actualizar cultivo si la parcela está inactiva.")
        if not nuevo_cultivo:
            raise ValueError("El nuevo cultivo no puede estar vacío.")
        evento = {
            "fecha": datetime.now(),
            "tipo": "actualizar_cultivo",
            "detalle": f"{self.__cultivo_actual} → {nuevo_cultivo}"
        }
        self.__cultivo_actual = nuevo_cultivo
        self.__historial_eventos.append(evento)

    def activar(self, motivo):
        self.estado = "activa"
        self.__historial_eventos.append({
            "fecha": datetime.now(),
            "tipo": "activar",
            "detalle": motivo
        })

    def desactivar(self, motivo):
        self.estado = "inactiva"
        self.__historial_eventos.append({
            "fecha": datetime.now(),
            "tipo": "desactivar",
            "detalle": motivo
        })

    def rectificar_superficie(self, nueva_superficie, motivo):
        if nueva_superficie <= 0:
            raise ValueError("La nueva superficie debe ser mayor a 0.")
        evento = {
            "fecha": datetime.now(),
            "tipo": "rectificar_superficie",
            "detalle": f"{self.__superficie_ha} → {nueva_superficie} | Motivo: {motivo}"
        }
        self.__superficie_ha = round(nueva_superficie, 2)
        self.__historial_eventos.append(evento)
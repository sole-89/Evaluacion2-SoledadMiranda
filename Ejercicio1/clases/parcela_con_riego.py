from datetime import datetime
from clases.parcela import Parcela

class ParcelaConRiego(Parcela):
    def __init__(self, id_parcela, superficie_ha, cultivo_actual):
        super().__init__(id_parcela, superficie_ha, cultivo_actual)
        self.__litros_disponibles = 0
        self.tasa_riego_l_ha = 1500
        self.umbral_min_litros = 2000
        self.estado_riego = "habilitado" if self.estado == "activa" else "inhabilitado"
        self.__eventos_riego = []

    @property
    def litros_disponibles(self):
        return self.__litros_disponibles

    @property
    def eventos_riego(self):
        return self.__eventos_riego.copy()

    def configurar_tasa(self, l_ha):
        if l_ha <= 0:
            raise ValueError("La tasa debe ser mayor a 0.")
        self.tasa_riego_l_ha = l_ha

    def configurar_umbral(self, litros):
        if litros < 0:
            raise ValueError("El umbral debe ser ≥ 0.")
        self.umbral_min_litros = litros

    def habilitar_riego(self):
        self.estado_riego = "habilitado"

    def inhabilitar_riego(self):
        self.estado_riego = "inhabilitado"

    def cargar_agua(self, litros):
        if litros <= 0:
            raise ValueError("Debe cargar más de 0 litros.")
        saldo_antes = self.__litros_disponibles
        self.__litros_disponibles += litros
        self.__eventos_riego.append({
            "fecha": datetime.now(),
            "tipo": "carga",
            "litros": litros,
            "saldo_antes": saldo_antes,
            "saldo_despues": self.__litros_disponibles
        })

    def regar_automatico(self, modo):
        if self.estado != "activa":
            raise Exception("La parcela está inactiva.")
        if self.estado_riego != "habilitado":
            raise Exception("El riego está inhabilitado.")
        if self.tasa_riego_l_ha <= 0:
            raise Exception("La tasa de riego no es válida.")

        demanda = self.superficie_ha * self.tasa_riego_l_ha
        saldo_antes = self.__litros_disponibles

        if modo == "estricto":
            if self.__litros_disponibles - demanda >= self.umbral_min_litros:
                self.__litros_disponibles -= demanda
                litros_aplicados = demanda
            else:
                raise Exception("No hay suficiente agua para riego estricto.")
        elif modo == "parcial":
            max_aplicable = self.__litros_disponibles - self.umbral_min_litros
            litros_aplicados = max(0, min(demanda, max_aplicable))
            self.__litros_disponibles -= litros_aplicados
        else:
            raise ValueError("Modo inválido. Usa 'estricto' o 'parcial'.")

        self.__eventos_riego.append({
            "fecha": datetime.now(),
            "modo": modo,
            "litros_solicitados": demanda,
            "litros_aplicados": litros_aplicados,
            "saldo_antes": saldo_antes,
            "saldo_despues": self.__litros_disponibles
        })
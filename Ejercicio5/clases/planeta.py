import math
from clases.cuerpo_celeste import CuerpoCeleste

class Planeta(CuerpoCeleste):
    def __init__(self, id_celeste, nombre, masa_kg, radio_km, distancia_sol_km):
        super().__init__(id_celeste, nombre, masa_kg)
        if radio_km <= 0 or distancia_sol_km <= 0:
            raise ValueError("El radio y la distancia al sol deben ser mayores a 0.")
        
        self.__radio_km = radio_km
        self.__distancia_sol_km = distancia_sol_km

    @property
    def radio_km(self):
        return self.__radio_km

    @property
    def distancia_sol_km(self):
        return self.__distancia_sol_km

    def actualizar_radio(self, nuevo_radio):
        if nuevo_radio <= 0:
            raise ValueError("El radio debe ser mayor a 0.")
        self.__radio_km = nuevo_radio

    def actualizar_distancia_sol(self, nueva_distancia):
        if nueva_distancia <= 0:
            raise ValueError("La distancia al sol debe ser mayor a 0.")
        self.__distancia_sol_km = nueva_distancia

    def calcular_densidad(self):
        volumen = (4/3) * math.pi * (self.__radio_km ** 3)
        densidad = self.masa_kg / volumen
        return round(densidad, 2)

    def comparar_distancia(self, otro_planeta):
        if not isinstance(otro_planeta, Planeta):
            raise TypeError("Solo se puede comparar con otro planeta.")
        if self.__distancia_sol_km < otro_planeta.distancia_sol_km:
            return f"{self.nombre} está más cerca del sol que {otro_planeta.nombre}."
        elif self.__distancia_sol_km > otro_planeta.distancia_sol_km:
            return f"{otro_planeta.nombre} está más cerca del sol que {self.nombre}."
        else:
            return "Ambos planetas están a la misma distancia del sol."
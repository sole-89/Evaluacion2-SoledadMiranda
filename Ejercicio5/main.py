from clases.planeta import Planeta
from clases.cuerpo_celeste import CuerpoCeleste

# Crear cuerpo celeste
estrella = CuerpoCeleste(id_celeste=1, nombre="Estrella X", masa_kg=2e30)

# Crear planetas
tierra = Planeta(id_celeste=2, nombre="Tierra", masa_kg=5.97e24, radio_km=6371, distancia_sol_km=149600000)
marte = Planeta(id_celeste=3, nombre="Marte", masa_kg=6.42e23, radio_km=3389, distancia_sol_km=227900000)

# Calcular densidad
print("Densidad de Tierra:", tierra.calcular_densidad(), "kg/km³")

# Comparar distancias
print(tierra.comparar_distancia(marte))

# Intentar crear planeta con radio inválido
try:
    Planeta(id_celeste=4, nombre="Error", masa_kg=1e24, radio_km=0, distancia_sol_km=100000000)
except ValueError as e:
    print("Error esperado:", e)

# Actualizar masa
tierra.actualizar_masa(6e24)

# Mostrar historial
print("\nHistorial de eventos de Tierra:")
for evento in tierra.historial_eventos:
    print(evento)
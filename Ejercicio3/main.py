from clases.carrera import Carrera
from clases.actividad import Actividad

# Crear actividad válida
actividad = Actividad(id_actividad=1, nombre="Yoga", duracion_min=60)

# Intentar crear actividad con duración inválida
try:
    Actividad(id_actividad=2, nombre="Error", duracion_min=0)
except ValueError as e:
    print("Error esperado:", e)

# Crear carrera
carrera = Carrera(id_actividad=3, nombre="10K", duracion_min=50)
carrera.registrar_distancia(10)

# Calcular ritmo
print("Ritmo:", carrera.calcular_ritmo(), "min/km")

# Intentar registrar distancia inválida
try:
    carrera.registrar_distancia(-3)
except ValueError as e:
    print("Error esperado:", e)

# Actualizar duración
carrera.actualizar_duracion(55)

# Mostrar historial
print("\nHistorial de actividad:")
for evento in carrera.historial_eventos:
    print(evento)

print("\nEventos de carrera:")
for evento in carrera.eventos_registro:
    print(evento)
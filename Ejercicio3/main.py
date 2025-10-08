from clases.carrera import Carrera
from clases.actividad import Actividad

print("🏋️‍♀️ === GESTIÓN DE ACTIVIDADES Y CARRERAS ===\n")

# Crear actividad válida
print("📘 Creando actividad válida...")
actividad = Actividad(id_actividad=1, nombre="Yoga", duracion_min=60)
print("✅ Actividad creada:", actividad.nombre, "-", actividad.duracion_min, "min\n")

# Intentar crear actividad con duración inválida
print("⚠️ Probando creación con duración inválida...")
try:
    Actividad(id_actividad=2, nombre="Error", duracion_min=0)
except ValueError as e:
    print("🚫 Error esperado:", e, "\n")

# Crear carrera
print("🏃‍♀️ Creando carrera de prueba...")
carrera = Carrera(id_actividad=3, nombre="10K", duracion_min=50)
carrera.registrar_distancia(10)
print("✅ Carrera creada con distancia:", carrera.distancia_km, "km")

# Calcular ritmo
print("⏱️ Calculando ritmo...")
print("📊 Ritmo promedio:", carrera.calcular_ritmo(), "min/km\n")

# Intentar registrar distancia inválida
print("⚠️ Probando registro de distancia inválida...")
try:
    carrera.registrar_distancia(-3)
except ValueError as e:
    print("🚫 Error esperado:", e, "\n")

# Actualizar duración
print("🕒 Actualizando duración de la carrera...")
carrera.actualizar_duracion(55)
print("🔁 Duración actualizada correctamente.\n")

# Mostrar historial de eventos
print("🧾 === HISTORIAL DE ACTIVIDAD ===")
for evento in carrera.historial_eventos:
    print("🗓️", evento)

print("\n🏁 === EVENTOS DE CARRERA ===")
for evento in carrera.eventos_registro:
    print("📍", evento)

print("\n✅ Programa finalizado correctamente 🚀")

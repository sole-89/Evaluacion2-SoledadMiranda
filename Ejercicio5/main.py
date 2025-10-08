from clases.planeta import Planeta
from clases.cuerpo_celeste import CuerpoCeleste

print("🌟 === SISTEMA DE CUERPOS CELESTES ===\n")

# Crear cuerpo celeste
print("☀️ Creando estrella...")
estrella = CuerpoCeleste(id_celeste=1, nombre="Estrella X", masa_kg=2e30)
print(f"✅ Cuerpo celeste creado: {estrella.nombre} - Masa: {estrella.masa_kg:.2e} kg\n")

# Crear planetas
print("🪐 Creando planetas...")
tierra = Planeta(id_celeste=2, nombre="Tierra", masa_kg=5.97e24, radio_km=6371, distancia_sol_km=149600000)
marte = Planeta(id_celeste=3, nombre="Marte", masa_kg=6.42e23, radio_km=3389, distancia_sol_km=227900000)
print(f"✅ Planeta creado: {tierra.nombre}, {marte.nombre}\n")

# Calcular densidad
print("🧪 Calculando densidad...")
print(f"📊 Densidad de {tierra.nombre}: {tierra.calcular_densidad():.2e} kg/km³\n")

# Comparar distancias al sol
print("📏 Comparando distancias al sol entre planetas...")
print(tierra.comparar_distancia(marte), "\n")

# Intentar crear planeta con radio inválido
print("⚠️ Probando creación de planeta con radio inválido...")
try:
    Planeta(id_celeste=4, nombre="Error", masa_kg=1e24, radio_km=0, distancia_sol_km=100000000)
except ValueError as e:
    print("🚫 Error esperado:", e, "\n")

# Actualizar masa
print("⚙️ Actualizando masa de la Tierra...")
tierra.actualizar_masa(6e24)
print(f"🔁 Masa de {tierra.nombre} actualizada: {tierra.masa_kg:.2e} kg\n")

# Mostrar historial de eventos
print("📋 === HISTORIAL DE EVENTOS DE TIERRA ===")
for evento in tierra.historial_eventos:
    fecha = evento['fecha'].strftime("%Y-%m-%d %H:%M:%S")
    tipo = evento.get('tipo', '')
    detalle = evento.get('detalle', '')
    print(f"🗓️ {fecha} | {tipo:<20} | {detalle}")

print("\n✅ Programa finalizado correctamente 🌌")

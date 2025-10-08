from clases.auto import Auto

print("🚗 === GESTIÓN DE VEHÍCULOS ===\n")

# Crear vehículo
print("🔧 Creando vehículo...")
auto = Auto(id_vehiculo=1, patente="ABCD12", peso_kg=1450, asientos_totales=5)
print(f"✅ Vehículo creado: {auto.patente} - Peso: {auto.peso_kg} kg - Asientos: {auto.asientos_totales}\n")

# Actualizar peso
print("⚙️ Actualizando peso del vehículo...")
auto.actualizar_peso(1500)
print("✅ Peso actualizado correctamente.")
try:
    auto.actualizar_peso(0)
except ValueError as e:
    print("🚫 Error esperado:", e)
print()

# Inhabilitar y probar restricciones
print("🚧 Inhabilitando vehículo por mantención...")
auto.inhabilitar("mantención")
try:
    auto.actualizar_peso(1600)
except Exception as e:
    print("🚫 Error esperado:", e)
auto.habilitar("mantención finalizada")

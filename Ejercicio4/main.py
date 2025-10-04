from clases.auto import Auto

# Crear vehículo
auto = Auto(id_vehiculo=1, patente="ABCD12", peso_kg=1450, asientos_totales=5)

# Actualizar peso
auto.actualizar_peso(1500)
try:
    auto.actualizar_peso(0)
except ValueError as e:
    print("Error esperado:", e)

# Inhabilitar y probar restricciones
auto.inhabilitar("mantención")
try:
    auto.actualizar_peso(1600)
except Exception as e:
    print("Error esperado:", e)
auto.habilitar("mantención finalizada")

# Subir personas
auto.subir_personas(3)
try:
    auto.subir_personas(3)
except ValueError as e:
    print("Error esperado:", e)

# Bajar personas
auto.bajar_personas(2)
try:
    auto.bajar_personas(5)
except ValueError as e:
    print("Error esperado:", e)

# Reconfigurar asientos
auto.reconfigurar_asientos(2, "reparación")
try:
    auto.reconfigurar_asientos(0, "error")
except ValueError as e:
    print("Error esperado:", e)

# Vaciar auto
auto.vaciar_auto("fin de turno")

# Inhabilitar y probar restricción de subida
auto.inhabilitar("prueba")
try:
    auto.subir_personas(1)
except Exception as e:
    print("Error esperado:", e)

# Mostrar auditoría
print("\nHistorial de eventos:")
for evento in auto.historial_eventos:
    print(evento)

print("\nEventos de ocupación:")
for evento in auto.eventos_ocupacion:
    print(evento)

print("\nOcupación actual:")
print(auto.consultar_ocupacion())
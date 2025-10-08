from clases.parcela_con_riego import ParcelaConRiego

# Crear parcela
parcela = ParcelaConRiego(id_parcela=1, superficie_ha=10.50, cultivo_actual="Trigo")

# Actualizar cultivo
parcela.actualizar_cultivo("Maíz")

# Configurar riego
parcela.configurar_tasa(1500)
parcela.configurar_umbral(2000)
parcela.cargar_agua(20000)

# Regar en modo estricto
parcela.regar_automatico("estricto")

# Desactivar parcela
parcela.desactivar("Fin de temporada")

# Intentar regar estando inactiva
try:
    parcela.regar_automatico("estricto")
except Exception as e:
    print("Error esperado:", e)

# Regar en modo parcial con saldo limitado
parcela.activar("Inicio nueva temporada")
parcela.cargar_agua(3000)
parcela.regar_automatico("parcial")

# === Sección mejorada de visualización ===
print("\n=== HISTORIAL DE EVENTOS ===")
for evento in parcela.historial_eventos:
    fecha = evento['fecha'].strftime("%Y-%m-%d %H:%M:%S")
    tipo = evento.get('tipo', '')
    detalle = evento.get('detalle', '')
    print(f"{fecha:<20} | {tipo:<20} | {detalle}")

print("\n=== EVENTOS DE RIEGO ===")
for evento in parcela.eventos_riego:
    fecha = evento['fecha'].strftime("%Y-%m-%d %H:%M:%S")
    modo = evento.get('modo', evento.get('tipo', ''))
    litros_solicitados = evento.get('litros_solicitados', '-')
    litros_aplicados = evento.get('litros_aplicados', '-')
    saldo_antes = evento.get('saldo_antes', '-')
    saldo_despues = evento.get('saldo_despues', '-')
    print(f"{fecha:<20} | {modo:<10} | Solicitados: {litros_solicitados:<8} | "
          f"Aplicados: {litros_aplicados:<8} | Saldo antes: {saldo_antes:<8} | "
          f"Saldo después: {saldo_despues:<8}")

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

# Mostrar historial
print("Historial de eventos:")
for evento in parcela.historial_eventos:
    print(evento)

print("\nEventos de riego:")
for evento in parcela.eventos_riego:
    print(evento)
from clases.libro import Libro
from clases.publicacion import Publicacion

print("\n📚 === INICIO DE PRUEBAS: CLASES LIBRO Y PUBLICACIÓN ===")

# === CREAR PUBLICACIÓN VÁLIDA ===
publicacion = Publicacion(id_publicacion=1, titulo="Don Quijote", anio=1605)
print("✅ Publicación creada correctamente:", publicacion.titulo)

# === INTENTAR CREAR PUBLICACIÓN CON AÑO INVÁLIDO ===
try:
    Publicacion(id_publicacion=2, titulo="Antiguo", anio=1400)
except ValueError as e:
    print("⚠️  Error esperado:", e)

# === CREAR LIBRO ===
libro = Libro(id_publicacion=3, titulo="Cien años de soledad", anio=1967, paginas_totales=500)
print("📖 Libro creado:", libro.titulo)

# === LEER PÁGINAS VÁLIDAS ===
libro.leer(120)
print(f"📘 Progreso actual: {libro.consultar_progreso()} %")

# === INTENTAR LEER DEMASIADO ===
try:
    libro.leer(400)
except ValueError as e:
    print("⚠️  Error esperado:", e)

# === ACTUALIZAR AÑO ===
libro.actualizar_anio(1980)
print("🕒 Año actualizado correctamente a 1980")

# === MOSTRAR HISTORIAL DE EVENTOS ===
print("\n" + "=" * 70)
print("📋 HISTORIAL DE PUBLICACIÓN")
print("=" * 70)
print(f"{'Fecha':<20} | {'Tipo':<20} | {'Detalle'}")
print("-" * 70)
for evento in libro.historial_eventos:
    fecha = evento['fecha'].strftime("%Y-%m-%d %H:%M:%S")
    tipo = evento.get('tipo', '')
    detalle = evento.get('detalle', '')
    print(f"{fecha:<20} | {tipo:<20} | {detalle}")

# === MOSTRAR EVENTOS DE LECTURA ===
print("\n" + "=" * 100)
print("📖 EVENTOS DE LECTURA")
print("=" * 100)
print(f"{'Fecha':<20} | {'Páginas Leídas':<15} | {'Progreso (%)':<15} | {'Páginas Restantes':<20}")
print("-" * 100)
for evento in libro.eventos_lectura:
    fecha = evento['fecha'].strftime("%Y-%m-%d %H:%M:%S")
    paginas = evento.get('paginas_leidas', '-')
    progreso = evento.get('progreso', '-')
    restantes = evento.get('paginas_restantes', '-')
    print(f"{fecha:<20} | {paginas:<15} | {progreso:<15} | {restantes:<20}")

print("\n✅ Prueba completada exitosamente.")

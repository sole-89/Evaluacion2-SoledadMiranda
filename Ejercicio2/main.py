from clases.libro import Libro
from clases.publicacion import Publicacion

# Crear publicación válida
publicacion = Publicacion(id_publicacion=1, titulo="Don Quijote", anio=1605)

# Intentar crear publicación con año inválido
try:
    Publicacion(id_publicacion=2, titulo="Antiguo", anio=1400)
except ValueError as e:
    print("Error esperado:", e)

# Crear libro
libro = Libro(id_publicacion=3, titulo="Cien años de soledad", anio=1967, paginas_totales=500)

# Leer páginas válidas
libro.leer(120)
print("Progreso:", libro.consultar_progreso(), "%")

# Intentar leer más páginas de las que quedan
try:
    libro.leer(400)
except ValueError as e:
    print("Error esperado:", e)

# Actualizar año
libro.actualizar_anio(1980)

# Mostrar historial de eventos
print("\nHistorial de publicación:")
for evento in libro.historial_eventos:
    print(evento)

print("\nEventos de lectura:")
for evento in libro.eventos_lectura:
    print(evento)

import random

# Listas con los nombres de las canciones y sus respectivas duraciones
nombres_canciones = ["Bohemian Rhapsody", "Stairway to Heaven", "Hotel California", "Imagine", "Smells Like Teen Spirit"]
duraciones_canciones = [5.55, 8.02, 6.30, 3.03, 5.01]

# Paso 1: Crear un diccionario con las canciones como claves y sus duraciones como valores
canciones_con_duracion = dict(zip(nombres_canciones, duraciones_canciones))

print("Lista completa de canciones con sus duraciones:", canciones_con_duracion)

# Paso 2: Seleccionar las 3 canciones más largas
# Ordenamos el diccionario por la duración de mayor a menor y seleccionamos las tres primeras
canciones_mas_largas = sorted(canciones_con_duracion.items(), key=lambda i: i[1], reverse=True)
top_3_canciones = dict(canciones_mas_largas[:3])

print("\nLas 3 canciones más largas son:", top_3_canciones)

# Paso 3: Selección aleatoria de un par de canciones
# Seleccionamos aleatoriamente dos canciones del diccionario original
canciones_aleatorias = random.sample(list(canciones_con_duracion.items()), 2)
seleccion_random = dict(canciones_aleatorias)

print("\nSelección aleatoria de canciones:", seleccion_random)
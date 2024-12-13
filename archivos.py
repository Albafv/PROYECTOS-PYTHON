# Intentamos abrir el archivo "mi_archivo.txt" en modo lectura ('r')
try:
    # Si el archivo no existe, se lanza un error
    with open("mi_archivo.txt", 'r') as file:
        print("El archivo ya existe.")
except FileNotFoundError:
    # Si no existe, lo creamos y escribimos 5 líneas
    print("El archivo no existe. Creando 'mi_archivo.txt'.")
    with open("mi_archivo.txt", 'w') as file:
        file.write("Línea 1: Esta es la línea 1.\n")
        file.write("Línea 2: Esta es la línea 2.\n")
        file.write("Línea 3: Esta es la línea 3.\n")
        file.write("Línea 4: Esta es la línea 4.\n")
        file.write("Línea 5: Esta es la línea 5.\n")

# Ahora leemos y mostramos el contenido del archivo
with open("mi_archivo.txt", 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break  # Si ya no hay más líneas, salimos
        print(line.strip())  # Mostramos la línea sin saltos de línea
        print(f"Posición del cursor: {file.tell()}")  # Mostramos la posición actual del cursor

# Abrimos el archivo para sobrescribirlo con una nueva línea
with open("mi_archivo.txt", 'w') as file:
    file.write("nueva línea escrita al sobrescribir el archivo.\n")

# Abrimos el archivo en modo anexado ('a+') para añadir una línea
with open("mi_archivo.txt", 'a+') as file:
    file.write("línea añadida al final del archivo.\n")
    # Volvemos al principio con seek(0) para leer todo el contenido
    file.seek(0)
    print("\nContenido del archivo después de añadir una línea:")
    print(file.read())

# Ahora probamos con el modo 'a' (solo añadir) en vez de 'a+'
try:
    with open("mi_archivo.txt", 'a') as file:
        file.write("Esta es una línea añadida en modo 'a'.\n")
        file.seek(0)  # Esto no funciona bien en 'a'
        print("\nContenido del archivo después de añadir una línea en modo 'a':")
        print(file.read())
except Exception as e:
    print(f"Error al intentar abrir el archivo en modo 'a': {e}")

# Los archivos se cierran automáticamente al salir del bloque 'with'



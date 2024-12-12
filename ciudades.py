import math
import statistics
personas = [
    {"nombre": "Ana", "edad": 25, "ciudad": "Madrid", "salario": 25000},
    {"nombre": "Juan", "edad": 30, "ciudad": "Sevilla", "salario": 30000},
    {"nombre": "María", "edad": 22, "ciudad": "Madrid", "salario": 22000},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona", "salario": 35000},
]

# Función para obtener el salario de una persona
def get_salary(persona):
    return persona['salario']

# Función para listar personas de forma legible
def list_personas_legible(personas):
    for persona in personas:
        print(f"Nombre: {persona['nombre']}, Ciudad: {persona['ciudad']}, Salario: {persona['salario']}, Edad: {persona['edad']}")

# Mostrar primeras 5 personas
print("Primeras 5 personas:")
list_personas_legible(personas[:5])

# Calcular y mostrar el salario medio
salarios = [get_salary(persona) for persona in personas]
salario_medio = sum(salarios) / len(salarios)
print(f"\nSalario medio: {round(salario_medio)}")

# Calcular y mostrar la mediana del salario
mediana_salario = statistics.median(salarios)
print(f"Mediana del salario: {int(mediana_salario)}")

# Combinar ciudades y salarios en tuplas
ciudades = [persona['ciudad'] for persona in personas]
ciudades_salarios = list(zip(ciudades, salarios))




#EJERCICIO CONT.
# Crear Diccionario de Salarios por Ciudad
# Mapeamos cada ciudad con la lista de salarios correspondientes utilizando un diccionario
salarios_por_ciudad = {}
for persona in personas:
    if persona['ciudad'] not in salarios_por_ciudad:
        salarios_por_ciudad[persona['ciudad']] = []
    salarios_por_ciudad[persona['ciudad']].append(persona['salario'])

# Mostrar salarios de la ciudad de Madrid
print("\nSalarios de la ciudad de Madrid:")
print(salarios_por_ciudad.get('Madrid', 'No hay salarios registrados para Madrid'))

# Calcular la Media de Salarios por Ciudad con Comprensión de Diccionario
# Usamos una comprensión de diccionario para calcular la media de salarios por ciudad
media_salarios_por_ciudad = {ciudad: sum(salarios) / len(salarios) for ciudad, salarios in salarios_por_ciudad.items()}

# Mostrar la media de salarios por ciudad
print("\nMedia de salarios por ciudad:")
for ciudad, media in media_salarios_por_ciudad.items():
    print(f"{ciudad}: {round(media)}")

# Calcular el salario medio general para filtrar las personas
salario_medio = sum(salarios) / len(salarios)

# Filtrar personas con salario por encima de la media
personas_salario_arriba_media = list(filter(lambda persona: persona['salario'] > salario_medio, personas))
print("\nPersonas con salario por encima de la media:")
list_personas_legible(personas_salario_arriba_media)

# Filtrar personas con salario por encima de la media de su ciudad
personas_salario_arriba_media_ciudad = list(filter(lambda persona: persona['salario'] > media_salarios_por_ciudad[persona['ciudad']], personas))
print("\nPersonas con salario por encima de la media de su ciudad:")
list_personas_legible(personas_salario_arriba_media_ciudad)

# Encontrar la persona más joven con el salario más alto
persona_mas_joven_salario_alto = min(personas, key=lambda persona: (persona['salario'], -persona['edad']))
print("\nLa persona más joven con el salario más alto:")
print(f"Nombre: {persona_mas_joven_salario_alto['nombre']}, Ciudad: {persona_mas_joven_salario_alto['ciudad']}, Salario: {persona_mas_joven_salario_alto['salario']}, Edad: {persona_mas_joven_salario_alto['edad']}")

# Obtener el top 5 de las personas más jóvenes con salario más alto
top_5_personas_jovenes_salario_alto = sorted(personas, key=lambda persona: (-persona['salario'], persona['edad']))[:5]
print("\nTop 5 de las personas más jóvenes con el salario más alto:")
list_personas_legible(top_5_personas_jovenes_salario_alto)
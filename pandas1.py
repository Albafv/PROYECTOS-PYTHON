import pandas as pd

# 1. Crear una Serie de Pandas usando una lista de números.
numeros = [10, 20, 30, 40, 50]
serie = pd.Series(numeros)

# 2. Imprimir la Serie para ver los valores iniciales.
print("Serie original:")
print(serie)


# 3. Añadir un nuevo valor a la Serie.
serie = pd.concat([serie, pd.Series([60])])
print("Serie después de agregar el número 60:")
print(serie)


# 4. Eliminar un elemento específico de la Serie (por su índice).
serie = serie.drop(2)  # Eliminamos el valor en el índice 2 (que es 30).
print("Serie después de quitar el valor en el índice 2 (30):")
print(serie)


# 5. Realizar operaciones matemáticas básicas (suma, resta, multiplicación y división) en cada elemento de la Serie.
suma = serie + 10
resta = serie - 5
multiplicacion = serie * 2
division = serie / 2

# 6. Mostrar el resultado de cada operación matemática.
print("Resultado de sumar 10 a cada número de la Serie:")
print(suma)


print("Resultado de restar 5 a cada número de la Serie:")
print(resta)


print("Resultado de multiplicar cada número de la Serie por 2:")
print(multiplicacion)


print("Resultado de dividir cada número de la Serie por 2:")
print(division)
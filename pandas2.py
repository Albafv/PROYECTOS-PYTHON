import pandas as pd

# 1. Crear dos Series a partir de listas de datos.
temperaturas = [18, 20, 22, 21, 23, 24, 25]
precipitacion = [5, 12, 7, 0, 0, 3, 8]

# Convertimos las listas en Series de Pandas
serie_temperaturas = pd.Series(temperaturas)
serie_precipitacion = pd.Series(precipitacion)

# 2. Realizar operaciones de slicing en ambas Series.
# Tomamos los primeros 5 valores de temperaturas
slice_temperaturas = serie_temperaturas[:5]

# Tomamos los valores de precipitación a partir del tercer día (índice 2)
slice_precipitacion = serie_precipitacion[2:]

# 3. Combinar las Series resultantes del slicing en una nueva Serie.
# Combinamos los valores obtenidos en el slicing
serie_combinada = pd.concat([slice_temperaturas, slice_precipitacion], ignore_index=True)

# 4. Realizar operaciones matemáticas básicas sobre la Serie combinada.
# Sumar 5 a cada valor de la serie combinada
suma_combinada = serie_combinada + 5

# Restar 3 a cada valor de la serie combinada
resta_combinada = serie_combinada - 3

# Multiplicar cada valor de la serie combinada por 2
multiplicacion_combinada = serie_combinada * 2

# Dividir cada valor de la serie combinada por 2
division_combinada = serie_combinada / 2

# Mostrar resultados
print("Serie de temperaturas:", serie_temperaturas)
print("Serie de precipitaciones:", serie_precipitacion)


print("Resultado del slicing de temperaturas (primeros 5 días):", slice_temperaturas)
print("Resultado del slicing de precipitaciones (días desde el 3er día):", slice_precipitacion)


print("Serie combinada (temperaturas + precipitaciones):", serie_combinada)


print("Resultado de sumar 5 a cada valor de la serie combinada:", suma_combinada)
print("Resultado de restar 3 a cada valor de la serie combinada:", resta_combinada)
print("Resultado de multiplicar cada valor de la serie combinada por 2:", multiplicacion_combinada)
print("Resultado de dividir cada valor de la serie combinada por 2:", division_combinada)
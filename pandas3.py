import pandas as pd
URL = "https://drive.google.com/uc?export=download&id=1-zKKm5aEEabJS01n4vZhE8iiacnXYWGg"
df = pd.read_csv(URL)

#PARTE 1
# 1. Mostrar las primeras y últimas 5 filas del DataFrame
print("Primeras 5 filas del DataFrame:")
print(df.head())  # Muestra las primeras 5 filas
print("\nÚltimas 5 filas del DataFrame:")
print(df.tail())  # Muestra las últimas 5 filas

# 2. Obtener información general del DataFrame (número de filas, columnas y tipos de datos)
print("\nInformación general del DataFrame:")
print(df.info())  # Información general (número de filas, columnas, tipos de datos)

# 3. Calcular estadísticas descriptivas básicas para las columnas numéricas
print("\nEstadísticas descriptivas básicas:")
print(df.describe())  # Estadísticas descriptivas (media, mediana, desviación estándar, mínimos y máximos)



#PARTE 2
# 1. Convertir la altura de pulgadas a centímetros (1 pulgada = 2.54 cm)
df['Height_cm'] = df['Height'] * 2.54
print("\nColumna de altura convertida a centímetros:")
print(df[['Height', 'Height_cm']].head())  # Muestra las primeras filas con ambas columnas

# 2. Convertir el peso de libras a kilogramos (1 libra = 0.453592 kg)
df['Weight_kg'] = df['Weight'] * 0.453592
print("\nColumna de peso convertida a kilogramos:")
print(df[['Weight', 'Weight_kg']].head())  # Muestra las primeras filas con ambas columnas

# 3. Manejo de valores faltantes
df.isnull().sum() #dice cuantos valores faltantes hay por categoría
df_nonulos=df.dropna().copy() #elimina los valores faltantes



#PARTE 4
# 1. Calcular los percentiles del peso para cada género
# Supongamos que el DataFrame tiene una columna llamada 'Gender' para el género de cada individuo
percentiles_peso = df_nonulos.groupby('Gender')['Weight'].quantile([0.25, 0.5, 0.75])  # Cuartiles del peso
print("\nPercentiles del peso para cada género:")
print(percentiles_peso)

# 2. Crear una nueva columna con la clasificación según el IMC
# Calcular el IMC: IMC = peso / (altura^2) 
df_nonulos['BMI'] = df_nonulos['Weight'] / (df_nonulos['Height'] / 100) ** 2  # Convertimos la altura a metros dividiendo entre 100

# Clasificar según el IMC
def clasificar_imc(bmi):
    if bmi < 18.5:
        return 'Bajo Peso'
    elif 18.5 <= bmi < 24.9:
        return 'Peso Normal'
    elif 25 <= bmi < 29.9:
        return 'Sobrepeso'
    else:
        return 'Obesidad'

# Aplicar la clasificación del IMC a una nueva columna 'BMI_Category'
df_nonulos['BMI_Category'] = df_nonulos['BMI'].apply(clasificar_imc)

# Mostrar las primeras filas con la nueva columna 'BMI' y 'BMI_Category'
print("\nClasificación de IMC:")
print(df_nonulos[['Height', 'Weight', 'BMI', 'BMI_Category']].head())


# PARTE5
# Guardar el DataFrame con los nuevos resultados en un archivo CSV
df_nonulos.to_csv('resultados_analisis.csv', index=False)

print("\nEl archivo de resultados ha sido guardado como 'resultados_analisis.csv'.")
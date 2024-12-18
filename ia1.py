import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt

# Paso 1: Cargar el archivo CSV desde Google Drive
url = "https://drive.google.com/uc?export=download&id=10JJmUmZaDE8k8AQs2gKbPZGPmrIH6GQG"
df = pd.read_csv(url)

# Ver las primeras filas del dataframe para inspeccionar los datos
print("Primeras filas del DataFrame:")
print(df.head())

# Paso 2: Comprobar valores faltantes con Missingno

# Visualización de la matriz de valores faltantes
msno.matrix(df)
plt.title("Matriz de Valores Faltantes")
plt.show()

# Visualización de los valores faltantes por columna en un gráfico de barras
msno.bar(df)
plt.title("Valores Faltantes por Columna")
plt.show()

# Visualización del mapa de calor de los valores faltantes
msno.heatmap(df)
plt.title("Mapa de Calor de Valores Faltantes")
plt.show()


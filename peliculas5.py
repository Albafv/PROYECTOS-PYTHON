import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Cargar el dataset
df= pd.read_csv(r'C:\Users\Admin\Desktop\ws\IMDB-Movie-Data.csv')

# Selección de las columnas relevantes
df = df[['Title', 'Year', 'Runtime (Minutes)', 'Rating', 'Votes', 'Revenue (Millions)']]

# Convertir las columnas a un array de Numpy
title_numpy = df['Title'].to_numpy()
year_numpy = df['Year'].to_numpy()
runtime_numpy = df['Runtime (Minutes)'].to_numpy()
rating_numpy = df['Rating'].to_numpy()
votes_numpy = df['Votes'].to_numpy()
revenue_numpy = df['Revenue (Millions)'].to_numpy()

# Manejo de valores faltantes en 'Revenue (Millions)', reemplazándolos con la media de la columna
revenue_series = df['Revenue (Millions)']
df['Revenue (Millions)'] = revenue_series.fillna(revenue_series.mean())

# Convertir nuevamente a un array de Numpy después de reemplazar los valores faltantes
revenue_numpy = df['Revenue (Millions)'].to_numpy()


# Calcular la calificación promedio de las películas
average_rating = np.mean(rating_numpy)
print(f"Calificación promedio de las películas: {average_rating}")

# Encontrar la película con la duración más larga
longest_runtime_index = np.argmax(runtime_numpy)
longest_runtime_movie = df.iloc[longest_runtime_index]['Title']
longest_runtime = runtime_numpy[longest_runtime_index]
print(f"La película con la duración más larga es '{longest_runtime_movie}' con {longest_runtime} minutos.")

# Determinar el ingreso promedio y la mediana de los ingresos de las películas
average_revenue = np.mean(revenue_numpy)
median_revenue = np.median(revenue_numpy)
print(f"Ingreso promedio de las películas: ${average_revenue} millones")
print(f"Ingreso mediano de las películas: ${median_revenue} millones")

# Manipulación de Datos

# Crear un subconjunto de datos con películas lanzadas en los últimos 10 años
current_year = 2024
last10years_df = df[df['Year'] >= current_year - 10]

# Convertir a un array de Numpy las columnas relevantes del subconjunto
last10years_votes_numpy = last10years_df['Votes'].to_numpy()

# Calcular el promedio de votos para este subconjunto
average_votes_last10years = np.mean(last10years_votes_numpy)
print(f"Promedio de votos de las películas en los últimos 10 años: {average_votes_last10years}")



# Correlación entre la calificación de IMDb y los ingresos de las películas
correlation = np.corrcoef(rating_numpy, revenue_numpy)[0, 1]
print(f"Correlación entre la calificación de IMDb y los ingresos: {correlation}")

# Representación gráfica de la correlación
plt.scatter(rating_numpy, revenue_numpy, alpha=0.5)
plt.title('Correlación entre Calificación de IMDb y Ingresos')
plt.xlabel('Calificación de IMDb')
plt.ylabel('Ingresos (Millones)')
plt.grid(True)
plt.show()
import pandas as pd
import requests

API_KEY = 'b50f00d8'

# Función para obtener los datos de una película desde OMDB
def obtener_datos_pelicula(nombre_pelicula):
    url = f"http://www.omdbapi.com/?t={nombre_pelicula}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    if data['Response'] == 'True':
        # Extraer la información básica
        return {
            'protagonistas': data.get('Actors', 'Desconocido'),
            'genero': data.get('Genre', 'Desconocido'),
            'año': data.get('Year', 'Desconocido'),
        }
    else:
        print(f"No se encontró información para: {nombre_pelicula}")
        return {
            'protagonistas': 'Desconocido',
            'genero': 'Desconocido',
            'año': 'Desconocido',
        }

# Función para cargar datos de películas en un DataFrame
def cargar_csv_de_peliculas():
    # Aquí puedes colocar los títulos de las películas manualmente o desde un CSV que ya tengas.
    peliculas = ['Inception', 'The Dark Knight', 'Titanic', 'The Matrix', 'Interstellar']
    data = []

    for pelicula in peliculas:
        info_pelicula = obtener_datos_pelicula(pelicula)
        info_pelicula['nombre'] = pelicula
        data.append(info_pelicula)

    # Crear un DataFrame con los datos obtenidos
    df = pd.DataFrame(data)
    
    # Guardar el DataFrame en un CSV
    df.to_csv('peliculas.csv', index=False)
    return df

# Función para explorar el DataFrame
def explorar_dataframe(df):
    # Mostrar las primeras 5 filas
    print("Primeras 5 filas del DataFrame:")
    print(df.head())

    # Mostrar las últimas 5 filas
    print("\nÚltimas 5 filas del DataFrame:")
    print(df.tail())

    # Obtener información general del DataFrame
    print("\nInformación general del DataFrame:")
    print(df.info())

# Función para enriquecer los datos de la película
def enriquecer_datos(df):
    # Enriquecer con más detalles de los protagonistas y género
    for index, row in df.iterrows():
        # Obtener la información de la película desde OMDB
        info_pelicula = obtener_datos_pelicula(row['nombre'])
        
        # Añadir los detalles al DataFrame
        df.at[index, 'protagonistas'] = info_pelicula['protagonistas']
        df.at[index, 'genero'] = info_pelicula['genero']
        df.at[index, 'año'] = info_pelicula['año']
        
    # Guardar el DataFrame enriquecido
    df.to_csv('peliculas_enriquecidas.csv', index=False)
    return df

# Función principal
def main():
    # Cargar el CSV de las películas
    df = cargar_csv_de_peliculas()

    # Explorar el DataFrame
    explorar_dataframe(df)

    # Enriquecer los datos con la información de la API
    df_enriquecido = enriquecer_datos(df)

    # Mostrar el DataFrame enriquecido
    print("\nDataFrame enriquecido:")
    print(df_enriquecido)

# Ejecutar el programa
if __name__ == "__main__":
    main()

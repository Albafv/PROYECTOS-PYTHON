import requests
import json  

# Reemplaza 'your_api_key' con clave de API de OMDb
api_key = 'b50f00d8'
movie_name = 'Inside Out'  # Película que deseas buscar

# URL de la OMDb API
url = f"http://www.omdbapi.com/?t={movie_name}&apikey={api_key}"
payload = {}
headers = {}

# Hacemos la solicitud GET
response = requests.get(url, headers=headers, data=payload)


# Convertimos la respuesta en formato JSON
movie_data = response.json()

# Guardamos el JSON en un archivo
with open('movie_data.json', 'w') as json_file:
    json.dump(movie_data, json_file, indent=4)  # Guardamos con formato legible
    print("La respuesta se ha guardado en 'movie_data.json'")

print(movie_data)
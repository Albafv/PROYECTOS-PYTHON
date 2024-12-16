#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests

# Cargar la clave API de OMDB
API_KEY = 'b50f00d8'

# Lista de películas, que estará almacenada en un archivo JSON
FILM_NAME = 'peliculas.json'

# Función para cargar películas desde el archivo JSON
def cargar_peliculas():
    try:
        with open(FILM_NAME, 'r', encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Función para guardar películas en el archivo JSON
def guardar_peliculas():
    with open(FILM_NAME, 'w', encoding="utf-8") as f:
        json.dump(listapelis, f, ensure_ascii=False, indent=4)

# Lista vacía de películas
listapelis = cargar_peliculas()

# Función para añadir películas
def meterenlista():
    nombre = input("Añade una película: ")
    
    # Verificar si la película ya existe por nombre
    if any(pelicula['nombre'] == nombre for pelicula in listapelis):
        print("Esa película ya está en la lista")
    else:
        # Buscar la película en OMDB si no está en la lista
        respuesta = requests.get(f"http://www.omdbapi.com/?t={nombre}&apikey={API_KEY}")
        datos = respuesta.json()
        
        if datos['Response'] == 'True':
            director = datos.get('Director', 'Desconocido')
            year = datos.get('Year', 'Desconocido')
            presupuesto = datos.get('BoxOffice', 'Desconocido')
            print(f"Película encontrada: {director}, {year}, {presupuesto}")
        else:
            print("Película no encontrada en OMDB. Introduce la información manualmente.")
            director = input("Introduce el director de la película: ")
            year = input("Introduce el año de la película: ")
            presupuesto = input("Introduce el presupuesto de la película: ")
        
        # Crear un diccionario para la película
        pelicula = {
            'nombre': nombre,
            'director': director,
            'year': year,
            'presupuesto': presupuesto
        }
        
        # Añadir la película a la lista
        listapelis.append(pelicula)
        guardar_peliculas()  # Guardar la lista actualizada en el archivo JSON
        print("Película añadida!")

# Función para buscar películas
def buscarenlista():
    buscar = input("Busca si una película está en la lista: ")
    # Buscar la película por nombre
    pelicula_encontrada = next((pelicula for pelicula in listapelis if pelicula['nombre'] == buscar), None)
    
    if pelicula_encontrada:
        print("La película está en la lista!")
        print(f"Detalles: Director: {pelicula_encontrada['director']}, Año: {pelicula_encontrada['year']}, Presupuesto: {pelicula_encontrada['presupuesto']}")
    else:
        print("La película no está en la lista")

# Función para borrar películas
def borrarenlista():
    borrar = input("Elimina una película: ")
    # Buscar y eliminar la película por nombre
    pelicula_encontrada = next((pelicula for pelicula in listapelis if pelicula['nombre'] == borrar), None)
    
    if pelicula_encontrada:
        listapelis.remove(pelicula_encontrada)
        guardar_peliculas()  # Guardar la lista actualizada en el archivo JSON
        print("Película borrada!")
    else:
        print("Esa película ya no estaba en la lista")

# Función para mostrar todas las películas
def mostrarlista():
    if listapelis:
        for pelicula in listapelis:
            print(f"Nombre: {pelicula['nombre']}, Director: {pelicula['director']}, Año: {pelicula['year']}, Presupuesto: {pelicula['presupuesto']}")
    else:
        print("No hay películas en la lista.")
   
# Función para modificar el presupuesto de una película en concreto
def modificar_presupuesto():
    nombre = input("Introduce el nombre de la película cuyo presupuesto deseas modificar: ")
    
    # Buscar la película por nombre
    pelicula_encontrada = next((pelicula for pelicula in listapelis if pelicula['nombre'] == nombre), None)
    
    if pelicula_encontrada:
        # Pedir el nuevo presupuesto
        nuevo_presupuesto = input(f"Introduce el nuevo presupuesto para la película '{nombre}': ")
        
        # Asegurarse de que el presupuesto no sea menor a 1
        if float(nuevo_presupuesto) < 1:
            print("El presupuesto no puede ser menor a 1.")
        else:
            # Actualizar el presupuesto
            pelicula_encontrada['presupuesto'] = nuevo_presupuesto
            guardar_peliculas()  # Guardar la lista actualizada en el archivo JSON
            print(f"El presupuesto de '{nombre}' ha sido actualizado!")
    
    else:
        print("La película no está en la lista.")

# Menú de opciones
def mostrar_menu():
    print("""*** Menú: ***
        1. Añadir Película
        2. Borrar Película
        3. Mostrar Películas
        4. Buscar Película
        5. Modificar Presupuesto
        6. Salir""")


# Función principal
def main():
    salir = False
    while not salir:  # No salir hasta que salir=True
        # Enseñar siempre el menú:
        mostrar_menu()
        opcion = input("\nElige una opción (1-6): ")  # Pido al usuario que haga una acción

        if opcion == "1":
            meterenlista()
        elif opcion == "2":
            borrarenlista()
        elif opcion == "3":
            mostrarlista()
        elif opcion == "4":
            buscarenlista()
        elif opcion == "5":
            modificar_presupuesto()  # Llamada a la nueva opción
        elif opcion == "6":
            salir = True  # Sale del bucle while 
            print("¡Hasta luego!")
        else:
            print("Por favor, elige una opción entre 1 y 6.")
        

# Ejecutar el programa, esto es lo primero que se ejecuta:
if __name__ == "__main__":
    main()
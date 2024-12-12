#!/usr/bin/python
# -*- coding: utf-8 -*-

#Lista vacía de películas: cada película será un diccionario
listapelis=[]

#Función para añadir películas
def meterenlista():
    nombre = input("Añade una película: ")
    
    # Verificar si la película ya existe por nombre
    if any(pelicula['nombre'] == nombre for pelicula in listapelis):
        print("Esa película ya está en la lista")
    else:
        # Pedir los metadatos de la película
        director = input("Introduce el director de la película: ")
        año = input("Introduce el año de la película: ")
        presupuesto = input("Introduce el presupuesto de la película: ")
        
        # Crear un diccionario para la película
        pelicula = {
            'nombre': nombre,
            'director': director,
            'año': año,
            'presupuesto': presupuesto
        }
        
        # Añadir la película a la lista
        listapelis.append(pelicula)
        print("Película añadida!")

#Función para buscar películas
def buscarenlista():
    buscar=input("Busca si una película está en la lista: ")
    # Buscar la película por nombre
    pelicula_encontrada = next((pelicula for pelicula in listapelis if pelicula['nombre'] == buscar), None)
    
    if pelicula_encontrada:
        print("La película está en la lista!")
        print(f"Detalles: Director: {pelicula_encontrada['director']}, Año: {pelicula_encontrada['año']}, Presupuesto: {pelicula_encontrada['presupuesto']}")
    else:
        print("La película no está en la lista")

 #Función para borrar películas
def borrarenlista():
    borrar=input("Elimina una película: ")
     # Buscar y eliminar la película por nombre
    pelicula_encontrada = next((pelicula for pelicula in listapelis if pelicula['nombre'] == borrar), None)
    
    if pelicula_encontrada:
        listapelis.remove(pelicula_encontrada)
        print("Película borrada!")
    else:
        print("Esa película ya no estaba en la lista")

#Función para mostrar todas las películas
def mostrarlista():
    print(listapelis)
   
    

# Menú de opciones
def mostrar_menu():
    print("""*** Menú: ***
        1. Añadir Película
        2. Borrar Película
        3. Mostrar Películas
        4. Buscar Película
        5. Salir""")


# Función principal
def main():
    salir=False
    while not salir: #No salir hasta que salir=True
        #Enseño siempre el menú:
        mostrar_menu()
        opcion = input("\nElige una opción (1-5): ") #Pido al usuario que haga una acción


        if opcion == "1":
            meterenlista()
        elif opcion == "2":
            borrarenlista()
        elif opcion == "3":
            mostrarlista()
        elif opcion == "4":
            buscarenlista()
        elif opcion == "5":
            salir=True #Sale del bucle while 
            print("¡Hasta luego!")
        else:
            print("Por favor, elige una opción entre 1 y 5.")
        

# Ejecutar el programa, esto es lo primero que se ejecuta:
if __name__ == "__main__":
    main()
    




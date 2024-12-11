#!/usr/bin/python
# -*- coding: utf-8 -*-

#Lista vacía de películas:
listapelis=[]

#Función para añadir películas
def meterenlista():
    meter=input("Añade una película: ")
    if meter in listapelis:
        print("Esa película ya está en la lista")
    else:
        listapelis.append(meter)
        print("Película añadida!")

#Función para buscar películas
def buscarenlista():
    buscar=input("Busca si una película está en la lista: ")
    if buscar in listapelis:
        print("La película está en la lista!")
    else:
        print("La película no está en la lista")

 #Función para borrar películas
def borrarenlista():
    borrar=input("Elimina una película: ")
    if borrar in listapelis:
        listapelis.remove(borrar)
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
    




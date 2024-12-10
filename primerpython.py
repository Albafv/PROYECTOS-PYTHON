#!/usr/bin/python
print("hola, esto siempre se imprime")
a=1
if a==1:
    print("a es 1")
else:
    print ("a no es 1")


# Programa que realiza operaciones aritméticas sencillas

# Pedir al usuario que ingrese dos números
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

# Realizar las operaciones
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

# Verificar si el segundo número es cero antes de realizar la división
if numero2 != 0:
    division = numero1 / numero2
else:
    division = "No se puede dividir entre cero"

# Mostrar los resultados
print(f"La suma de {numero1} y {numero2} es: {suma}")
print(f"La resta de {numero1} y {numero2} es: {resta}")
print(f"La multiplicación de {numero1} y {numero2} es: {multiplicacion}")
print(f"La división de {numero1} entre {numero2} es: {division}")
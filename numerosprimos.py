#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
# DADO UN NÚMERO CUALQUIERA, ¿SABEMOS SI ES PRIMO?
numero = float(input("Ingresa un número: "))

if numero != int(numero):
    print(f"El {numero} es decimal. Los números decimales no son primos.")

elif numero <=1 : 
    print(f"El {numero} es menor que 1. Los números menores que 1 no son primos.")

elif numero % 2 == 0:
     print(f"El {numero} es par. Los números pares mayores que 2 no son primos.")

elif numero == 2:   
    print(f"El número {numero} es primo, el único primo par.")

else:
    # Falta comprobar que el número tenga otros divisores.
    """Si tiene un divisor >sqrt(numero), necesariamente tendrá otro divisor <sqrt(numero).
    Esto es debido a que numero=divisor*cociente=sqrt(numero)*sqrt(numero).
    Por tanto, basta comprobar divisores hasta sqrt(numero), pues la existencia de uno 
    en este rango implica directamente la existencia de otro (el cociente) en un rango >sqrt(numero)."""
    #ponemos un paso de 2 para saltarnos los numeros pares, que ya han sido evaluados antes.
    for i in range(3, int(math.sqrt(numero)) + 1, 2): 
        if numero % i == 0:
            print(f"El número {numero} no es primo") # Si encontramos un divisor, no es primo
            break
    else:#si no encontramos un divisor, el número es primo
        print(f"El número {numero} es primo.")

    
# Mostrar también el resultado de algunas operaciones
print(f"El módulo de {numero} % 5 es: {numero % 5}")
print(f"La raíz cuadrada de {numero} es aproximadamente: {round(math.sqrt(numero), 2)}")
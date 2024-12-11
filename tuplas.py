# Convertir la tupla a una lista e imprimirla
mis_datos = ("manzana", "banana", 7, 2.5)

lista_datos = list(mis_datos)

print("Lista convertida de la tupla:", lista_datos)


# Cambiar el segundo elemento de la lista y volver a convertirla a tupla
lista_datos[1] = "naranja" 

tupla_final = tuple(lista_datos)

print("Tupla después de la modificación:", tupla_final)



# tupla de números y hacer algunas operaciones
numeros = (15, 25, 35, 45, 55)

# Sumar todos los números
total = sum(numeros)
# Encontrar el valor máximo y el mínimo
maximo = max(numeros)
minimo = min(numeros)

print(f"Total: {total}, Máximo: {maximo}, Mínimo: {minimo}")


# Cuadrados de los números de la tupla usando comprensión de listas
cuadrados_numeros = [n**2 for n in numeros]
print("Cuadrados de los números:", cuadrados_numeros)

#  Desempaquetar la tupla en variables
x, y, z, w, v = numeros

print(f"Desempaquetado: x={x}, y={y}, z={z}, w={w}, v={v}")
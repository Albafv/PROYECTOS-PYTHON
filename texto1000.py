#!/usr/bin/python
# -*- coding: utf-8 -*-

# Crear un texto largo de 1000 líneas como una lista de strings
texto_largo = ["Línea " + str(i + 1) for i in range(1000)]

# Lista vacía para almacenar los bloques
bloques = []

# Número de líneas por bloque
lineas = 25

# Iterar a través de las líneas del texto, en pasos de 25
for i in range(0, len(texto_largo), lineas):
    bloque = texto_largo[i:i + lineas]  # Obtener un bloque de 25 líneas
    bloques.append(bloque)  # Añadir el bloque a la lista de bloques

print(len(bloques))
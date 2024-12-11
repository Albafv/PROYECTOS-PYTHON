#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
# Lista random de temperaturas entre -500 y 500 º
temperaturas = [random.randint(-700, 700) for _ in range(100)]
#Filtrado de temperaturas mayores que -196 ºC
crit=-196
gaseoso =  [temp for temp in temperaturas if (temp >= crit)]
# Imprimimos las temperaturas y cuántas cumplen la condición
print("Temperaturas donde el nitrógeno es gaseoso:", gaseoso)
print("En ", len(gaseoso) ," ocasiones, el nitrógeno se encontraba en estado gas")
import random
# Lista random de temperaturas entre -500 y 500 º
temperaturas = [random.randint(-700, 700) for _ in range(100)]
#Filtrado de temperaturas mayores que -196 ºC
gaseoso =  [temp for temp in temperaturas if (temp > -196)]
# Imprimimo las temperaturas y cuántas cumplen la condición
print("Temperaturas donde el nitrógeno es gaseoso:", gaseoso)
print("En ", len(gaseoso) ," ocasiones, el nitrógeno se encontraba en estado gas")
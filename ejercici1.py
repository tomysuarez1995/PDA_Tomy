import math
from math import acos
print ("Bienvenido! este es un programa para calcular la distancia entre dos puntos")
t= input ("desea calcular sus coordenadas? (y/n)")
if t == "y":
    g_1 = float(input("Escriba el primer valor de latitud: "))
    t_1 = float(input("Escriba el primer valor de longitud:  "))
    g_2 = float(input("Escriba el segundo valor de latitud: "))
    t_2 = float(input("Escriba el segundo valor de longitud: "))
    print(f"La primeras coordenadas fueron:({g_1}, {t_1})")
    print(f"Las segundas coordenadas fueron: ({g_1}, {t_1})")  
    a7= 6371.01 * acos(( math.sin (t_1)*math.sin(t_2))+math.cos(t_1)*math.cos(t_2)*math.cos(g_1 - g_2))
    print("la distancia es: " + str(a7))
    print ("espero le haya sido de ayuda! Adios :D ")
else:
    print ("Vuelva pronto :D")



# ## Ejercicio 3 - Formando un triángulo mediante tres puntos (obligatorio)

# Implemente una clase *Triangle()*. La misma debe,

# - Tener un constructor que reciba tres objetos del tipo *Punto()* (esta clase fue vista en teoría y ejercitación). Durante la creación del triángulo se debe chequear que los puntos otorgados por el usuario formen un triangulo, caso contrario deben dar un *error*, para esto implemente la siguiente linea de código,
# ```Python
# raise ValueError("Los puntos no forman un triangulo")
# ```
# - Debe tener un método para determinar qué tipo de triangulo es en base a la longitud de sus lados.
#     - Equilatero: Tres lados iguales.
#     - Isósceles: Dos lados iguales.
#     - Escaleno: Ninguno de sus lados iguales.
    
# - Debe tener un método para calcular el área del triángulo.
# - Debe tener un método para devolver las longitudes de los lados del triángulo.

# NOTA: En el módulo 5 veremos más sobre manejo de errores y excepciones.

class Triangle():
    """esta clase determina si hay un triangulo y de ser asi lo identifica y clasifica segun sus lados"""
    def __init__(yo, p1, p2, p3):
        """constructor"""
        if yo.existencia(p1,p2,p3) == 1:
            yo.p1 = p1
            yo.p2 = p2
            yo.p3 = p3
            print("se formo un triangulo donde: ")
        elif yo.existencia(p1,p2,p3)==0:
            raise ValueError("No forma un triangulo")

    def existencia(yo, p1, p2, p3):
        """con esta funcion definimos la existencia del triangulo"""
        pp1=p1[0]+p1[1]
        pp2=p2[0]+p2[1]
        pp3=p3[0]+p3[1]
        try:
            pen12= (p2[1]-p1[1])/(p2[0]-p1[0])
        except:
            pen12 = 0
        try:
            pen13 =(p3[1]-p1[1])/(p3[0]-p1[0])
        except:
            pen13= 0 
        if pp1==pp2 or pp1==pp3:
            return 0
        elif  pen12 == 0 and pen13 ==0:
            return 0
        elif pp1 != pp2 or pp1 != pp3:
            return 1
        elif pen12 != 0 and pen13 !=0:
            return 1

    def lineas(yo):
        """Genero las lineas del triangulo con los puntos"""
        l12= round(((((yo.p2[1]-yo.p1[1])**2)+((yo.p2[0]-yo.p1[0])**2))**(1/2)),2)
        l23= round(((((yo.p3[1]-yo.p2[1])**2)+((yo.p3[0]-yo.p2[0])**2))**(1/2)),2)
        l13= round(((((yo.p3[1]-yo.p1[1])**2)+((yo.p3[0]-yo.p1[0])**2))**(1/2)),2)
        return l12, l23, l13

    def perimetro(yo):
        """calculo el perimetro"""
        s= sum(yo.lineas())/2
        return round(s,2)

    def area(yo):
        """este metodo genera el area del triangulo"""
        s= yo.perimetro()
        areas =(s*(s-yo.lineas()[0])*(s-yo.lineas()[1])*(s-yo.lineas()[2]))**(1/2)
        return round(areas, 2)

    def tipo(yo):
        """este metodo nos dice que tipo de triangulo es"""

        if yo.lineas()[0]== yo.lineas()[1] and yo.lineas()[0]==yo.lineas()[2]:
            return "Equilatero"
        elif yo.lineas()[0] != yo.lineas()[1] and yo.lineas()[0] != yo.lineas()[2]:
            return "Escaleno"
        else:
            return "Isoceles"

punto1=(2,13)
punto2=(22,7)
punto3=(32,71)
triangulo= Triangle(punto1, punto2, punto3)
print(f"sus lados son: {triangulo.lineas()}")
print(f"su perimetro es: {triangulo.perimetro()}")
print(f"su area es: {triangulo.area()}")
print (f"es un triangulo de tipo: {triangulo.tipo()}")

"""NOTA* COMO RESOLVER LO DE PASAR DE LISTAS A OTRA FUNCION, COMO YO LO PIENSO: yo.lineas([0]) pero no anda"""




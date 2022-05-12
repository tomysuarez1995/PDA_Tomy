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
import math
class Punto():
    """Clase para crear y operar puntos en un plano 2D
    
    p0 = Punto()
    p1 = Punto(3,4)
    p0.calcularDistancia(punto1) # retorna 5.0
    """
    
    def __init__(self, x:float = 0.0, y:float = 0.0) ->None:
        """Iniciamos coordenadas de los puntos.
        Si los puntos x e y no se dan, se los inicializa en el origen"""
        self.moveTo(x, y)  
    
    def moveToOrigin(self) ->None:
        """Mueve un punto al origen"""
        self.x = 0.
        self.y = 0.
        
    def moveTo(self, newx:float, newy:float) ->None:
        """Mueve un punto a una nueva coordenada"""
        self.x = newx
        self.y = newy
        
    def calcularDistancia(self, otroPunto: "Punto") ->float:
        """Calcula la distancia euclidiana entre dos puntos
        
        Parámetro:
            - otroPunto: Instancia de un Punto()
            
        Retorna:
            - La distancia entre puntos (float)
        """
        return math.hypot(self.x - otroPunto.x, self.y - otroPunto.y)
    
    def __str__(self):
        """Imprimimos coordenadas del punto"""
        return f"P(%s,%s)"  % (self.x, self.y)
    
    def __eq__(self, otroPunto):
        """Comparamos si dos puntos son iguales"""
        if not isinstance(otroPunto, Punto):
            return False
        else:
            return (self.x, self.y) == (otroPunto.x, otroPunto.y)

            
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
        
        try:
            pen12= (p2.y-p1.y)/(p2.x-p1.x)
        except:
            pen12 = 0
        try:
            pen13 =(p3.y-p1.y)/(p3.x-p1.x)
        except:
            pen13= 0 
        if p1==p2 or p1==p3 or p2==p3:
            return 0
        elif  pen12 == 0 and pen13 ==0:
            return 0
        elif (p1.x == p2.x and p1.x==p3.x and p2.x==p3.x):
            return 0
        elif (p1.y== p2.y and p1.y==p3.y and p2.y==p3.y):
            return 0
        elif p1 != p2 or p1 != p3 or p2!=p3:
            return 1
        elif pen12 != 0 and pen13 !=0:
            return 1

    def lineas(yo):
        """Genero las lineas del triangulo con los puntos"""
        l12= round(((((yo.p2.y-yo.p1.y)**2)+((yo.p2.x-yo.p1.x)**2))**(1/2)),2)
        l23= round(((((yo.p3.y-yo.p2.y)**2)+((yo.p3.x-yo.p2.x)**2))**(1/2)),2)
        l13= round(((((yo.p3.y-yo.p1.y)**2)+((yo.p3.x-yo.p1.x)**2))**(1/2)),2)
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

punto1=Punto(2,23)
punto2=Punto(23,2)
punto3=Punto(18,71)
triangulo= Triangle(punto1, punto2, punto3)
print(f"sus lados son: {triangulo.lineas()}")
print(f"su perimetro es: {triangulo.perimetro()}")
print(f"su area es: {triangulo.area()}")
print (f"es un triangulo de tipo: {triangulo.tipo()}")





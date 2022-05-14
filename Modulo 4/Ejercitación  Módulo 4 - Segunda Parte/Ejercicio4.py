from cmath import inf
from numpy import NaN, Inf, arange, isscalar, asarray, array
import matplotlib.pyplot as plt
class BasicPlethy():
    """Doc acá..."""
    
    def __init__(self, signal:list, fm:float = 125.):
        """Doc del constructor..."""
        self.señal = signal #señal
        self.fm = fm #frecuencia de muestreo
        self.T =  1/fm #Período de la señal
        self.Duracion = len(signal)*self.T # Duración de la señal (en segundos)
        
    def duration(self):
        """Returna la duración de la señal"""
        return f"tiene {round(self.Duracion,0)} segundos" 
        
    def piquitos(self)->list:
        """Obtiene los momentos en que ocurren los picos en la señal, codigo basado en deteccion de picos
        de mathlab"""
        picosmax= []
        x = arange(len(self.señal))
        max= -Inf #floating point representation of (positive) infinity, sacado de numpy
        min= Inf #floating point representation of (positive) infinity, sacado de numpy
        maxposit = NaN #floating point representation of Not a Number (NaN), sacado de numpy
        minposit = NaN #floating point representation of Not a Number (NaN), sacado de numpy
        buscar= None
        umbral= .75 #valor para comparar con el anterior maximo
        for i in arange(len(self.señal)):
            señal = self.señal[i]
            if señal > max: #este if sirve para tomar el valor maximo y guardarlo en max y maxposit toma el valor de la copia x[i]
                max = señal
                maxposit = x[i]
            elif señal < min:#este if sirve para tomar el valor minimo y guardarlo en min y minposit toma el valor de la copia x[i]
                min = señal
                minposit = x[i]
                
            if buscar:
                if señal < (max*umbral):
                    """este if sirve para ir guardando en picosmax los picos maximos"""
                    picosmax.append((maxposit))
                    min = señal
                    minposit = x[i]
                    buscar = False
            else:
                if señal > (min*umbral):
                    """este if sirve para retroalimentar los picos max y al for"""
                    max = señal
                    maxposit = x[i]
                    buscar = True
        qiqi=[]
        for j in picosmax:
            """con este for tomo los valores de los picos y los paso a segundos"""
            air= round((j/self.fm),1)
            qiqi.append(air)

        return qiqi

    def freq(self)->float:
        """Calcula la frecuencia cardíaca en latidos por minutos (Heart Rate)..."""
        return (len(self.piquitos()))/(self.Duracion/60)

        
        
lePlesti = open("plethysmography.txt", "r")
leListe = [float(valor) for valor in lePlesti.read().split()]
lista2 = leListe[:8000]
leMandar= BasicPlethy(leListe)
print(f"la señal tiene un tiempo de: {leMandar.duration()}")
print(f"tiene una frecuencia cardiaca de:{leMandar.freq()}" )
print(f"los picos ocurren en los segundos: {leMandar.piquitos()}")
print(f"tiene: {len(leMandar.piquitos())} picos ")
#plt.scatter(array(leMandar.piquitos())[:,0],array(leMandar.piquitos())[:,1], color='r')
#plt.plot(leListe, color = "g")
#plt.show()


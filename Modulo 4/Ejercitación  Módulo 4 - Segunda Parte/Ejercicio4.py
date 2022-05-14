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
        picosmin = []
        x = arange(len(self.señal))
        max= -Inf #floating point representation of (positive) infinity, sacado de numpy
        min= Inf #floating point representation of (positive) infinity, sacado de numpy
        maxposit = NaN #floating point representation of Not a Number (NaN), sacado de numpy
        minposit = NaN #floating point representation of Not a Number (NaN), sacado de numpy
        buscar= None
        umbral= .75 #valor para comparar con el anterior maximo
        for i in arange(len(self.señal)):
            señal = self.señal[i]
            if señal > max:
                max = señal
                maxposit = x[i]
            elif señal < min:
                min = señal
                minposit = x[i]
                
            if buscar:
                if señal < (max*umbral):
                    picosmax.append((maxposit))
                    min = señal
                    minposit = x[i]
                    buscar = False
            else:
                if señal > (min*umbral):
                    picosmin.append((minposit))
                    max = señal
                    maxposit = x[i]
                    buscar = True
        qiqi=[]
        for j in picosmax:
            air= j/self.fm
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
print(f"tiene:{len(leMandar.piquitos())} picos ")
#plt.scatter(array(leMandar.piquitos())[:,0],array(leMandar.piquitos())[:,1], color='r')
#plt.plot(leListe, color = "g")
#plt.show()


from numpy import NaN, Inf, arange
import matplotlib.pyplot as plt
class BasicPlethy():
    """Est clase nos sirve para procesar señales plestimograficas"""
    
    def __init__(self, signal:list, fm:float = 125.):
        """constructor"""
        self.señal = signal #señal
        self.fm = fm #frecuencia de muestreo
        self.T =  1/fm #Período de la señal
        self.Duracion = len(signal)*self.T # Duración de la señal (en segundos)
        
    def duration(self):
        """Returna la duración de la señal"""
        return f"{round(self.Duracion,0)} seg" 
        
    def piquitos(self)->list:
        """Obtiene los momentos en que ocurren los picos en la señal, codigo basado en deteccion de picos
        de mathlab"""
        picosmax= []
        x = arange(len(self.señal)) #generamos un array de duracion de la señal -1 valor osea 60.001-1 = 60.000, esto para guardar la ubicacion del pico
        max= -Inf #floating point representation of (positive) infinity, sacado de numpy
        min= Inf #floating point representation of (positive) infinity, sacado de numpy
        maxposit = NaN #floating point representation of Not a Number (NaN), sacado de numpy
        buscar= None
        umbral= .75 #valor para comparar con el anterior maximo y descartar diastole en % 0.75 = 75%
        for i in arange(len(self.señal)):
            señal = self.señal[i]
            if señal > max: #este if sirve para tomar el valor maximo y guardarlo en max y maxposit toma el valor de la copia x[i]
                max = señal
                maxposit = x[i]
            elif señal < min:
                """Este elif sirve para tomar los minimos y despue usarlos para compararlos con los maxios"""
                min = señal
            if buscar:
                if señal < (max*umbral):
                    """este if sirve para ir guardando en picosmax los picos maximos"""
                    picosmax.append((maxposit))
                    min = señal
                    buscar = False
            else:
                if señal > (min*umbral):
                    """este if sirve para retroalimentar los picos max y descartar los minimos al umbral"""
                    max = señal
                    maxposit = x[i]
                    buscar = True
        return picosmax

    def momentos(self):   
        """"devuelve los picos pasados a segundos"""
        qiqi=[]
        for j in self.piquitos():
            """con este for tomo los valores de los picos y los paso a segundos"""
            air= round((j/self.fm),1)
            qiqi.append(air)
        return qiqi
        

    def freq(self)->float:
        """Calcula la frecuencia cardíaca en latidos por minutos (Heart Rate) en los primeros 10 seg"""
        return round((len(self.piquitos()*60)/(self.Duracion)),1)
    



lePlesti = open("plethysmography.txt", "r")
leListe = [float(valor) for valor in lePlesti.read().split()]
leMandar= BasicPlethy(leListe)

print(f"los picos ocurren en los segundos: {leMandar.momentos()}")
print(f"tiene: {len(leMandar.momentos())} picos ")
print(f"la señal tiene un tiempo de: {leMandar.duration()}")
print(f"tiene una frecuencia cardiaca de: {leMandar.freq()} LPM" )







class BasicPlethy():
    """Doc acá..."""
    
    def __init__(self, signal:list, fm:float = 125.):
        """Doc del constructor..."""
        self.signal = signal #señal
        self.fm = fm #frecuencia de muestreo
       # self.T =  #Período de la señal
        #self.signalDuration =  # Duración de la señal (en segundos)
        
    def duration(self):
        """Returna la duración de la señal"""
       
        
    def getHR(self)->float:
        """Calcula la frecuencia cardíaca en latidos por minutos (Heart Rate)..."""
       
        return 
        
    def getPeaks(self)->list:
        """Obtiene los momentos en que ocurren los picos en la señal"""
       
        
        return 
lePlesti = open("plethysmography.txt", "r")
leListe = [float(valor) for valor in lePlesti.read().split()]
leMandarALaClase= BasicPlethy(leListe)
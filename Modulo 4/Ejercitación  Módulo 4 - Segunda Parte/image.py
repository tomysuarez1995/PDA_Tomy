"""Clase Image para el ejercicio de la Ejercitación Módulo 4 - Segunda Parte"""
from numpy import uint8
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from utils import crearMatrix

class Image():
    """Documentación de Image"""

    def __init__(self, dimensiones:tuple = None, filename:str = ""):
        """Crea una imagen
        Paramas:
            - dimensiones: tupla con las dimensiones de la imágen a formar
            - filenme: nombre del archivo de imágen a cargar
        """
        if dimensiones:
            self.image = crearMatrix(dimensiones) #generamos una matriz de ceros
            self.filas = self.image.shape[0]
            self.columnas = self.image.shape[1]
            self.canales = self.image.shape[2]
        elif filename:
            self.image = self._loadImage(filename)
            self.filas = self.image.shape[0] #número de filas
            self.columnas = self.image.shape[1] #número de columnas
            self.canales = self.image.shape[2]
        else:
            raise ValueError("No se ha dado una dimensión ni un archivo")

    def _loadImage(self, filename:str):
        """Cargamos imágen"""
        return mpimg.imread(filename)
        
    def show(self):
        """Mostramos imágen"""
        imgplot = plt.imshow(self.image.astype(uint8)) #.astype(np.uint8)

    def size(self):
        """Retorna una tupla de la forma (filas, columnas, canales)
        Si Image posee un solo canal, devuelve una tupla de la forma (filas, columnas)
        """
        pass

    def saveImage(self, filename:str):
        """Guarda la imágen en un archivo jpg"""
        pass

def main():
    ## Genero un objeto Image a partir de un archivo jpg
    perro = Image(filename = "dog.jpg")

    ## si quisiera saber el valor del píxel en el canal ROJO, en la fila 200 y columna 250 podría hacer
    i = 200 #fila
    j = 250 #columna
    c = 0 # canal Rojo
    pixel = perro.image[j][j][canal]

    print(f"El valor del píxel es {pixel}")

    ## muestro la imágen
    # perro.show()

    ## Genero una imagen vacía con las mismas dimensiones de la imágen perro
    filas = perro.filas
    columnas = perro.columnas
    canales = perro.canales
    emptyImage = Image(dimensiones = (filas, columnas, canales))

    ##chequeamos las dimensiones de emptyImage
    print(f"emptyImage tiene una dimensión de {emptyImage.image.shape}")
    ## vemos que emptyImage tiene las mismas dimensiones que perro

    ## veamos que tiene emptyImage
    # emptyImage.show()
    ## Vemos que es una imágen en negro ya que todos sus píxeles son por defecto 0 al crear un nuevo objeto
    ## Image a partir de simensiones

    fig = plt.figure()
    ax = fig.add_subplot(1, 2, 1)
    imgplot = plt.imshow(perro.image)
    ax.set_title('Perro')
    ax = fig.add_subplot(1, 2, 2)
    imgplot = plt.imshow(emptyImage.image)
    ax.set_title('emptyImage')

if __name__ == '__main__':
    main()


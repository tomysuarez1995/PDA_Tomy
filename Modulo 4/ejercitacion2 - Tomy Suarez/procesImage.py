from image import Image
import numpy as np
from utils import crearMatrix

def ajustarBrillo(image, ajuste):
    """Doc..."""
    pass

def getHistograma(image):
    """Doc..."""
    pass

def getChannels(image):
    """Doc..."""
    pass

def ajustarContraste(image, alfa):
    """Ajusta el contraste de una imágen.
    
    Retorna una nueva imágen con las mismas dimensiones de la imágen original.
    """
    filas = image.image.shape[0] #cantidad de filas
    columnas = image.image.shape[1] #cantidad de columnas
    canales = image.image.shape[2]
    ## Creo un nuevo objeto Image
    imagenProcesada = Image(dimensiones = (filas, columnas, canales))
    for canal in range(canales):
        for i in range(filas):
            for j in range(columnas):
                pixel = int(alfa*(image.image[i][j][canal]-128) + 128)
                if pixel < 0:
                    pixel = 0
                elif pixel > 255:
                    pixel = 255
                imagenProcesada.image[i][j][canal] = pixel
                
    return imagenProcesada

def ajustarGamma(image, gamma):
    """Doc..."""
    pass

def aplicarKernel(image, kernel):
    """Doc..."""
    pass

def main():
    #Mostrar su implementación aquí
    pass

if __name__ == '__main__':
    main()

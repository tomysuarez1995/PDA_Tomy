"""Clase Image para el ejercicio de la Ejercitación Módulo 4 - Segunda Parte"""
from numpy import imag, uint8, zeros
import cv2
import numpy as np
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
        return cv2.imread(filename)
        
    def show(self):
        """Mostramos imágen"""
        imgplot = cv2.imshow(self.image.astype(uint8))

    def size(self):
        """Retorna una tupla de la forma (filas, columnas, canales)
        Si Image posee un solo canal, devuelve una tupla de la forma (filas, columnas)
        """
        pass

    def saveImage(self, filename:str):
        """Guarda la imágen en un archivo jpg"""
        pass


def ajustarBrillo(image, ajuste):
    """cambia el brillo de la imagen"""
    filas, columnas, canales = image.shape
    imagenBr= zeros((filas, columnas, canales))
    for canal in range(canales):
        for i in range(filas):
            for j in range(columnas):
                brillo = int(ajuste*(image[i][j][canal]))
                if brillo < 0:
                    brillo = 0
                elif brillo > 255:
                    brillo = 255
            imagenBr[i][j][canal] = brillo

    return imagenBr
            

def getHistograma(image):
    """Doc..."""
    alto, ancho, canal= img.shape
    ejex= np.linspace(0,255, num=256,dtype=np.uint8)
    ejey= np.zeros(256)
    for can in range(canal):
        for j in range(alto):
            for k in range(ancho):
                imag = img[j, k, can]
                ejey[imag] += 1
    return (ejex, ejey)    
def imprimirhist(image):
    plt.plot(getHistograma()[0], getHistograma()[1])
    plt.show()

def getChannels(image):
    """obtengo los canales""" 
    return f"los canales son {image.shape[2]}" 

def logT(image):
    """se ajusta logaritmo de la imagen"""
    c= 255/(np.log(1+np.max(image)))
    logi = c*np.log(1+image)
    return np.array(logi, dtype=uint8)

def ajustarContraste(image, alfa):
    """Ajusta el contraste de una imágen.
    
    Retorna una nueva imágen con las mismas dimensiones de la imágen original.
    """
    filas, columnas, canales = image.shape
    imagenProcesada= zeros((filas, columnas, canales))
    for canal in range(canales):
        for i in range(filas):
            for j in range(columnas):
                pixel = int(alfa*(image[i][j][canal]-128) + 128)
                if pixel < 0:
                    pixel = 0
                elif pixel > 255:
                    pixel = 255
                imagenProcesada[i][j][canal] = pixel
                #no entiendo el error que me da en imagenprocesada "TypeError: tuple expected at most 1 argument, got 3"
    return imagenProcesada

def ajustarGamma(imagen, gamma):
    """ajusto el gamma, donde la funcion power de numpy devuelve:
    numpy.power, para hacer la potencia"""
    gamm= np.power(imagen/float(np.max(imagen)), gamma)
    return gamm

def aplicarKernel(image, kernel):
    """Doc..."""
    pass

# def main():
#     ## Genero un objeto Image a partir de un archivo jpg
#     perro = Image(filename = "gallina.jpg")

#     ## si quisiera saber el valor del píxel en el canal ROJO, en la fila 200 y columna 250 podría hacer
#     i = 200 #fila
#     j = 250 #columna
#     c = 0 # canal Rojo
#     pixel = perro.image[j][j][c]

#     print(f"El valor del píxel es {pixel}")

#     ## muestro la imágen
#     # perro.show()

#     ## Genero una imagen vacía con las mismas dimensiones de la imágen perro
#     filas = perro.filas
#     columnas = perro.columnas
#     canales = perro.canales
#     emptyImage = Image(dimensiones = (filas, columnas, canales))

#     ##chequeamos las dimensiones de emptyImage
#     print(f"emptyImage tiene una dimensión de {emptyImage.image.shape}")
#     ## vemos que emptyImage tiene las mismas dimensiones que perro

#     ## veamos que tiene emptyImage
#     # emptyImage.show()
#     ## Vemos que es una imágen en negro ya que todos sus píxeles son por defecto 0 al crear un nuevo objeto
#     ## Image a partir de simensiones

#     fig = plt.figure()
#     ax = fig.add_subplot(1, 2, 1)
#     imgplot = plt.imshow(perro.image)
#     ax.set_title('Perro')
#     ax = fig.add_subplot(1, 2, 2)
#     imgplot = plt.imshow(emptyImage.image)
#     ax.set_title('emptyImage')

#     pass

img = cv2.imread('gallina.jpg')
gam=2
print(getChannels(img))
#print(img.shape)
enviar= getHistograma(img)
enviar
#enviar= ajustarGamma(img, gam)
#enviar2 = ajustarContraste(img, alfa= 2)
# cv2.imshow("gallina.jpg", img)
# cv2.imshow("nueva comtraste", enviar)
# cv2.waitKey(0)
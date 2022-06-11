"""Clase Image para el ejercicio de la Ejercitación Módulo 4 - Segunda Parte"""
from numpy import imag, uint8, zeros
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


# class Image():
#     """Documentación de Image"""

#     def __init__(self, dimensiones:tuple = None, filename:str = ""):
#         """Crea una imagen
#         Paramas:
#             - dimensiones: tupla con las dimensiones de la imágen a formar
#             - filenme: nombre del archivo de imágen a cargar
#         """
#         if dimensiones:
#             self.image = crearMatrix(dimensiones) #generamos una matriz de ceros
#             self.filas = self.image.shape[0]
#             self.columnas = self.image.shape[1]
#             self.canales = self.image.shape[2]
#         elif filename:
#             self.image = self._loadImage(filename)
#             self.filas = self.image.shape[0] #número de filas
#             self.columnas = self.image.shape[1] #número de columnas
#             self.canales = self.image.shape[2]
#         else:
#             raise ValueError("No se ha dado una dimensión ni un archivo")

#     def _loadImage(self, filename:str):
#         """Cargamos imágen"""
#         return cv2.imread(filename)
        
#     def show(self):
#         """Mostramos imágen"""
#         imgplot = cv2.imshow(self.image.astype(uint8))

#     def size(self):
#         """Retorna una tupla de la forma (filas, columnas, canales)
#         Si Image posee un solo canal, devuelve una tupla de la forma (filas, columnas)
#         """
#         pass

#     def saveImage(self, filename:str):
#         """Guarda la imágen en un archivo jpg"""
#         pass


def ajustarBrillo(image, ajuste):
    """cambia el brillo de la imagen"""
    image2=np.copy(image)
    return  np.clip(image*ajuste,0,255).astype(np.uint8)

    
def getHistograma(image):
    """Doc..."""
    plt.hist(np.histogram(image), bins = [0,50,100,150,200,250]) 
    plt.title("histogram") 
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
    return np.clip(128 + alfa * img - alfa * 128, 0, 255).astype(np.uint8)


def ajustarGamma(imagen, gamma ):
    """ajusto el gamma, donde la funcion power de numpy devuelve:
    numpy.power, para hacer la potencia"""
    gamm= np.power(imagen/float(np.max(imagen)), gamma)
    return gamm

def aplicarKernel(img, kernel,padding=0, strides=1):
    """Doc..."""
    xKernShape = kernel.shape[0]
    yKernShape = img.shape[1]
    xImgShape = img.shape[0]
    yImgShape = img.shape[1]

    # Shape of Output Convolution
    xOutput = int(((xImgShape - xKernShape + 2 * padding) / strides) + 1)
    yOutput = int(((yImgShape - yKernShape + 2 * padding) / strides) + 1)
    output = np.zeros((xOutput, yOutput))

    # Apply Equal Padding to All Sides
    if padding != 0:
        imagePadded = np.zeros((img.shape[0] + padding*2, img.shape[1] + padding*2))
        imagePadded[int(padding):int(-1 * padding), int(padding):int(-1 * padding)] = img
        print(imagePadded)
    else:
        imagePadded = img

    # Iterate through image
    for y in range(img.shape[1]):
    # Exit Convolution
        if y > img.shape[1] - yKernShape:
            break
    # Only Convolve if y has gone down by the specified Strides
        if y % strides == 0:
            for x in range(img.shape[0]):
                # Go to next row once kernel is out of bounds
                if x > img.shape[0] - xKernShape:
                    break
                try:
                    # Only Convolve if x has moved by the specified Strides
                    if x % strides == 0:
                        output[x, y] = (kernel * imagePadded[x: x + xKernShape, y: y + yKernShape]).sum()
                except:
                    break
        pass


img = mpimg.imread('files\monet.jpg')
# gam=2
# print(getChannels(img))
#print(img.shape)
# enviar= getHistograma(img)
#enviar= ajustarGamma(img, gam)
enviar2 = ajustarBrillo(img,2.1)


kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
output = aplicarKernel(img, kernel, padding=2)
kernel = np.flipud(np.fliplr(kernel))
plt.imshow(output)
plt.show()
 
# Gather Shapes of Kernel + Image + Padding

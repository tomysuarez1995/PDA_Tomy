import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('gallina.jpg')
alto, ancho, canal= img.shape
print(alto, ancho, canal)
cv2.imshow("gallina.jpg", img)
ejex= np.linspace(0,255, num=256,dtype=np.uint8)
ejey= np.zeros(256)
for can in range(canal):
    for j in range(alto):
        for k in range(ancho):
            imag = img[j, k,can]
            ejey[imag] += 1
            
            #histr = cv2.calcHist([img],[i],None,ejey,ejex)
            #plt.bar(histr,hight, color = col)
            #plt.xlim([0,256])

    plt.plot(ejex, ejey)
plt.show()

# img = cv2.imread('brainvessels1.jpg', cv2.IMREAD_GRAYSCALE)
# alto, ancho = img.shape
# cv2.imshow("brainvessels1.jpg", img)
# ejex=np.linspace(0,255, num=256,dtype=np.uint8)
# ejey=np.zeros(256)
# for i in range(alto):
#     for j in range(ancho):
#         imag = img[i, j]
#         ejey[imag] += 1
# plt.plot(ejex, ejey)
# plt.show()



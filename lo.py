import cv2
import numpy as np

alto=480
ancho=640
img=np.zeros((alto,ancho,3),dtype=np.uint8)

lado_cuadrado=200
x_inicio=(ancho-lado_cuadrado)//2
y_inicio=(alto-lado_cuadrado)//2
cv2.rectangle(img,(x_inicio,y_inicio),(x_inicio+lado_cuadrado,y_inicio+lado_cuadrado),(255,255,255),-1)
cv2.imshow('img',img)
cv2.imwrite('img_crada.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


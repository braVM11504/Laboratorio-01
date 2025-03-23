import cv2

def indentifyspot(m,b):
    img=cv2.imread(m)
    bordecanny=cv2.Canny(img,100,200)
    
    contours, _=cv2.findContours(bordecanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cv2.imshow(f'contornos  {b}',img)
    num_contours=len(contours)
    print(f"numero de contornos {b}: {num_contours}")
    
    return num_contours
    
contours_blue=indentifyspot('blue_car.jfif','carro_azul')
contours_red=indentifyspot('red_car.jfif','carro_rojo')
contours_yellow=indentifyspot('yellow_car.jfif','carro_amarillo')
contours_empty=indentifyspot('empty.jfif','espacio vacio')


if contours_blue > contours_empty:
    print("espacio ocupado ")
else:
    print("espacio libre")

if contours_red > contours_empty:
    print("espacio ocupado ")
else:
    print("espacio libre")

if contours_yellow > contours_empty:
    print("espacio ocupado ")
else:
    print("espacio libre")
if contours_empty == contours_empty: 
    print("el espacio está libre")
cv2.waitKey(0)
cv2.destroyAllWindows()








 




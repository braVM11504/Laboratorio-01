# Import OpenCV module
import cv2

# Read image
def indetifycolor(plane_r,plane_g,plane_b):
    if (plane_r>plane_g)and(plane_r>plane_b):
        return"el color predominante es rojo "
    elif (plane_g>plane_b)and(plane_g>plane_r):
        return"el color el predominante es Amarillo"
    elif (plane_b>plane_g)and(plane_b>plane_r):
        return"El color predominante es azul "
    else:
        return"no tiene color predominante "

slecimg= int(input("seleccion el color de el carro: 1= carro azul. 2=carro rojo, 3= carro amarillo: "))
if slecimg== 1: 
    img = cv2.imread("blue_car.jfif", cv2.IMREAD_COLOR)
    
elif slecimg== 2:
    img = cv2.imread("red_car.jfif", cv2.IMREAD_COLOR)
elif slecimg==  3:
    img = cv2.imread("yellow_car.jfif", cv2.IMREAD_COLOR)
else :
    print("no hay de ese color")

# Get image dimensions
dims=img.shape

# Show image dimensions
print(f'Image has {dims[2]} color planes each having {dims[0]} rows and {dims[1]} columns')

# Get matrix for each color plane
bluePlane=img[:,:,0]
greenPlane=img[:,:,1]
redPlane=img[:,:,2]

# Show image and each color plane
cv2.imshow("image", img)
cv2.imshow("Blue plane", bluePlane)
cv2.imshow("Green plane", greenPlane)
cv2.imshow("Red plane", redPlane)

plane_r=redPlane

dims=plane_r.shape

mean_r=0.0
for  i in range(dims[0]):
    for j in range(dims[1]):
        mean_r+=plane_r[i][j]
print(f'Mean of plane red is: {mean_r/(dims[0]*dims[1]):.2f}')


# promedio plano azul
plane_b=bluePlane
dims=plane_b.shape

mean_b=0.0
for  i in range(dims[0]):
    for j in range(dims[1]):
        mean_b+=plane_b[i][j]

print(f'mean of plane blue is :{mean_b/(dims[0]*dims[1]):.2f}')
#promedio verde
plane_g=greenPlane
dims=plane_g.shape

mean_g=0.0
for  i in range(dims[0]):
    for j in range(dims[1]):
        mean_g+=plane_g[i][j]
print(f'Mean of plane green is: {mean_g/(dims[0]*dims[1]):.2f}')

resultado = indetifycolor(mean_r, mean_g, mean_b)
print(resultado)

# Wait for key
cv2.waitKey()
cv2. destroyAllWindows()

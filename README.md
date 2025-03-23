# 🛠 Laboratorio 01 - Procesamiento de Imágenes con OpenCV

Este repositorio contiene la solución del Laboratorio 01, donde se implementan varios retos relacionados con el procesamiento de imágenes utilizando OpenCV.

# 📌 Reto 1: Generación de una imagen monocromática

📖 Descripción

Crear una imagen de 640x480 píxeles con un cuadro blanco de 200x200 píxeles en el centro, mientras el resto de la imagen es negra.

La imagen generada es [img_crada.jpg](https://github.com/braVM11504/Laboratorio-01/blob/main/img_crada.jpg) y el pseudocodigo cumpliendo los requisitos [`Reto#1.py`](https://github.com/braVM11504/Laboratorio-01/blob/main/lo.py)

# 🎨 Reto 2: Identificación de colores

Modificar [`test_image.py`](https://github.com/parrado/lab1-1-2025/blob/main/test_image.py)  para calcular el promedio de color de cada imagen y determinar si un automóvil es azul, rojo o amarillo.

Objetivos:

-Calcular los valores promedio de cada plano de color.

-Crear un programa que pida al usuario una imagen ([blue_car.tiff](https://github.com/braVM11504/Laboratorio-01/blob/main/blue_car.jfif), [red_car.tiff](https://github.com/braVM11504/Laboratorio-01/blob/main/red_car.jfif), o [yellow_car.tiff](https://github.com/braVM11504/Laboratorio-01/blob/main/yellow_car.jfif)) e identifique el color del automóvil.

-Implementar la función identifyColor para la identificación de colores.

Pseudocodigo detectando colores cumpliendo los requisitos mencionados en la imagen anterior [`Reto#2.py`](https://github.com/braVM11504/Laboratorio-01/blob/main/punto_2.pt2.py)

# 🔍 Reto 3: Operadores para detección de bordes
Crear un programa que detecte bordes en las siguientes imágenes: [blue_car.jfif](https://github.com/parrado/lab1-1-2025/blob/main/blue_car.jfif), [red_car.jfif](https://github.com/braVM11504/Laboratorio-01/blob/main/red_car.jfif), [yellow_car.jfif](https://github.com/braVM11504/Laboratorio-01/blob/main/yellow_car.jfif) o [emphy.jfif](https://github.com/braVM11504/Laboratorio-01/blob/main/empty.jfif)

Objetivos:

-Implementar la función identifySpot para detectar bordes.

-Utilizar el filtro Canny de OpenCV para realizar la detección.

-Determinar si un puesto de parqueo está ocupado o disponible.

Pseudocodigo cumpliendo requisitos [`Reto#3.py`](https://github.com/braVM11504/Laboratorio-01/blob/main/prueba_3.py)

# 🏗️ Reto 4: Construcción de maqueta  

Para verificar el funcionamiento del **Reto 3**, se debe construir una maqueta que permita probar el sistema en un entorno físico, se recomendo utilizar el programa [`VerCamara.py`](https://github.com/parrado/lab1-1-2025/blob/main/VerCamara.py) 

pseudocodigo modificado para la verificacion del **Reto 3** haciendo uso de camara  [`Reto#4`](https://github.com/braVM11504/Laboratorio-01/blob/main/punto4.py)








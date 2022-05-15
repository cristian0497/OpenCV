import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Creamos una imagen negra (valores cero)
# Matriz de 255x255, 3 canales, 0 cada uno.
img = np.zeros((512,512, 3), np.uint8)

# Dibujamos una línea diagonal azul
# (img, inicio_trazo, fin_trazo, color_rgb, puntos_grosor)
cv.line(img, (0,0), (511,511), (255,0,0), 5)

# Rectangulo verde
cv.rectangle(img, (384, 0), (510,128), (0,255,0), 3 )

# Circle
cv.circle(img, (447, 63), 63, (0,0,255), -1)

# Printing
plt.imshow(img)
plt.show()
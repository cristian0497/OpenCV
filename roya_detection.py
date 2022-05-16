import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Path to jpg image
path = "./images/roya.jpg"

# Read image and print 
img = cv.imread(path)

plt.title("Imagen Original en color BGR")
plt.imshow(img)
plt.show()

#convert Default BGR openCV to RGB space color
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.title("Imagen procesada a color RGB")
plt.imshow(img)
plt.show()

# Convert to HSV format
hsv = cv.cvtColor(img, cv.COLOR_RGB2HSV)

# Define orange range to detect roya
lower = np.array([10,90,110])
upper = np.array([18,255,255])

# Extracting range aplicable pixels
mask = cv.inRange(hsv, lower, upper)
plt.title("Conjunto de píxeles encontrados")
plt.imshow(mask)
plt.show()

# Selecting pixels found
res = cv.bitwise_and(img, img, mask=mask)
plt.title("Imagen real con píxeles identificados del hongo roya")
plt.imshow(res)
plt.show()
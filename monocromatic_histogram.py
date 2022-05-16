import cv2 as cv
from matplotlib import pyplot as plt

path = "./images/home.jpg"
fig = plt.figure()

img = cv.imread(path, 0)
fig.add_subplot(2,2, 1)
plt.title("Gray Scale image Histogram")


# histogram calculating
plt.hist(img.ravel(), 255, [0,255])
fig.add_subplot(2,2, 2)
plt.imshow(img, cmap="gray")
plt.axis('off')
plt.title("Gray Scale image")
plt.plot()



img = cv.imread(path)
# Convert to RGB and print
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
fig.add_subplot(2,2, 3)
#plt.axis('off')
plt.title("RGB histogram")


# Histogram for red, chanel #0
hist = cv.calcHist([img],[0], None, [256], [0,256])
plt.plot(hist, color='red')
plt.xlim([0,255])

# Histogram for green, chanel #1
hist = cv.calcHist([img],[1], None, [256], [0,256])
plt.plot(hist, color='green')
plt.xlim([0,255])

# Histogram for blue, chanel #2
hist = cv.calcHist([img],[2], None, [256], [0,256])
plt.plot(hist, color='blue')
plt.xlim([0,255])

fig.add_subplot(2,2,4)
plt.imshow(img)
plt.axis('off')
plt.title("RGB Image")


plt.show()
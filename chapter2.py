import cv2
import numpy as np

print("Package imported")

img = cv2.imread("resources/lamborghini.jpg")
print(img.shape)

imgCropped = img[0:200, 200:500] # crop an image

imgResize = cv2.resize(img, (300, 200))

cv2.imshow("Image", img)
cv2.imshow("Resized Image", imgResize)

cv2.waitKey(0)

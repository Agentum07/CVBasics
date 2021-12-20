# face detection
 
import cv2 as cv

faceCascade = cv.CascadeClassifier("resources/haarcascade_frontalface_default.xml")
img= cv.imread("resources/lena.jpg")
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

for (x, y, w, h) in faces:
    cv.rectangle(img, (x,y), (x + w, y + h), (0, 0, 0), 5)

cv.imshow("Image", img)
cv.waitKey(0)
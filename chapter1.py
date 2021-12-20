import cv2
import numpy as np

print("Package imported")

# =============================================================================
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# 
# cap.set(3, 640)  # width
# cap.set(4, 480)  # height
# cap.set(10, 100) # brightness
# 
# while True:
#     success, img = cap.read()
#     imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     cv2.imshow("My camera", imgGray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# 
# cv2.destroyWindow("My camera")
# cv2.waitKey(1)
# =============================================================================
# showed webcam

img = cv2.imread("resources/lena.jpg")
kernel = np.ones((5, 5), np.uint8)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
imgCanny = cv2.Canny(img, 150, 200)
imgDilation = cv2.dilate(imgCanny, kernel, iterations = 1)
imgEroded = cv2.erode(imgDilation, kernel, iterations = 1)

# cv2.imshow("Grey Image", imgGray)
# cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilation Image", imgDilation)
cv2.imshow("Eroded Image", imgEroded)

cv2.waitKey(0)

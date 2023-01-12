# Grayscale Blur CannyEdgeDet Erode Dilate
import cv2
import numpy as np
img = cv2.imread('Resources/lena.png')
kernel = np.ones((5, 5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
imgCanny = cv2.Canny(img, 150, 200)  # lower the thresholds finer the edge detection
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)   #adds pixels to the boundary
imgEroded = cv2.erode(imgDilation,kernel, iterations=1)
# imgBlur1 = cv2.GaussianBlur(imgGray, (3, 3), 0)   # the values can only be odd
cv2.imshow('Gray Image', imgGray)
cv2.imshow('Blur image', imgBlur)
cv2.imshow('Canny image', imgCanny)
cv2.imshow('Dilate image', imgDilation)
cv2.imshow('Eroded image', imgEroded)
# cv2.imshow('Blur1 image', imgBlur1)
cv2.waitKey(0)

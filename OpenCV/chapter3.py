#resize and crop
import cv2

img = cv2.imread("Resources/lambo.png")
print(img.shape)
imgResize = cv2.resize(img, (1000, 500))  # w first h second
print(imgResize.shape)  # h first w second

imgCropped = img[0:200, 200:500] # h first w second
cv2.imshow("Lambo", img)
cv2.imshow("lambo resize", imgResize)
cv2.imshow("lambo cropped", imgCropped)
cv2.waitKey(0)

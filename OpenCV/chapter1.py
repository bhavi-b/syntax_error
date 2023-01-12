# Read images video webcam
import cv2
import numpy as np

# print('Package imported')

# img = cv2.imread("Resources/lena.png")

# cv2.imshow("Output", img)
# cv2.waitKey(0) parameter is in mili

# cap=cv2.VideoCapture("Resources/test_video.mp4")
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF==ord('q'):   quits the video if user inputs q
#         break

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # 3 is for width
cap.set(4, 480)  # 4 is for height
# cap.set(10,50)  # adjusts brightness
while True:
    success, img = cap.read()
    cv2.imshow('Video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

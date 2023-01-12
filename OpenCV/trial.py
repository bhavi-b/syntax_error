# import cv2
# import mediapipe as mp
# import numpy as np

# cap = cv2.VideoCapture(0)

# hands =  mp.solutions.hands
# hands = hands.Hands(
#     min_detection_confidence=0.5,
#     min_tracking_confidence=0.5)
# hands_mesh = hands.Hands(static_image_mode = True,min_detection_confidence=0.7)
# draw = mp.solutions.drawing_utils


# while True:
#     success ,img = cap.read();
#     rgb =cv2.cvtColor(cv2.flip(img , 1) , cv2.COLOR_BGR2RGB)
#     results = hands.process(img)
#     image_height, image_width, _ = img.shape

#     op = hands_mesh.process(rgb)

#     if op.multi_hand_landmarks:
#         for i in op.multi_hand_landmarks:
#             draw.draw_landmarks(img , i , hands.HAND_CONNECTIONS )

#     if results.multi_hand_landmarks:
#       for hand_landmarks in results.multi_hand_landmarks:
#         for ids, landmrk in enumerate(hand_landmarks.landmark):
#             cx , cy = landmrk.x * image_width  , landmrk.y*image_height
#             print (cx , " , " , cy)

#     cv2.imshow("Window", img)

#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         cv2.destroyAllWindows()
#         break


import cv2
import mediapipe as mp
import pyautogui
#import time

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

#time.sleep(5)
# For webcam input:
#time.sleep(5)
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue
        i = 1
        cxn = 0
        cyn = 0
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

        image.flags.writeable = False
        results = hands.process(image)
        image_height, image_width, _ = image.shape
        # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:

                for ids, landmrk in enumerate(hand_landmarks.landmark):
                    # print(ids, landmrk)
                    cx, cy = landmrk.x * image_width, landmrk.y * image_height
                    cx = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width)
                    cy = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height)
                    if (abs(cxn - cx) >= 100 | abs(cyn - cy) >= 75):
                        print(cx, cy)
                        pyautogui.moveTo(cx, cy)
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        cv2.imshow('MediaPipe Hands', image)
        if cv2.waitKey(5) & 0xFF == 'q':
            break
cap.release()
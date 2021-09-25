# for right only

import cv2
import numpy as np
import mediapipe as mp
import time
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(0.8)
prevTime = 0

cap = cv2.VideoCapture(0)
tipIds = [8, 12, 16]


while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    if hands:
        lmList = hands[0]['lmList']
        fingers = []

        q1 = lmList[20][1]
        q2 = lmList[18][1]
        if q1 < q2:
            fingers.append(1)
        else:
            fingers.append(0)



        s1 = lmList[4][0]
        s2 = lmList[3][0]
        if s1 > s2:
            fingers.append(1)
        else:
            fingers.append(0)

        for i in tipIds:
            x1 = lmList[i][0]
            x2 = lmList[i-2][0]
            if x1 < x2 :
                fingers.append(0)
            else:
                fingers.append(1)

        totalFingers = fingers.count(1)

        print(totalFingers)
        cv2.rectangle(img,(100,50),(200,100),(0,255,0),cv2.FILLED)
        cv2.putText(img,str(totalFingers),(130,100),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)






    currTime = time.time()
    fps = 1/(currTime-prevTime)
    prevTime = currTime

    cv2.putText(img, f'Fps: {int(fps)}', (380, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)


    cv2.imshow("Image", img)

    cv2.waitKey(1)
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import cvzone

cap = cv2.VideoCapture(0)

detector = HandDetector(detectionCon=0.8, maxHands=1)
# function
x = [300, 245, 200, 170, 100, 257, 80, 112, 145, 130, 103, 93, 80, 75, 70, 60]
y = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

coff = np.polyfit(x, y, 2)

while True:
    success, img = cap.read()
    # print(img.shape)

    hands = detector.findHands(img, draw=False)

    if hands:
        lmList = hands[0]['lmList']

        x1, y1 = lmList[5]
        x2, y2 = lmList[17]
        x, y, w, h = hands[0]['bbox']
        distance = np.sqrt(((y2 - y1) ** 2 + (x2 - x1) ** 2))
        A, B, C = coff
        distanceCm = A * (distance ** 2) + B * distance + C
        # print(distanceCm)
        cvzone.putTextRect(img, f'{int(distanceCm)} cm', (x + 5, y - 50))
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 3)
        if distanceCm <= 70:
            cv2.putText(img, "Hand Detected", (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 5)
            if distanceCm < 68:
                break
        else:
            cv2.putText(img, "Hand Not Detected", (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 5)







    cv2.imshow("Window", img)
    cv2.waitKey(1)

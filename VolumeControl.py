import cv2
import numpy as np
import time
import mediapipe as mp
import pycaw
from cvzone.HandTrackingModule import HandDetector
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


cap = cv2.VideoCapture(0)
detector = HandDetector(0.8)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
#volume.GetMute()
#volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
vol = 0
volBar = 300

#print(volume.GetVolumeRange())
minVol = volRange[0]
maxVol = volRange[1]

prevTime = 0
volPer = 0
while True:
    success, img = cap.read()




    hands, img = detector.findHands(img)
    if hands:
        lmList = hands[0]['lmList']

        x1, y1 = lmList[4][0], lmList[4][1]

        x2, y2 = lmList[8][0], lmList[8][1]
        cx, cy = (x1+x2)//2 , (y1+y2)//2

        cv2.circle(img,(x1,y1),10,(0,255,0),cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (0, 255, 0), cv2.FILLED)
        cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)

        cv2.line(img, (x1,y1),(x2,y2),(0,255,0),3)
        length, info = detector.findDistance((x1,y1),(x2,y2))
        #print(length)
        #Convert volume into hand range

        vol = np.interp(length,[10,130],[minVol,maxVol])
        volBar = np.interp(length,[10,130],[300,100])
        volPer = np.interp(length,[10,130],[0,100])
        volume.SetMasterVolumeLevel(vol, None)

        if length < 25:
            cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)


    cv2.rectangle(img, (100,100), (80,300), (0,255,0),3)
    cv2.rectangle(img, (100, int(volBar)), (80, 300), (0,255, 0), cv2.FILLED)
    cv2.putText(img, f'{int(volPer)} %', (70, 350), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)


    currTime = time.time()
    fps = 1 / (currTime - prevTime)
    prevTime = currTime

    cv2.putText(img, f'Fps:{int(fps)}', (60, 60), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
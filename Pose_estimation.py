import cv2
import mediapipe as mp
import numpy as np
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()
cap = cv2.VideoCapture("Resources/video3.mp4")
prevTime = 0

while True:
    success, img = cap.read()
    h,w,c = img.shape
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    p = results.pose_landmarks
    if p:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
    point = []
    for i,lm in enumerate(results.pose_landmarks.landmark):

        cx, cy = int(lm.x*w), int(lm.y*h)
        point.append([cx,cy])

        cv2.circle(img,(cx,cy),10,(255,0,0),cv2.FILLED)


    new_h = h//3
    new_w = w//3
    resizeImg = cv2.resize(img,(new_w,new_h))
    currTime = time.time()
    fps = 1/(currTime-prevTime)
    prevTime = currTime



    cv2.putText(resizeImg,str(int(fps)),(60,60),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),4)


    cv2.imshow("Video",resizeImg)
    cv2.waitKey(1)
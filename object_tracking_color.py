import numpy as np
import  matplotlib.pyplot as plt
import cv2
cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)


    lower_blue=np.array([110,50,50])
    upper_blue=np.array([130,255,255])

    mask=cv2.inRange(hsv,lower_blue,upper_blue)

    res=cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("Original Image",frame)

    cv2.imshow("Color",mask)

    cv2.imshow("Threshold",res)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break



cap.release()
cv2.destroyAllWindows()
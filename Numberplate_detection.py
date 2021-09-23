import cv2
import numpy as np
import matplotlib.pyplot as plt

count = 0

nPlateCascade = cv2.CascadeClassifier("Resources/haarcascade_russian_plate_number.xml")

img = cv2.imread("Resources/car5.jbg.jpg")
#imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#print(img.shape)
cv2.resize(img,(500,500))

numberPlates = nPlateCascade.detectMultiScale(img, 1.1, 4)
for (x, y, w, h) in numberPlates:

    cv2.rectangle(img,(x,y),(x+w,y+h), (255,0,0),2)
    cv2.putText(img, "Number Plate", (x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (255,0,255))
    imgRoi = img[y:y+h, x:x+w]
    cv2.imshow("Roi", imgRoi)

cv2.imshow("Original Image", img)
cv2.waitKey(1500)


cv2.imwrite("Resources/Scanned/NoPlate_"+str(count)+".jpg", imgRoi)

cv2.rectangle(img,(x,y-150),(x+w,y+h-170),(0,255,0),cv2.FILLED)
cv2.putText(img,"Image Scanned",(x+20,y+h-220),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,255))
cv2.imshow("Result",img)

count += 1

cv2.waitKey(0)
import cv2
import numpy as np
import matplotlib.pyplot as plt


faceDetection = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

img = cv2.imread("Resources/s3.jpg")
cv2.resize(img,(200,300))

faces = faceDetection.detectMultiScale(img, 1.1, 4)
for (x, y, w, h) in faces:

    cv2.rectangle(img,(x,y),(x+w,y+h), (255,0,0),2)




cv2.imshow("Original Image", img)

cv2.waitKey(0)

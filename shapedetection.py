import cv2
import numpy as np
def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        cv2.drawContours(imgContour,  cnt, -1,  (255, 0, 0),2)
        peri = cv2.arcLength(cnt, True)
        print(peri)
        approx = cv2.approxPolyDP(cnt, 0.02*peri,True)
        print(len(approx))
        objCor = len(approx)
        x, y, w, h = cv2.boundingRect(approx)

        if objCor == 3:
            objectType = "Tri"
        elif objCor==4:
            aspectRatio = w/float(h)
            if aspectRatio >0.95 and aspectRatio <1.05:
                objectType = "Square"
            else:
                objectType = "Rect"
        elif objCor >4:
            objectType ="Circle"
            
        else:objectType = "None"
        cv2.rectangle(imgContour,(x,y),(x+w, y+h),(0,0,255),2)
        cv2.putText(imgContour, objectType, ( x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,255,0),2)



img = cv2.imread("Resources/shapes.png")
print(img.shape)

q = cv2.resize(img, (300, 200))
imgContour = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 100, 300)
getContours(imgCanny)

cv2.imshow("Original image", img)
cv2.imshow("Gray image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Edge detection", imgCanny)
cv2.imshow("Contour Image", imgContour)
cv2.waitKey(0)
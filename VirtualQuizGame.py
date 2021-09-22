import cv2
import csv
from cvzone.HandTrackingModule import HandDetector
import cvzone
import time

widthFrame = 1280
heightFrame = 720
cap = cv2.VideoCapture(0)
cap.set(3, widthFrame)
cap.set(4, heightFrame)
detector = HandDetector(detectionCon=0.8)


class MCQ():
    def __init__(self, data):
        self.question = data[0]
        self.choice1 = data[1]
        self.choice2 = data[2]
        self.choice3 = data[3]
        self.choice4 = data[4]
        self.answer = int(data[5])

        self.userAnswer = None

    def update(self, cursor, bboxs):

        for x, bbox in enumerate(bboxs):

            x1, y1, x2,y2 = bbox
            if x1 < cursor[0] < x2 and y1 < cursor[1] < y2:
                self.userAnswer = x + 1
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),cv2.FILLED)




#Import csv file data
pathCSV = 'Mcq.csv'
with open(pathCSV,newline="\n") as f:
    reader = csv.reader(f)
    dataAll = list(reader)[1:]
#print(len(dataAll))
#Create Object for each mcq
mcqlist = []
for q in dataAll:
    mcqlist.append(MCQ(q))

#print(len(mcqlist))


qNo = 0
qTotal = len(dataAll)


while True:
    success, img = cap.read()
    img = cv2.flip(img,1)
    hands, img = detector.findHands(img,flipType=False)

    if qNo<qTotal:

        mcq = mcqlist[qNo]

        img, bbox = cvzone.putTextRect(img,mcq.question,[60,100],1,1,offset=20,border=3)
        img, bbox1 = cvzone.putTextRect(img, mcq.choice1, [60, 200], 1, 1, offset=20, border=3)
        img, bbox2 = cvzone.putTextRect(img, mcq.choice2, [230, 200], 1, 1, offset=20, border=3)
        img, bbox3 = cvzone.putTextRect(img, mcq.choice3, [60, 300], 1, 1, offset=20, border=3)
        img, bbox4 = cvzone.putTextRect(img, mcq.choice4, [230, 300], 1, 1, offset=20, border=3)

        if hands:
            lmList = hands[0]['lmList']
            cursor = lmList[8]
            length, info = detector.findDistance(lmList[8], lmList[12])
            #print((length))

            if length < 15:
                mcq.update(cursor,[bbox1,bbox2,bbox3,bbox4])
                print(mcq.userAnswer)
                if mcq.userAnswer is not None:

                    time.sleep(0.6)
                    qNo +=1

    else:
        score = 0
        for mcq in mcqlist:
            if mcq.answer == mcq.userAnswer:

                score += 1
        score = round((score/qTotal)*100, 2)
        img, _ = cvzone.putTextRect(img, 'Quiz Completed', [40,150], 1, 1, offset=10,border=2)
        img, _ = cvzone.putTextRect(img, f'Your Score: {score}%', [280, 150], 1, 1, offset=10,border=2)

    #Draw Progress Bar
    Barvalue = 30 +(530//qTotal)*qNo
    cv2.rectangle(img,(30,400),(Barvalue,430),(0,255,0),cv2.FILLED)
    cv2.rectangle(img,(30,400),(560,430),(255,0,255),3)
    img, _ = cvzone.putTextRect(img, f'{round((qNo/qTotal)*100)}%',[580,425],1,1,offset=4)

    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


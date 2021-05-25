#virtual paint using green color

import cv2
import numpy as np

def getContours(mask,points):
    for i in range(len(points)-1):
        coordinates_1=points[i]
        coordinates_2=points[i+1]
        cv2.line(img,(coordinates_1[0],coordinates_1[1]),(coordinates_2[0],coordinates_2[1]),(0,255,0),6)
    # for i in points:
    #     cv2.circle(img, (i[0], i[1]), 4, (0, 255, 0), 15)
    #     #print(len(points))
    contours,hierarchy=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        perimeter=cv2.arcLength(cnt,True)
        area=cv2.contourArea(cnt)

        if area>8000:
            cv2.drawContours(img, cnt, -1, (255, 255, 255), 1)
            approx=cv2.approxPolyDP(cnt,0.02*perimeter,True)
            x,y,width,height=cv2.boundingRect(approx)
            coordinates=[x+(width//2),y+(height//2)]
            points.append(coordinates)

video=cv2.VideoCapture(1)
video.set(10,130)
video.set(3,2220)
video.set(4,720)
points=[]
points2=[]
points3=[]
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (int(video.get(3)),  int(video.get(4))))
while(True):
    success,img=video.read()
    if success==True:
        
        out.write(img)

    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #green color
    lower2 = np.array([29, 48, 112])
    upper2 = np.array([73, 237, 255])
    mask2 = cv2.inRange(imgHSV, lower2, upper2)
    getContours(mask2, points2)
    Result=cv2.bitwise_and(img,img,mask=mask2)



    #cv2.imshow('mask', mask2)
    #cv2.imshow('mask2',Result)
    cv2.putText(img, 'Press Space to exit....', (0, 690), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (0, 0, 255))
    cv2.moveWindow('Webcam', 20, 20)
    cv2.imshow('Webcam',img)


    if cv2.waitKey(1) & 0xFF==32:
        break

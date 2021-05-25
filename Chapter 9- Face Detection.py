import cv2
import numpy as np

faceCascade=cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')
img=cv2.imread('Resources/photo-1531844251246-9a1bfaae09fc.jfif')
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=faceCascade.detectMultiScale(imgGray,1.1,4)
for (x,y,width,height) in faces:
    cv2.rectangle(img,(x,y),(x+width,y+height),(0,0,255),2)

cv2.imshow("Original Photo",img)
cv2.waitKey(0)
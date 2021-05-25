import cv2
import numpy as np

def getContours(img):
    contours, hierarchy= cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        print(area)
        if area>0:
            cv2.drawContours(imgContour, cnt, -1, (0, 0, 255),1)
            perimeter=cv2.arcLength(cnt,True)
            print(perimeter)
            approx=cv2.approxPolyDP(cnt,0.02*perimeter,True)
            print(len(approx))
            objCorners=len(approx)
            x,y,width,height=cv2.boundingRect(approx)

            if objCorners==3:
                objectType='Triangle'
            elif objCorners==4:
                if(width!=height):
                    objectType='Rectangle'
                else:
                    objectType='Square'
            elif objCorners>10:
                objectType='Heart'
            else:
                objectType='Circle'


            cv2.rectangle(imgContour, (x, y), (x + width, y + height), (0, 255, 0), 2)
            cv2.putText(imgContour,objectType,(x+(width//2)-10,y+(height//2)-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)

img=cv2.imread('Resources/Screenshot (23).png')
imgContour =img.copy()
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(7,7),2)
imgCanny=cv2.Canny(imgBlur,130,130)
imgBlank=np.zeros_like(img)

imgTotal=cv2.hconcat([imgGray,imgBlur,imgCanny])
cv2.imshow('Shapes',img)
cv2.imshow('Shapes(Blur and Gray)',imgTotal)
#cv2.imshow('Blank',imgBlank)
getContours(imgCanny)
cv2.imshow('Contout Image  :',imgContour)



cv2.waitKey(0)
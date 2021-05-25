import cv2
import numpy as np

def empty(a):
    pass

#trackbar initalization
cv2.namedWindow('Trackbars')
cv2.resizeWindow('Trackbars',640,360)
cv2.createTrackbar('Hue Min','Trackbars',16,179,empty)
cv2.createTrackbar('Hue Max','Trackbars',179,179,empty)
cv2.createTrackbar('Sat Min','Trackbars',210,255,empty)
cv2.createTrackbar('Sat Max','Trackbars',255,255,empty)
cv2.createTrackbar('Val Min','Trackbars',79,255,empty)
cv2.createTrackbar('Val Max','Trackbars',255,255,empty)

while True:
    img=cv2.imread("Resources/download.jpg")
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min=cv2.getTrackbarPos('Hue Min','Trackbars')
    h_max = cv2.getTrackbarPos('Hue Max', 'Trackbars')
    s_min = cv2.getTrackbarPos('Sat Min', 'Trackbars')
    s_max = cv2.getTrackbarPos('Sat Max', 'Trackbars')
    v_min = cv2.getTrackbarPos('Val Min', 'Trackbars')
    v_max = cv2.getTrackbarPos('Val Max', 'Trackbars')
    #print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(imgHSV,lower,upper)
    imgResult=cv2.bitwise_and(img,img,mask=mask)

    #cv2.imshow('Output',imgHSV)
    cv2.imshow('Mask',mask)
    #cv2.imshow('Result', imgResult)
    final_image=cv2.vconcat([img,imgResult,imgHSV])
    final_image=cv2.resize(final_image,(640,780))
    cv2.imshow('Final Image',final_image)
    cv2.waitKey(1)
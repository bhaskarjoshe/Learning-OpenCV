import cv2
import numpy as np

img=cv2.imread('Resources/330px-Lenna_(test_image).png')
kernel=np.ones(( 5,5),np.uint8)
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#converting image to GrayScale
imgBlur=cv2.GaussianBlur(imgGray,(7,7),0)#gaussian blur
imgCanny=cv2.Canny(img,100,150) #edge detection
imgDialation =cv2.dilate(imgCanny,kernel,iterations=1) #to thicken edge of our therholded image
imgErroded=cv2.erode(imgDialation,kernel,iterations=1) #to thicken the edges
#cv2.imshow('Output Gray',imgGray)
#cv2.imshow('Output Blur',imgBlur)
#cv2.imshow('Output Edges',imgCanny)
cv2.imshow('Output Dialation',imgDialation)
cv2.imshow('Output Eroded',imgErroded)
cv2.waitKey(0)
import cv2
import numpy as np

img=cv2.imread('Resources/330px-Lenna_(test_image).png')
#using numpy
imgHor=np.hstack((img,img))
imgVer=np.vstack((imgHor,imgHor))
cv2.imshow('Horizontal',imgHor)
cv2.imshow('Vertival',imgVer)
cv2.waitKey(0)
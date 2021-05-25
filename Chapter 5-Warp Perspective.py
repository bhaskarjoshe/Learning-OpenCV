import cv2 as cv
import numpy as np

img=cv.imread('Resources/Hanafuda-playing-cards-koi.png')
width,height=250,350
points_coordinates=np.float32([[446,153],[577,78],[589,339],[721,262]])
points_positions=np.float32([[0,0],[width,0],[0,height],[width,height]])
kernel=np.ones(( 5,5),np.uint8)
transformation_martrix=cv.getPerspectiveTransform(points_coordinates,points_positions)
imgOutput=cv.warpPerspective(img,transformation_martrix,(width,height))
imgOutput=cv.resize(imgOutput,(350,450))
imgOutput=cv.dilate(imgOutput,kernel,iterations=2)
imgOutput=cv.erode(imgOutput,kernel,iterations=6)
#cv.imshow('',img)
cv.imshow('Output',imgOutput)
cv.waitKey(0)
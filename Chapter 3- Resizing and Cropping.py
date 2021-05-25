import cv2
import numpy as np

img=cv2.imread('Resources/lambo.png')
print(img.shape)
imgResize=cv2.resize(img,(1240,520))#resizing image
imgCropped =img[255:380,150:275]

#cv2.imshow("Original Image",img)
cv2.imshow("Cropped Image",imgCropped)
#cv2.imshow('Resize Image',imgResize)

imgCroppedResize=cv2.resize(imgCropped,(400,400))

cv2.imshow('Resized Cropped Image',imgCroppedResize)
cv2.waitKey(0)


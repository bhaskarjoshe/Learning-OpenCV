import cv2
import numpy as np
'''#COLORING AN IMAGE
img=np.zeros((512,512,3),np.uint8)
print(img)
img[200:300,200:300]=0,0,255
'''
# creating shapes
img=np.zeros((512,512,3))
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),2)
cv2.rectangle(img,(150,100),(350,400),(0,0,150),cv2.FILLED)
cv2.circle(img,(250,250),100,(255,255,255),cv2.FILLED,5)
#text on image
cv2.putText(img,'OPEN CV',(200,250),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255),2)
cv2.imshow('',img)

cv2.waitKey(0)
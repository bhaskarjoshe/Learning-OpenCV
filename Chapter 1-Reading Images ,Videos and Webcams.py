import cv2
'''
print('Package imported')
img=cv2.imread('Resources/330px-Lenna_(test_image).png')
cv2.imshow("output",img)
cv2.waitKey(0)'''

'''video= cv2.VideoCapture("Resources/videoplayback.mp4")
while(True):f
    success,img=video.read()
    cv2.imshow('Video',img)
    if cv2.waitKey(1) & 0xFF==ord('f'):
        break'''
video= cv2.VideoCapture(0)
video.set(3,1400)
video.set(4,480)
video.set(10,150)
while(True):
    success,img=video.read()
    cv2.imshow('Video',img)
    if cv2.waitKey(1) & 0xFF==ord('f'):
        break
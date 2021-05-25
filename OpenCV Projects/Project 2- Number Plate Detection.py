import cv2

count=0
cascade=cv2.CascadeClassifier('Resources/haarcascade_russian_plate_number.xml')
video= cv2.VideoCapture(0)
video.set(3,1400)
video.set(4,480)
video.set(10,150)
while(True):
    success,img=video.read()
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    numberplates=cascade.detectMultiScale(imgGray,1.1,4)

    for (x,y,w,h) in numberplates:
        area=w*h
        if area>500:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255))
            cv2.putText(img,'Number Plate',(x,y-5),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(0,0,255),2)
            imgReg=img[y:y+h,x:x+w]
            cv2.imshow('Plate', imgReg)
    cv2.imshow('Video',img)

    if cv2.waitKey(1) & 0xFF==32:
        cv2.imwrite('Resources/Scan/NoPlate_'+str(count)+'.jpg',imgReg)
        cv2.rectangle(img,(0,200),(640,400),(0,255,0),cv2.FILLED)
        cv2.putText(img,'scan saved',(150,265),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2)
        cv2.imshow('Video',img)
        cv2.waitKey(500)
        count+=1
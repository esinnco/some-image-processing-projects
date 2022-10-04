import numpy as np
import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier("haarcascade_eye.xml")

cap=cv2.VideoCapture(0)

while True:
    ret, img= cap.read()
    gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray , 1.3 , 5)

    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y) , (x+w,y+h) , (255,102,102) , 4 ) 
        roi_gray=gray[y:y+h , x:x+w]
        roi_color=img[y:y+h , x:x+w]

        eyes= eye_cascade.detectMultiScale(roi_gray)
        i=0

        for(ax,ay,aw,ah) in eyes:
            i+=1
            cv2.rectangle(roi_color , (ax,ay) , (ax+aw,ay+ah), (255,128,0) ,2)
            if i==2:
                break
        
    cv2.imshow("cam", img)
    k=cv2.waitKey(10) & 0Xff

    if k==27:
         break

cap.release()
cv2.destroyAllWindows()


import cv2
import numpy

img= cv2.imread("resim.jpg")
face_cascade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
gray_scale= cv2.cvtColor(img,  cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_scale,1.2,5)

for(x,y,w,h) in faces:
    cv2.rectangle(img, (x,y) , (x+w,y+h) , (178,102,255), 4)
    
cv2.imshow("baslik", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


    
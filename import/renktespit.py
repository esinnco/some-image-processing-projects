import cv2
import numpy as np

cap=cv2.VideoCapture(0 ,cv2.CAP_DSHOW )

while True:
    ret,frame = cap.read()
    
    if ret == False:
        break
    
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_green = np.array([45,100,50])
    upper_green = np.array([75,255,255])
    green_mask = cv2.inRange(hsv_frame , lower_green , upper_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)
    

    lower_blue = np.array([100,150,0])
    upper_blue = np.array([140,255,255])
    blue_mask= cv2.inRange(hsv_frame, lower_blue , upper_blue)
    blue = cv2.bitwise_and(frame, frame , mask=blue_mask)



    cv2.imshow("camera", frame)
    cv2.imshow("green mask", green_mask)
    cv2.imshow("green" , green)
    cv2.imshow("blue mask", blue_mask)
    cv2.imshow("blue", blue)
    if cv2.waitKey(1) & 0xff == ord("q"):
        break
     
    
cap.release()
cv2.destroyAllWindows()

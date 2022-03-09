
# Importing all required packages
import cv2
import numpy as np



face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('smile_cascade.xml')


cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces:
        roi  = frame[y:y+h,x:x+w]
        graySmile = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
        smileS = smile_cascade.detectMultiScale(graySmile, 1.3, 5)
        for (k,l,m,n) in smileS:
            frame = cv2.rectangle(frame,(k,l),(k+m,l+n),(0,0,255),2)           
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("face",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
    # Saving the image


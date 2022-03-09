# Importing all required packages
import cv2
import numpy as np
import random
count_left = 0
count_right = 0



def midPoint(x,y,w,h):
    x = x+w/2
    y = y+h/2
    return x,y

def drawRectangle(x,y,frame):
    colorName = ["mavi","yesil","kirmizi","sari","pembe","siyah","turuncu","mor","kahverengi"]
    rnd = random.randint(0,len(colorName)-1)
    cv2.rectangle(frame,(x-10,y-80),(x+w+10,y-10),(0,255,0),3)
    cv2.putText(frame,colorName[rnd],(int(x+w/2-40),y-40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255))

# Read in the cascade classifiers for face and eyes
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')



cap = cv2.VideoCapture(0)
while True:

    ret,frame = cap.read()
    frame = cv2.flip(frame,1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        # cv2.rectangle(image, start_point, end_point, color, thickness)
        #frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        drawRectangle(x, y, frame)
        if (x+w/2<200) and (y+h/2-40<50):
            count_left = count_left +1 
            
            
        elif (x+w/2>440) and (y+h/2-40<50):
            count_right = count_right +1
    cv2.putText(frame, str(count_left), (0,180), cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (0, 0, 255), 1, cv2.LINE_AA)        
    cv2.putText(frame, str(count_right), (0,140), cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (0, 0, 255), 1, cv2.LINE_AA)       
    print(f"sol: {count_left}")
    print(f"sag: {count_right}")            
    cv2.imshow("face",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
    # Saving the image


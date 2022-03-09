
# Importing all required packages
import cv2
import numpy as np

import time

# Read in the cascade classifiers for face and eyes
eye_cascade = cv2.CascadeClassifier(r'C:\Users\frknl\Desktop\furk\classifier\cascade.xml')

prev_frame_time = 0
new_frame_time = 0
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)
while True:

    ret,frame = cap.read()
    #frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    new_frame_time = time.time()
    fps = 1/(new_frame_time-prev_frame_time)
    prev_frame_time = new_frame_time
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fps = int(fps)
    fps = str(fps)
    #faces = eye_cascade.detectMultiScale(gray, 1.3, 5)

    #for (x,y,w,h) in faces:
        # cv2.rectangle(image, start_point, end_point, color, thickness)
        #frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        
    cv2.putText(frame, fps, (7, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (100, 255, 0), 3, cv2.LINE_AA)
    cv2.imshow("face",frame)
    if cv2.waitKey(500) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
    # Saving the image


import cv2
import numpy as np
face_cascade = cv2. CascadeClassifier ('haarcascade_frontalface_default.xml')
webcam = cv2.VideoCapture(0)

while True:
  ret , img = webcam.read()
  gray = cv2. cvtColor (img, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray,1.5,4)

  for (x,y,w,h) in faces:
     cv2. rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)
   
  cv2. imshow("Face detection", img)

  if cv2.waitKey (1) & 0xFF == ord('x'):
    break

webcam.release()
cv2. destroyAllWindows ()
# Python program to illustrate
# saving an operated video
from threading import Thread

# organize imports
import numpy as np
import cv2

# This will return video from the first webcam on your computer.
#cap = cv2.VideoCapture(r'C:\Users\neelr_rzc8ain\PycharmProjects\CGCProject\vid3.mp4')
cap = cv2.VideoCapture(r'C:\Users\neelr_rzc8ain\Desktop\img\vid6.mp4')
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('mysite/media/output.avi', fourcc, 20.0, (640, 480))
#out = cv2.VideoWriter('mysite/media/output.avi', -1, 20.0, (640,480))
fps = cap.get(cv2.CAP_PROP_FPS)
width  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)   # float
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float
out = cv2.VideoWriter('mysite/media/output.mp4', -1,fps, (int(width), int(height)))

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# loop runs if capturing has been initialized.
while True:
    # Read the frame
    ret, img = cap.read()

    # Convert to grayscale
    if ret:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)


            #cv2.imshow('Frame', temp)
        # Display
        out.write(img)
        cv2.imshow('Original', img)
        #cv2.imshow('Frame', gray)
        # Stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff
        if k==27:
            break
    else:
        print('video not found')
        break
# Release the VideoCapture object
print('we are done! ')
cap.release()

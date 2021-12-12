import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#https://www.youtube.com/watch?v=Xygk7UjKM2g
# To capture video from webcam.
#cap = cv2.VideoCapture(r'C:\Users\neelr_rzc8ain\PycharmProjects\CGCProject\vid1.mp4')
cap = cv2.VideoCapture(r'C:\Users\neelr_rzc8ain\Desktop\img\vid2.mp4')
print ( type(cap) )
# To use a video file as input
# cap = cv2.VideoCapture('filename.mp4')

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
        # Display
        cv2.imshow('img', img)

        # Stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff
        if k==27:
            break
    else:
        print('video not found')
        break
# Release the VideoCapture object
cap.release()

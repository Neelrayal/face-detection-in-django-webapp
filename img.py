import cv2

#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


img = cv2.imread(r'C:\Users\neelr_rzc8ain\Desktop\img\7.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5) #1.3 5

print('No of faces detected', len(faces))
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    #roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

cv2.namedWindow('finalImg', cv2.WINDOW_NORMAL)
cv2.imshow("finalImg",img)

cv2.waitKey(0)
cv2.destroyAllWindows()


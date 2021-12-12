import cv2

#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
import time
start_time = time.time()


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

original_img = cv2.imread(r'C:\Users\neelr_rzc8ain\Desktop\img\7.jpg')
gray = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5) #1.3 5


for (x,y,w,h) in faces:
    img = cv2.rectangle(original_img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    cv2.imwrite('mysite/media/new_img.jpg', img )


saved_img = cv2.imread( 'mysite/media/new_img.jpg' )
#cv2.imshow('img',img)
cv2.namedWindow('finalImg', cv2.WINDOW_NORMAL)
cv2.imshow("finalImg",original_img)
print('No of faces detected', len(faces))
#cv2.imshow('saved image', saved_img)

print("--- %s seconds ---" % (time.time() - start_time))

cv2.waitKey(0)
cv2.destroyAllWindows()


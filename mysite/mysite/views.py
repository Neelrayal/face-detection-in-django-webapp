from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.conf.urls.static import static

import cv2
dir_path = 'C:/Users/neelr_rzc8ain/PycharmProjects/CGCProject/mysite'
def index(request):
    return HttpResponse('hello world')

def video(video_sent):
    video_sent = dir_path + video_sent

    cap = cv2.VideoCapture(video_sent)
    print('type of video: ', type(cap))
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    #out = cv2.VideoWriter('mysite/media/output.avi', fourcc, 20.0, (640, 480))
    #out = cv2.VideoWriter('mysite/media/output.avi', -1, 20.0, (640,480))
    fps = cap.get(cv2.CAP_PROP_FPS)
    width  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)   # float
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float
    out = cv2.VideoWriter(dir_path + '/media/new_vid.mp4', -1,fps, (int(width), int(height)))

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # loop runs if capturing has been initialized.
    count = 0
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

            count += len(faces)

                #cv2.imshow('Frame', temp)
            # Display
            out.write(img)
            #cv2.imshow('Original', img)
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
    return count



def getfaces(img_sent):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    print('image sent is: ', img_sent)
    #image sent is:  /media/7_HTatdkY.jpg
    img_sent = dir_path + img_sent
    '''
    cur_img = cv2.imread(img_sent)
    cv2.namedWindow('current image', cv2.WINDOW_NORMAL)
    cv2.imshow('current image', cur_img)
    '''
    original_img = cv2.imread(img_sent)

    print( 'type of org image: ', type(original_img) )
    gray = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5) #1.3 5

    for (x,y,w,h) in faces:
        img = cv2.rectangle(original_img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        cv2.imwrite(dir_path + '/media/new_img.jpg', img )
    '''
    img2 = cv2.imread(dir_path + '/media/new_img.jpg')
    cv2.namedWindow('updated image', cv2.WINDOW_NORMAL)
    cv2.imshow('updated image', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    '''
    return (len(faces))

def upload(request):
    if request.method == 'POST': # and request.FILES['upload']
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        print('file_url is: ', file_url)
        if 'img' in request.POST:
            no_of_faces = getfaces(file_url)
            saved_img_url = fss.url(dir_path + '/media/new_img.jpg')
            ls = [saved_img_url, no_of_faces ]
            #return render(request, 'afterupload.html', {'file_url' : saved_img_url})
            return render(request, 'afterupload.html', {'file_url': ls}  )
        else:

            no_of_faces = video(file_url)
            #no_of_faces = 200
            saved_vid_url = fss.url(dir_path + '/media/new_vid.mp4')
            ls = [ saved_vid_url , no_of_faces ]

            return render(request, 'afterUploadVid.html', {'file_url': ls})
        #return render(request, 'upload.html', {'file_url': file_url})
    return render(request, 'upload.html')

def checking(request):
    temp = dir_path + '/media/new_img.jpg'
    print('path is: ', temp)
    x = cv2.imread(temp)
    cv2.namedWindow('image in checking', cv2.WINDOW_NORMAL)
    cv2.imshow('image in checking', x)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return HttpResponse('hello checking')


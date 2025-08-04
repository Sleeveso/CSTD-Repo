import cv2 as cv



faceCascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv.VideoCapture(0) # webcam is 0
cap.set(3, 640) # for setting the size for 'cap' cap.set(width, 640) 3 is the id number for width
cap.set(4, 480) # for setting the size for 'cap' cap.set(hight, 640) 4 is the id number for height
cap.set(10, 100) # 10 is the id number for brightness

while True:
    isTrue, img = cap.read()
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray,1.1,4)
    for (x,y,w,h) in faces:
        cv.rectangle(img,(x,y), (x+w,y+h), (255,0,0), 2) # this puts a bounding rectange(around things detected). cv.rectangle(img,(initial point), (diagonal point), (color), thickness)

    cv.imshow("video", img)
    if cv.waitKey(1) & 0xff == ord("q"):
        break


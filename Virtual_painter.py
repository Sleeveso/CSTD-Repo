import cv2 as cv
import numpy as np
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# Project 1: Virtual paint

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

frameWidth = 640
frameHeight = 480

cap = cv.VideoCapture(0)
cap.set(3, frameWidth ) 
cap.set(4, frameHeight)
cap.set(10, 130) 


# by using the color detection program, u acan find the cordinates (max and min of the trackbars then import them each for a specific color)

myColors = [
            [6,163,0,179,255,240]]

# [5,107,0,19,255,255],
#             [133,56,0,159,156,255],
#             [57,76,0,100,255,255],

# then u add the color u cant to display for each coordinates detected_ blue has already been provided 
myClorValues = [
                [255,0,0]]

# [51,153,255],
#                 [255,0,255],
#                 [0,255,0],

myPoints = [] #[x, y, colorid]


def findColor(img,myColors,myClorValues):
    imgHsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    count = 0
    newPoint = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv.inRange(imgHsv, lower, upper)
        x,y = getContours(mask)
        cv.circle(imgResult,(x,y), 10, myClorValues[count],cv.FILLED)
        if x != 0 and y != 0:
            newPoint.append([x,y,count])
        count += 1
        cv.imshow(str(color[0]), mask)
    return newPoint

def getContours(img):
    contours,hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area >500:
            #cv.drawContours(imgResult, cnt, -1, (255,0,0), 3) # this draws the contour cv.drawContours(img, area of contour, index, (color), thickness)
            peri = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt, 0.02*peri, True)
            print(len(approx))
            x,y,w,h = cv.boundingRect(approx)
    return x+w//2,y


def drawOnCanvas(myPoints,myClorValues):
    for point in myPoints:
         cv.circle(imgResult,(point[0],point[1]), 10, myClorValues[point[2]],cv.FILLED)





while True:
    isTrue, img = cap.read()
    imgResult = img.copy()
    newPoint = findColor(img, myColors, myClorValues)
    if len(newPoint) != 0:
        for newp in newPoint:
            myPoints.append(newp)
    if len(myPoints) != 0 :
        drawOnCanvas(myPoints, myClorValues)
    cv.imshow("video", imgResult)
    if cv.waitKey(1) & 0xff == ord("q"):

        break

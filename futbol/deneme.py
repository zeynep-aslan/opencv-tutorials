import cv2
import numpy as np
import imutils

kamera = cv2.VideoCapture(0)
while True:
    ret, frame = kamera.read()
    if ret==False:
        kamera = cv2.VideoCapture(0)
        ret, frame = kamera.read()
    # frame=imutils.resize(frame,width=600)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur=cv2.medianBlur(gray,3)
    #blur=cv2.GaussianBlur(gray,(5,5),0)
    thresh=cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,3)
    # ret3,thresh = cv2.threshold(blur,0,155,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        
    #print(thresh)
    kernel=np.ones((5,5),np.uint8)
    erod=cv2.erode(thresh,kernel,iterations=1)
    dilat=cv2.dilate(erod,kernel,iterations=1)

    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    # print(cnts)
    center = None

    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        if radius > 5 and radius<20:
            print("1")
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 0, 255), 2)

    if x < 200:
        cv2.putText(frame, "GOOOAALLLL!! ", (50, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, .7, (0, 255, 0))
    else:
        cv2.putText(frame, "NO GOAL", (50, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, .7, (0, 0, 255))
    cv2.line(frame, (200, 0), (200, 511), (255, 0, 0), 5)
    cv2.imshow('goruntu',frame)

    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

kamera.release()
cv2.destroyAllWindows()

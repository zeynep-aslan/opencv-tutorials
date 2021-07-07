import cv2
import numpy as np
import imutils
from collections import deque

h_black=np.array([80,80,80])
l_black=np.array([255,255,255])
kernel=np.ones((5,5),np.uint8)
pts = deque()

kamera = cv2.VideoCapture(0)
while True:
    ret, frame = kamera.read()
    if ret==False:
        kamera = cv2.VideoCapture(0)
        ret, frame = kamera.read()

    # pts = deque()

    frame = cv2.flip(frame, 1) # resmi çevirir
    frame=imutils.resize(frame,width=600)
    
    blur=cv2.GaussianBlur(frame,(11,11),0)
    hsv=cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)

    mask=cv2.inRange(hsv,h_black,l_black)
    mask=cv2.erode(mask,kernel,iterations=2)
    mask=cv2.dilate(mask,kernel,iterations=2)
    # cv2.imshow("mask",mask)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)  # buna bak
    # print(cnts)
    center = None

    if len(cnts)>0:
        c=max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        if radius>10 and radius<30:
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)  # çemberin merkezi
    
    pts.appendleft(center)

    for i in range(1, len(pts)):
    
        if pts[i-1] is None or pts[i] is None:
            continue
        cv2.line(frame, pts[i-1], pts[i], (0, 0, 255), 5)

    if cv2.waitKey(1) & 0xFF == ord('c'):  # clean
        cv2.imwrite("new_image.jpeg",frame)
        pts.clear()
        # pts.pop()
        #pts = deque()
        
    cv2.imshow("frame",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # quit
        break

    
kamera.release()
cv2.destroyAllWindows()



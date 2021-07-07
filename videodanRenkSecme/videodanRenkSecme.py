import cv2
import numpy as np

webcam = cv2.VideoCapture("ram.mp4")

while True:
    _, imageFrame = webcam.read() 
    
    if _==False:
        webcam = cv2.VideoCapture("ram.mp4")
        _, imageFrame = webcam.read() 

    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV) 
    kernal = np.ones((5, 5), "uint8")

    cv2.normalize(imageFrame, imageFrame, 50, 200, cv2.NORM_MINMAX)  

    red_lower = np.array([136, 87, 111], np.uint8) 
    red_upper = np.array([180, 255, 255], np.uint8) 
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)
    red_mask = cv2.dilate(red_mask, kernal)
    res_red = cv2.bitwise_and(imageFrame, imageFrame, mask = red_mask)

    green_lower = np.array([25, 52, 72], np.uint8) 
    green_upper = np.array([102, 255, 170], np.uint8) 
    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)
    green_mask = cv2.dilate(green_mask, kernal)
    res_green = cv2.bitwise_and(imageFrame, imageFrame, mask = green_mask)

    blue_lower = np.array([94, 80, 2], np.uint8) 
    blue_upper = np.array([120, 255, 255], np.uint8) 
    blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)
    blue_mask = cv2.dilate(blue_mask, kernal)
    res_blue = cv2.bitwise_and(imageFrame, imageFrame, mask = blue_mask)

    black_lower = np.array([0, 0, 0], np.uint8) 
    black_upper = np.array([10, 10, 10], np.uint8) 
    black_mask = cv2.inRange(hsvFrame, black_lower, black_upper)
    black_mask = cv2.dilate(black_mask, kernal)
    res_black = cv2.bitwise_and(imageFrame, imageFrame, mask = black_mask)

    white_lower = np.array([220, 220, 220], np.uint8) 
    white_upper = np.array([255, 255, 255], np.uint8) 
    white_mask = cv2.inRange(hsvFrame, white_lower, white_upper)
    cv2.imshow("hsv",hsvFrame)
    cv2.imshow("1",white_mask)
    white_mask = cv2.dilate(white_mask, kernal)
    cv2.imshow("2",white_mask)
    res_white = cv2.bitwise_and(imageFrame, imageFrame, mask = white_mask)
    cv2.imshow("3",res_white)

    imageFrame=cv2.medianBlur(imageFrame,1)
    # cv2.imshow("ben blue",blue_mask)
    contours, hierarchy = cv2.findContours(red_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  # RETR_TREE -> ebeveynler ve çocuklar eşit
    # print(contours)
    # print(hierarchy)
    for pic,contour in enumerate(contours):  # cv2.CHAIN_APPROX_SIMPLE -> gereksiz noktaları kaldırır kontür sıkılaştırır. alan tasarrufu sağlar
        area=cv2.contourArea(contour)
        if (area>300):
            x,y,w,h=cv2.boundingRect(contour)  # çizilen dikdörtgen içindekinin boyutuna göre şekil alır
            imageFrame=cv2.rectangle(imageFrame,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.putText(imageFrame,"Red Colour",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,0,255))

    contours, hierarchy = cv2.findContours(green_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic,contour in enumerate(contours):
        area=cv2.contourArea(contour)
        if (area>300):
            x,y,w,h=cv2.boundingRect(contour)  
            imageFrame=cv2.rectangle(imageFrame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imageFrame,"Green Colour",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,255,0))

    contours, hierarchy = cv2.findContours(blue_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic,contour in enumerate(contours):
        area=cv2.contourArea(contour)
        if (area>300):
            x,y,w,h=cv2.boundingRect(contour)  
            imageFrame=cv2.rectangle(imageFrame,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(imageFrame,"Blue Colour",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1.0,(255,0,0))

    contours, hierarchy = cv2.findContours(black_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic,contour in enumerate(contours):
        area=cv2.contourArea(contour)
        if (area>300):
            x,y,w,h=cv2.boundingRect(contour)  
            imageFrame=cv2.rectangle(imageFrame,(x,y),(x+w,y+h),(0,0,0),2)
            cv2.putText(imageFrame,"Black Colour",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,0,0))

    contours, hierarchy = cv2.findContours(white_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic,contour in enumerate(contours):
        area=cv2.contourArea(contour)
        if (area>50):
            x,y,w,h=cv2.boundingRect(contour)
            imageFrame=cv2.rectangle(imageFrame,(x,y),(x+w,y+h),(220,90,240),2)
            cv2.putText(imageFrame,"White Colour",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1.0,(220,90,240))        

    cv2.imshow("Benimki", imageFrame) 
    
    if cv2.waitKey(50) & 0xFF == ord('q'): 
        webcam.release()
        cv2.destroyAllWindows()
        break
    








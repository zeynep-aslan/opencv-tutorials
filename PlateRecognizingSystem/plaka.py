import cv2
import numpy as np
import imutils
import pytesseract 
from PIL import Image

# print("0")
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/PCnet/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'
file = open("recognized.txt", "w+") 
file.write("") 
file.close() 
temp = False
kamera = cv2.VideoCapture("sanatsal.mp4")
while True:
    ret, frame = kamera.read()
    if ret==False:
        # print("1")
        kamera = cv2.VideoCapture("sanatsal.mp4")
        ret, frame = kamera.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #noise_removal = cv2.bilateralFilter(gray, 9, 120, 120)
    noise_removal = cv2.GaussianBlur(gray, (13, 13),sigmaX=0)
    # noise_removal = cv2.medianBlur(gray,13)

    # ret, thresh_image = cv2.threshold(noise_removal,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    thresh_image = cv2.adaptiveThreshold(noise_removal,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,9,2)

    # ret, thresh_image = cv2.threshold(noise_removal, 0, 255, cv2.THRESH_OTSU)
    
    canny_image=cv2.Canny(thresh_image, 100, 255)
    # kernel = np.ones((3, 3), np.uint8)
    # dilated_image = cv2.dilate(canny_image, kernel, iterations=1)
    cv2.imshow('dilated_image', canny_image)

    contours=cv2.findContours(canny_image.copy(),cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    contours = sorted(contours,key=cv2.contourArea, reverse = True)[:10]
    screenCnt = None
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * peri, True)
        if len(approx) == 4:
            screenCnt = approx
            cropped = frame[y:y+h, x:x+w]
            file = open("recognized.txt", "a")             
            text = pytesseract.image_to_string(cropped, config='--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZXWQ')
            # boxes = pytesseract.image_to_data(cropped,config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZXWQ')  # --psm bak
            
            # print(type(text))
            if (text[0].isdecimal()) and (text[1].isdecimal()):
                print(text)
                file.write(text) 
                file.write("\n")
                file.close
            # print(text)    
                cv2.imshow('cropped', cropped)
                

    if cv2.waitKey(1) & 0xFF == ord('q'):
        # temp =True
        break
    
kamera.release()
cv2.destroyAllWindows()        
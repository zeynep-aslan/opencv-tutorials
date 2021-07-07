import numpy as np
import cv2
import threading
import time

def kamera0():
    temp = False
    while True:
        try:
            cap0 = cv2.VideoCapture("USB/VID_05A3&PID_9210&MI_00")
        except:
            pass
        while cap0.isOpened():
            ret0 , frame = cap0.read()

            if ret0==False:
                try:
                    cap0 = cv2.VideoCapture("USB/VID_05A3&PID_9210&MI_00")
                except:
                    pass
                ret0, frame = cap0.read()
            else:
                cv2.imshow('webcam', frame)    
                if cv2.waitKey(1) & 0xFF == ord('c'): 
                    #cv2.destroyWindow("webcam")
                    cap0.release()
                    temp = True
                    
                    break

        if temp:
            break

def kamera1():
    temp = False
    while True:
        try:
            cap0 = cv2.VideoCapture("USB/VID_5986&PID_2113&MI_00")
        except:
            pass
        while cap0.isOpened():
            ret0 , frame = cap0.read()

            if ret0==False:
                try:
                    cap0 = cv2.VideoCapture("USB/VID_5986&PID_2113&MI_00")
                except:
                    pass
                ret0, frame = cap0.read()
            else:
                cv2.imshow('kamera', frame)    
                if cv2.waitKey(1) & 0xFF == ord('x'): 
                    #cv2.destroyWindow("kamera")
                    cap0.release()
                    temp = True
                    
                    break

        if temp:
            break

t0=threading.Thread(target=kamera0,)
t1=threading.Thread(target=kamera1,)

t0.start()

t1.start()
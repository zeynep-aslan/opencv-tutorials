import numpy as np
import cv2
import threading
import time

def kamera0():
    cap0 = cv2.VideoCapture("USB/VID_05A3&PID_9210&MI_00/6&226FD587&0&0000")
    temp=1
    while cap0.isOpened():
        ret0 , frame = cap0.read()
        if ret0==False:
            cap0 = cv2.VideoCapture("USB/VID_05A3&PID_9210&MI_00/6&226FD587&0&0000")
            ret0, frame = cap0.read()
        frame = cv2.flip(frame, 1)
        cv2.imshow('webcam', frame)    
        if cv2.waitKey(1) & 0xFF == ord('c'): 
            # cv2.destroyWindow(frame)
            # cv2.waitKey(0)
            # temp=0
            
            cap0.release()
            break
    #kamera0()

    # try:
    #     pass
    # except:
    #     kamera0()

    # if not cap0.isOpened():
    #     return kamera0()        

def kamera1():
    cap1 = cv2.VideoCapture("USB/VID_5986&PID_2113&MI_00/6&108FD781&0&0000")
    print("1")
    tempp=1
    while cap1.isOpened():
        ret1 , frame1 = cap1.read()
        if ret1==False:
            cap1 = cv2.VideoCapture("USB/VID_5986&PID_2113&MI_00/6&108FD781&0&0000")
            ret1, frame1 = cap1.read()
        frame1 = cv2.flip(frame1, 1)    
        cv2.imshow('laptop camera', frame1)    
        if cv2.waitKey(1) & 0xFF == ord('x'): 
            # cv2.destroyWindow(frame1)
            # cv2.waitKey(0)
            # tempp=0
            
            cap1.release()
            break
    #kamera1()

    # try:
    #     pass
    # except:
    #     kamera1()

    # if not cap1.isOpened():
    #     return kamera1()

# while True:
t0=threading.Thread(target=kamera0,)
t1=threading.Thread(target=kamera1,)

t0.start()
t1.start()

#t0.join()
#t1.join()




# if cv2.waitKey(1) & 0xFF == ord('q'): 
#     # cv2.destroyAllWindows()
#     break


# vid0 = cv2.VideoCapture(0)
# vid1 = cv2.VideoCapture(1)
# cam0=True
# cam1=True

# while True:
#     if cam0:
#         ret0 , frame = vid0.read()
#     if cam1:    
#         ret1 , frame1 = vid1.read()

#     if ret0:
#         cv2.imshow('cam0',frame)  
#     else:
#         cam0=False
#         cv2.destroyWindow(frame)
#         vid0.release()
#         # cv2.waitKey(1)

#     if ret1:
#         cv2.imshow('cam1', frame1)
#     else:
#         cam1=False
#         cv2.destroyWindow(frame1)
#         vid1.release()
#         # cv2.waitKey(1)

#     if cv2.waitKey(1) & 0xFF == ord('q'): 
#         break
# cv2.waitKey(1)
# cv2.destroyAllWindows()


# import cv2 as cv
# import time

# WINDOW_NAME = "win"

# image = cv.imread("img_1.jpeg", CV_LOAD_IMAGE_COLOR)
# cv.namedWindow(WINDOW_NAME, CV_WINDOW_AUTOSIZE)
# initialtime = time.time()

# cv.startWindowThread()

# while (time.time() - initialtime < 5):
#   print("in first while")
# cv.imshow(WINDOW_NAME, image)
# cv.waitKey(1000)

# cv.waitKey(1)
# cv.destroyAllWindows()
# cv.waitKey(1)

# initialtime = time.time()
# while (time.time() - initialtime < 6):
#     print("in second while")
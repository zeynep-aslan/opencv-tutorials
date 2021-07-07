import cv2
import numpy as np

sinirlar=[
    ([161, 155, 84], [179, 255, 255]),
	([25, 52, 72], [102, 255, 255]),
	([94, 80, 2], [126, 255, 255]),
    ([103, 86, 65], [145, 133, 128])
]

def Renk_Algila(sinirlar,color_index):
    kamera = cv2.VideoCapture("renkler.mp4")
    while (kamera.isOpened()):
        ret, frame = kamera.read()
        cv2.imshow("videoooooo",frame)
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        low = np.array(sinirlar[color_index][0])
        high = np.array(sinirlar[color_index][1])
        mask = cv2.inRange(hsv_frame, low, high)
        color = cv2.bitwise_and(frame, frame, mask=mask)
        median=cv2.medianBlur(color,5)
        cv2.imshow("colorr",median)
        if (cv2.waitKey(100) & 0xFF == ord('q')):
            break


color = input("hangi rengi gormek istersiniz? (b,g,r) ")
if color=="b":
    Renk_Algila(sinirlar,2)
elif color=="g":
    Renk_Algila(sinirlar,1)
elif color=="r":
    Renk_Algila(sinirlar,0)
else:
    print("yalis girdin")



cv2.waitKey(0)
cv2.destroyAllWindows()  



















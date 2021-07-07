import cv2
import numpy as np

def Kare(resim, x):
    yukseklik, genislik, kanal = resim.shape
    for i in range(yukseklik):
        for j in range(genislik):
            if ((i>(yukseklik/2)-(x/2) and i<(yukseklik/2)+(x/2))and(j>(genislik/2)-(x/2) and j<(genislik/2)+(x/2))):
                resim[i,j] = 255,0,0
    return resim

resim = np.zeros((300,150,3), dtype="uint8")
yukseklik,genislik, kanal = resim.shape
num = int(input("bir sayi girin: "))
while (yukseklik<num or genislik<num):
    print("daha kucuk bir sayi girin.")
    num = int(input("bir sayi girin: "))
resim = Kare(resim, num)
cv2.imshow("resim", resim)
# print(Kare(resim, num))




cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np

img_org = cv2.imread("cicek.jpg",0)

def Boyut_Kucult(resim):
    yukseklik, genislik = resim.shape
    kucuk_image = np.zeros((int(yukseklik/4), int(genislik/4)), resim.dtype)
    a=0
    b=0
    for y in range(0,yukseklik, 4):
        for x in range(0,genislik, 4):
            kucuk_image[a,b] =resim[y,x] #(resim[y, x + 1] + resim[y, x] + resim[y + 1, x] + resim[y + 1, x + 1]) / 4
            b += 1
        a += 1
        b = 0
    return kucuk_image

def Boyut_Buyut(resim):
    yukseklik, genislik = resim.shape
    buyuk_image = np.zeros((yukseklik*4, genislik*4), resim.dtype)
    a=0
    b=0
    for y in range(yukseklik):
        for x in range(genislik):
            if a<1024 and b<1024:
                for i in range(0,4):
                    for j in range(0,4):
                        buyuk_image[a+i,b+j] = resim[y,x]
            b += 4
        a += 4
        b=0
    return buyuk_image
cv2.imshow("orijinal resim", img_org)
kucuk = Boyut_Kucult(img_org)
cv2.imshow("kucuk resim", kucuk)

buyuk = Boyut_Buyut(kucuk)
cv2.imshow("buyuk resim", buyuk)

cv2.waitKey(0)
cv2.destroyAllWindows()
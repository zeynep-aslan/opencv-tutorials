import cv2
import numpy as np
import random
# benim blurla düzeltme
img_org = cv2.imread("ram2.jpg",0)

def addNoise(img):
    yukseklik, genislik = img.shape
    new_image = np.zeros(img.shape, img.dtype)

    p = 0.08
    for i in range(yukseklik):
        for j in range(genislik):
            r = random.random()
            if r < p/2:
                new_image[i,j] = 0
            elif r<p:
                new_image[i,j] = 255
            else:
                new_image[i,j] = img[i,j]
    return new_image            

def Blur_Yap(img_org, blur_miktar):
    yukseklik, genislik = img_org.shape
    new_image = np.zeros(img_org.shape, img_org.dtype)
    temp = 0
    sayac = 0
    blue = 0
    green = 0
    red = 0
    val = blur_miktar
    for y in range(yukseklik):
        for x in range(genislik):
            for i in range(-val,val+1):
                for j in range(-val,val+1):
                    if (y+i<yukseklik and x+j<genislik and y+i>=0 and x+j>=0):
                        temp += int(img_org[y+i, x+j])
                        sayac +=1
                        # blue += int(img_org[y+i, x+j, 0])
                        # green += int(img_org[y+i, x+j, 1])
                        # red += int(img_org[y+i, x+j, 2])

            for m in range(-val,val+1):
                for n in range(-val,val+1):
                    if (y+m<yukseklik and x+n<genislik and y+m>=0 and x+n>=0):
                        new_image[y+m, x+n] = int(temp/sayac)
                        # new_image[y+m, x+n, 0] = int(blue/((val*2+1)**2))
                        # new_image[y+m, x+n, 1] = int(green/((val*2+1)**2))
                        # new_image[y+m, x+n, 2] = int(red/((val*2+1)**2))
            temp = 0
            sayac =0
    return new_image

def Threshold_Yap(blurlu, thres_sinir):
    th1 = cv2.adaptiveThreshold(blurlu,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,3,2)
    return th1        

noiseli = addNoise(img_org)
cv2.imshow("noise eklenmis", noiseli)

blur_miktar = 1
blurlu = Blur_Yap(noiseli, blur_miktar)
cv2.imshow("benim blur eklenmis", blurlu)

thres_sinir = 150
thresli = Threshold_Yap(blurlu, thres_sinir)

cv2.imshow("adaptive threshold lu", thresli)


cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np
import random
# median blurla düzeltme
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
    median = cv2.medianBlur(img_org,blur_miktar)          
    return median

def Threshold_Yap(blurlu, thres_sinir):
    th1 = cv2.adaptiveThreshold(blurlu,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,3,2)
    return th1        

noiseli = addNoise(img_org)
cv2.imshow("noise eklenmis", noiseli)

blur_miktar = 4
blurlu = Blur_Yap(noiseli, blur_miktar)
cv2.imshow("median blur eklenmis", blurlu)

thres_sinir = 150
thresli = Threshold_Yap(blurlu, thres_sinir)

cv2.imshow("adaptive threshold lu", thresli)


cv2.waitKey(0)
cv2.destroyAllWindows()
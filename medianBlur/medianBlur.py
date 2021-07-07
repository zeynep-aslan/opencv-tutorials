import cv2
import numpy as np
import random

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
    liste = []
    sayac = 0
    val = blur_miktar
    for y in range(yukseklik):
        for x in range(genislik):
            for i in range(-val,val+1):
                for j in range(-val,val+1):
                    if (y+i<yukseklik and x+j<genislik and y+i>=0 and x+j>=0):
                        liste.append(int(img_org[y+i, x+j]))  # matrisi listeye attık
                        sayac +=1

            for m in range(-val,val+1):
                for n in range(-val,val+1):
                    if (y+m<yukseklik and x+n<genislik and y+m>=0 and x+n>=0):
                        # new_image[y+m, x+n] = int(temp/sayac)
                        araEleman = 0
                        for k in range(sayac):  # listeyi kuc-buy sıraladık
                            for l in range(sayac):
                                if(liste[k]>liste[l]):
                                    araEleman=liste[k]
                                    liste[k]=liste[l]
                                    liste[l]=araEleman
            ortadaki = int(sayac/2)
            new_image[y, x] = liste[ortadaki]                                                       
            liste.clear()
            sayac =0
    return new_image

def Blur_Yapp(img_org, blur_miktar):
    median = cv2.medianBlur(img_org,blur_miktar)          
    return median

def Threshold_Yap(blurlu, thres_sinir):
    th1 = cv2.adaptiveThreshold(blurlu,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,3,2)
    return th1  

noise = addNoise(img_org)
benimMedianBlur = Blur_Yap(noise, 1)

tempMedianBlur = Blur_Yapp(noise,3)

benimThres= Threshold_Yap(benimMedianBlur, benimMedianBlur)
benimThresHazirBlur= Threshold_Yap(tempMedianBlur, tempMedianBlur)


cv2.imshow("kendi median blurum", benimMedianBlur)
cv2.imshow("hazir median blur", tempMedianBlur)

cv2.imshow("benim blurla threshold",benimThres)
cv2.imshow("hazir blurla threshold",benimThresHazirBlur)


cv2.waitKey(0)
cv2.destroyAllWindows()
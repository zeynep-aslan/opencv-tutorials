import cv2
import numpy as np

img_org = cv2.imread("ram2.jpg",0)

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

def Threshold_Yap(blurlu_image, thres_sinir):
    yukseklik, genislik = blurlu_image.shape
    thresli_image = np.zeros(blurlu_image.shape, blurlu_image.dtype)

    for y in range(yukseklik):
        for x in range(genislik):
            if (blurlu_image[y,x]<thres_sinir):
                thresli_image[y,x] = 0
            else:
                thresli_image[y,x] = 255
    return thresli_image                


blur_miktar = int(input("blur derecesini girin [0-10]: "))
while (blur_miktar<0 or blur_miktar>10):
    print("lütfen 0 ile 10 arasinda bir deger girin: ")
    blur_miktar = int(input("blur derecesini girin "))

thres_sinir = int(input("threshold sinirini girin [75-150]: "))
while (thres_sinir<75 or thres_sinir>150):
    print("lütfen 75 ile 150 arasinda bir deger girin: ")
    thres_sinir = int(input("threshold sinirini girin: "))

blurlu = Blur_Yap(img_org, blur_miktar)
thresli = Threshold_Yap(blurlu, thres_sinir)
th1 = cv2.adaptiveThreshold(blurlu,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,3,2)
cv2.imshow("orijinal resim", img_org)
cv2.waitKey(0)

cv2.imshow("blurlu resim", blurlu)
cv2.waitKey(0)

cv2.imshow("thresli resim", thresli)
cv2.imshow("thresli binary", th1)

cv2.waitKey(0)
cv2.destroyAllWindows()
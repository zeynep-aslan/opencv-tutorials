import cv2
import numpy as np
from matplotlib import pyplot as plt
import random

# original = cv2.imread("ram2.jpg",0)


# noise = np.random.normal(0, 1, original.shape)
# # new_signal = original + noise
# # print(new_signal)

# # noise = np.random.normal(0,1,100)

# new_signal = cv2.add(original,noise)

# cv2.imshow("gurultulu resim", new_signal)
# cv2.imshow("gurultusuz resim", original)

# ----------------

img = cv2.imread("ram2.jpg",0)
yukseklik, genislik = img.shape

def Blur_Yap(img_org, blur_miktar):
    yukseklik, genislik = img_org.shape
    new_image = np.zeros(img_org.shape, img_org.dtype)
    temp = 0
    sayac = 0
    val = blur_miktar
    for y in range(yukseklik):
        for x in range(genislik):
            for i in range(-val,val+1):
                for j in range(-val,val+1):
                    if (y+i<yukseklik and x+j<genislik and y+i>=0 and x+j>=0):
                        temp += int(img_org[y+i, x+j])
                        sayac +=1

            for m in range(-val,val+1):
                for n in range(-val,val+1):
                    if (y+m<yukseklik and x+n<genislik and y+m>=0 and x+n>=0):
                        new_image[y+m, x+n] = int(temp/sayac)

            temp = 0
            sayac =0
    return new_image

p = 0.08

new_image = np.zeros(img.shape, img.dtype)

for i in range(yukseklik):
    for j in range(genislik):
        r = random.random()
        if r < p/2:
            new_image[i,j] = 0
        elif r<p:
            new_image[i,j] = 255
        else:
            new_image[i,j] = img[i,j]      

# dst = new_image.copy()
# dst = cv2.fastNlMeansDenoising(new_image,None,3,7,21)
median = cv2.medianBlur(new_image,3)          

# cv2.imshow("ssss", Blur_Yap(new_image, 3))
# plt.imshow(new_image)
# plt.show()
cv2.imshow("new image", new_image)
cv2.imshow("dst image", median)

cv2.waitKey(0)
cv2.destroyAllWindows()
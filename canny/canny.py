import cv2 
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('vaseline6.jpeg', 0) 

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


# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
# plt.show()


blurlu=Blur_Yap(img,1)
edges = cv2.Canny(blurlu,100,200)
cv2.imshow("canny",edges)
blursuzEdges=cv2.Canny(img,100,200)
cv2.imshow("blursuz",blursuzEdges)

cv2.waitKey(0)
cv2.destroyAllWindows()
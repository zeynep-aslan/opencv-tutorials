import cv2
import numpy as np

resim = cv2.imread("ram2.jpg")
new_image = np.zeros(resim.shape, resim.dtype)

def Parlaklik_Degistir(resim, parlaklik, secenek):
    if secenek==1:
        for y in range(resim.shape[0]):
            for x in range(resim.shape[1]):
                for c in range(resim.shape[2]):
                    new_image[y, x, c] = np.clip(resim[y, x, c] + parlaklik, 0, 255)
                    # alpha = (parlaklik / resim[y, x, c])
                    # beta = (parlaklik % resim[y, x, c])
        return new_image
    elif secenek==2:
        for y in range(resim.shape[0]):
            for x in range(resim.shape[1]):
                for c in range(resim.shape[2]):
                    new_image[y, x, c] = np.clip(resim[y, x, c] - parlaklik, 0, 255)
                    # alpha = (parlaklik / resim[y, x, c])
                    # beta = (parlaklik % resim[y, x, c])
        return new_image
    else:
        print("hatali sayi girdin seni Allahina yolluyorum")

try:
    us = int(input('* parlaklik degeri girin[1-8]: '))
except ValueError:
    print('lutfen sayi girin')

secenek = int(input("parlakligi arttirmak istiyorsaniz 1\nParlakligi azalmak istiyorsaniz 2 yi tuslayin\n"))
cv2.imshow('Original Image', resim)

for i in range(1,us+1):
    parlaklik = 2**i
    print(i)
    cv2.imshow('New Image', Parlaklik_Degistir(resim, parlaklik, secenek))
    cv2.waitKey(0)
cv2.waitKey(0)
cv2.destroyAllWindows()
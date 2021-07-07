import cv2
import numpy as np

def tersTrol(resim):
    yukseklik, genislik = resim.shape
    sayac = 0
    for i in range(yukseklik):
        sayac += 1
        for j in range(genislik):
            if (yukseklik % 2 == 0 and sayac < yukseklik / 2):
                temp = resim[i][j]
                resim[i][j] = resim[yukseklik - i - 1][j]
                resim[yukseklik - i - 1][j] = temp
            elif (yukseklik % 2 == 1 and sayac < (yukseklik - 1) / 2):
                temp = resim[i][j]
                resim[i][j] = resim[yukseklik - i - 1][j]
                resim[yukseklik - i - 1][j] = temp
        print('\n')
    return resim

def aynaliTrol(resim):
    yukseklik, genislik = resim.shape
    if (genislik % 2 == 0):
        print(type(genislik/2))
        print(genislik/2)
        for i in range(int(genislik/2)):
            for j in range(yukseklik):
                
                temp = resim[j][i]
                resim[j][i] = resim[j][genislik-i-1]
                resim[j][genislik-i-1] = temp
            print('\n')
    print(genislik)                
    if (genislik % 2 == 1):
        # print(genislik)  # 240
        for i in range((genislik-1)/2):
            for j in range(yukseklik):
                temp = resim[i][j]
                resim[i][j] = resim[i][genislik-j-1]
                resim[i][genislik-j-1] = temp
                print('\n')                
    return resim

resim_org = cv2.imread("ram2.jpg",0)
resim = resim_org.copy()
resim2 = resim_org.copy()
resim = aynaliTrol(resim)

resim2 = tersTrol(resim2)

cv2.imshow("aynali trol",resim)

cv2.imshow("ters trol",resim2)

cv2.waitKey(0)
cv2.destroyAllWindows()
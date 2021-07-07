import cv2
import numpy as np

img=cv2.imread("kare2.jpeg")  # benim şeklim içerdeki kareleri neden bulmuyor, kare3 ün yamukluğunu düzelt(araştırma), en büyük kareyi bul(alandan yola çık(h*w))
frame=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(frame, (7, 7), 2)

edge = cv2.Canny(blur, 0, 50, 3)
contours, hierarchy = cv2.findContours(edge,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

try: hierarchy = hierarchy[0]
except: hierarchy = []

height, width = edge.shape
alanlar=[]
alan=0
for contour, hier in zip(contours, hierarchy):
    (x,y,w,h) = cv2.boundingRect(contour)
    # min_x, max_x = min(x, min_x), max(x+w, max_x)
    # min_y, max_y = min(y, min_y), max(y+h, max_y)
    alan=w*h
    alanlar.append(alan)
    kareDict = {
        alan:{
            "w":w,
            "h":h
    }}

    kareDict.update({
        alan: {"w":w,"h":h}
    })

    kareDict[alan]["w"]=w
    kareDict[alan]["h"]=h


alanlar.sort(reverse=True)
enbuyuk=alanlar[0]
values= []
for item in kareDict[enbuyuk].values():
    values.append(item)

w=values[0]
h=values[1]

cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)
    

cv2.imshow("Contour", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

#----------------------

# deneme

# import cv2 as cv
# import numpy as np
# import random as rng

# img = cv.imread('kare2.jpeg') # read picture
# imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # BGR to grayscale
# imgray = cv.blur(imgray, (3,3))

# ret, threshold = cv.threshold(imgray, 200, 255, cv.THRESH_BINARY)
# canny_output = cv.Canny(threshold, 0, 50, 3)
# # edge = cv2.Canny(blur, 0, 50, 3)

# contours, hierarchy = cv.findContours(canny_output, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

# contours_poly = [None]*len(contours)
# boundRect = [None]*len(contours)
# # centers = [None]*len(contours)
# # radius = [None]*len(contours)
# for i, c in enumerate(contours):
#     contours_poly[i] = cv.approxPolyDP(c, 3, True)
#     boundRect[i] = cv.boundingRect(contours_poly[i])
#     # centers[i], radius[i] = cv.minEnclosingCircle(contours_poly[i])

# drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)

# for i in range(len(contours)):
#     color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
#     cv.drawContours(drawing, contours_poly, i, color)
#     cv.rectangle(drawing, (int(boundRect[i][0]), int(boundRect[i][1])), \
#           (int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])), color, 2)
#         # cv.circle(drawing, (int(centers[i][0]), int(centers[i][1])), int(radius[i]), color, 2)

# cv.imshow('Contours', drawing)
# # epsilon = 0.1 * cv2.arcLength(countours[0], True)
# # approx = cv2.approxPolyDP(countours[0], epsilon, True)

# # cv2.drawContours(im, approx, -1, (0, 255, 0), 3)
# # cv2.imshow("Contour", im)

# cv.waitKey(0)
# cv.destroyAllWindows()



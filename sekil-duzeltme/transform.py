import cv2
import numpy as np
import imutils

def proccess(frame):      
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7, 7), 2)
    edged = cv2.Canny(blur, 0, 50, 5)
    kernel = np.ones((3, 3), np.uint8) 
    # Using cv2.erode() method  
    eroded = cv2.dilate(edged, kernel)
    # cv2.imshow("edge", edge)
    cv2.imshow("erode",eroded)
    cv2.imshow("edge",edged)
    cnts = cv2.findContours(eroded.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    # cnts = cv2.findContours(edged.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)  # opencv nin sürümünü kullanıp kullanmadığımıza bağlı olarak uygun tuple değerini alır.
    # print(cnts)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:50]
    # print(cnts)
    screenCnt = None
    for c in cnts:
        epsilon = cv2.arcLength(c, True)  # sekil kapali mi acik mi
        approx = cv2.approxPolyDP(c, 0.02 * epsilon, True)
        # print(approx)
        if len(approx) == 4:
            screenCnt = approx
            print("ww")
        # break
    if screenCnt is None:
        detected = 0
    else:
        detected = 1
    # print(screenCnt)
    return frame, screenCnt, detected

def reading(frame, screenCnt):
    crd = screenCnt[0]
    x0, y0 = crd[0]
    crd = screenCnt[1]
    x1, y1 = crd[0]
    crd = screenCnt[2]
    x2, y2 = crd[0]
    crd = screenCnt[3]
    x3, y3 = crd[0]
    pts = np.array([(x0, y0), (x1, y1), (x2, y2), (x3, y3)], dtype="float32")
    Cropped = four_point_transform(frame, pts)

    #Cropped = cv2.fastNlMeansDenoisingColored(Cropped, None, 10, 10, 7, 15)
    # Cropped = cv2.cvtColor(Cropped, cv2.COLOR_BGR2GRAY)
    # blur = cv2.GaussianBlur(Cropped, ksize=(3, 3), sigmaX=0)
    # ret, Cropped = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    
    # Cropped=cv2.cvtColor(Cropped, cv2.COLOR_BGR2GRAY)
    # blur = cv2.GaussianBlur(Cropped, (7, 7), 2)
    # Cropped = cv2.Canny(blur, 0, 50, 5)
    #cv2.imshow('Cropped', Cropped)
    #cv2.imshow('frame', frame)
    #cv2.waitKey(100)

    return Cropped

def order_points(pts):
    rect = np.zeros((4, 2), dtype = "float32")

    s = pts.sum(axis = 1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    diff = np.diff(pts, axis = 1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    return rect

def four_point_transform(image, pts):
    rect = order_points(pts)
    (tl, tr, br, bl) = rect

    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))

    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))

    dst = np.array([
		[0, 0],
		[maxWidth - 1, 0],
		[maxWidth - 1, maxHeight - 1],
		[0, maxHeight - 1]], dtype = "float32")

    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    return warped

if __name__ == "__main__":
    img=cv2.imread("kare2.jpeg")

    frame, screenCnt, detected=proccess(img)
    # print(detected)
    if detected:
        Cropped=reading(frame,screenCnt)
        # cropped=four_point_transform(img,pts)

        cv2.imshow("warplanmis resim",Cropped)
    else:
        print("Kapali kenar bulunamadi !!!!")
cv2.waitKey(0)
cv2.destroyAllWindows()
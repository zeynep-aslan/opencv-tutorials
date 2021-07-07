import cv2
import numpy as np

def oyunAlani(image,values=[' ' for x in range(9)]):
    font = cv2.FONT_HERSHEY_SIMPLEX
    h,w,kanalS=image.shape
    sayac=0
    for i in range(3):
        for j in range(3):
            if sayac==9:
                break
            cv2.putText(image, values[sayac],((int(((2*(j+1)-1)*w)/6)), (int(((2*(i+1)-1)*h)/6))),font,1,(0, 255, 0),2,cv2.LINE_AA)
            sayac+=1
    cv2.imshow('kesit', image)
    if cv2.waitKey(0) and 0xFF == ord('q'):
        cv2.destroyAllWindows()
        

def skorTablosu(skor_listesi):
    print("\t","*"*30)
    print("\t           SKOR TABLOSU           ")
    print("\t","*"*30)
 
    players = list(skor_listesi.keys())
    print("\t   ", players[0], "\t    ", skor_listesi[players[0]])
    print("\t   ", players[1], "\t    ", skor_listesi[players[1]])
    print("\t","*"*30)

def game(sirasi_gelen, image):
    values = [' ' for x in range(9)]
    count=0
    for i in range(10):
        try:
            print(f"Sira sende {sirasi_gelen}! Hangi kutuya gitmek istersin : ", end="")
            gidecek_yer = int(input()) 
        except ValueError:
            print("1 den 10 a kadar bir tam sayi girin.")
            continue

        if gidecek_yer<1 and gidecek_yer>9:
            print("yanlis girdi. tekrar deneyin")  
            continue

        if values[gidecek_yer-1]!=' ':
            print("sectiginiz kutu dolu. tekrar deneyin")
            continue

        values[gidecek_yer-1]=sirasi_gelen
        count+=1

        oyunAlani(image,values)

        if count>=5 and count<9:
            if values[0]==values[1]==values[2]!=' ':
                print("oyun bitti")
                print(f"{sirasi_gelen} oyunu kazandi!")
                return sirasi_gelen
            if values[3]==values[4]==values[5]!=' ':
                print("oyun bitti")
                print(f"{sirasi_gelen} oyunu kazandi!")    
                return sirasi_gelen          
            if values[6]==values[7]==values[8]!=' ':
                print("oyun bitti")
                print(f"{sirasi_gelen} oyunu kazandi!") 
                return sirasi_gelen
            if values[0]==values[4]==values[8]!=' ':
                print("oyun bitti")
                print(f"{sirasi_gelen} oyunu kazandi!")  
                return sirasi_gelen            
            if values[2]==values[4]==values[6]!=' ':
                print("oyun bitti")
                print(f"{sirasi_gelen} oyunu kazandi!") 
                return sirasi_gelen
            if values[0]==values[3]==values[6]!=' ':
                print("oyun bitti")
                print(f"{sirasi_gelen} oyunu kazandi!") 
                return sirasi_gelen
            if values[1]==values[4]==values[7]!=' ':
                print("oyun bitti")
                print(f"{sirasi_gelen} oyunu kazandi!")   
                return sirasi_gelen           
            if values[2]==values[5]==values[8]!=' ':
                print("oyun bitti")
                print(f"{sirasi_gelen} oyunu kazandi!")  
                return sirasi_gelen

        if count==9:
            print("kimse kazanamadi")
            return 'berabere'

        if sirasi_gelen=='X':
            sirasi_gelen='O'
        else:
            sirasi_gelen='X'    

if __name__ == "__main__":
    frame = cv2.imread('sekil.png')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7, 7), 0.5)
    edge = cv2.Canny(blur, 0, 50, 3)
    contours, hierarchy = cv2.findContours(edge, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour, hier in zip(contours, hierarchy):
        (x,y,w,h) = cv2.boundingRect(contour)
        kesit = frame[y:y+h,x:x+w]
        image=np.zeros((h,w),dtype="uint8")
        image=kesit
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    print("Player 1")
    player1 = input("isminizi girin : ")
    print("\n")
    
    print("Player 2")
    player2 = input("isminizi girin : ")
    print("\n")

    sirasi_gelen_oyuncu=player1
    skor_listesi={player1:0, player2:0}
    xoKim={'X':"",'O':""}
    xolist=['X','O']

    while True:
        print("Seceneklerden birini sec ", sirasi_gelen_oyuncu)
        print("X icin 1 i")
        print("O icin 2 i")
        print("Cikmak icin 3 u tuslayin ")
        try:
            secenek = int(input())   
        except ValueError:
            print("Seceneklerde verilen degerlerden birini girin\n")
            continue

        if secenek == 1:
            xoKim['X'] = sirasi_gelen_oyuncu
            if sirasi_gelen_oyuncu == player1:
                xoKim['O'] = player2
            else:
                xoKim['O'] = player1
 
        elif secenek == 2:
            xoKim['O'] = sirasi_gelen_oyuncu
            if sirasi_gelen_oyuncu == player1:
                xoKim['X'] = player2
            else:
                xoKim['X'] = player1
         
        elif secenek == 3:
            print("Final Skorlari")
            skorTablosu(skor_listesi)
            break     
        kazanan = game(xolist[secenek-1], image) #  'X'
        print(kazanan)

        if kazanan!='berabere':
            kazanan_oyuncu=xoKim[kazanan]
            skor_listesi[kazanan_oyuncu]+=1

        if sirasi_gelen_oyuncu==player1:
            sirasi_gelen_oyuncu=player2
        else:
            sirasi_gelen_oyuncu=player1    


cv2.waitKey(0)
cv2.destroyAllWindows()
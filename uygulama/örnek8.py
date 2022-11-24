def sayi_al(alt_sinir,ust_sinir):
    sayi=int(input())
    while sayi<alt_sinir or sayi>ust_sinir:
        sayi=int(input("Hatalı veri girildi. Lütfen tekrar giriniz: "))
    return(sayi)
def dikdortgen_ciz(dikey_kenar,yatay_kenar):
    for i in range(dikey_kenar):
        for j in range(yatay_kenar):
            print("*",end="")
        print("")
def dikdortgen_bilgilerini_hesapla(kenar1,kenar2):
    return(kenar1*kenar2,2*(kenar1+kenar2),kenar1==kenar2)
def faktoriyel(sayi):
    carpim=1
    for carpan in range(sayi,1,-1):
        carpim=carpim*carpan
    return carpim
def kombinasyon(n,k):
    return faktoriyel(n)/(faktoriyel(k)*faktoriyel(n-k))
def menu_goruntule():
    print("1. Dikdortgen çizme...")
    print("2. Dikdortgen bilgilerini hesaplama...")
    print("3. Faktoriyel hesaplama...")
    print("4. Kombinasyon(C(n,k)) hesaplama...")
    print("5. Çıkış...")
def main():
    cikis="h"
    while cikis=="h" or cikis=="H":
        menu_goruntule()
        print("Seçiminizi giriniz [0-5]:",end=" ")
        secim=sayi_al(0,5)
        if secim==1:
            print("Dikdörtgenin dikey kenar uzunluğunu giriniz [1,20]:",end=" ")
            kenar_dikey=sayi_al(1,20)
            print("Dikdörtgenin yatay kenar uzunluğunu giriniz [1,75]:",end=" ")
            kenar_yatay=sayi_al(1,75)
            dikdortgen_ciz(kenar_dikey,kenar_yatay)
        elif secim==2:
            print("Dikdörtgenin uzun kenarının uzunluğunu giriniz [1-1000]:",end=" ")
            kenar1=sayi_al(1,1000)
            print("Dikdörtgenin kısa kenarının uzunluğunu giriniz [1-1000]:",end=" ")
            kenar2=sayi_al(1,1000)
            alan,cevre,kare_mi=dikdortgen_bilgilerini_hesapla(kenar1,kenar2)
            print(f"Dikdörtgenin alanı: {alan}, çevresi: {cevre}")
            if kare_mi:
                print("Bu dikdörtgen bir karedir.")
        elif secim==3:
            print("Faktoriyeli hesaplanacak sayıyı giriniz [0,10]:",end=" ")
            n=sayi_al(0,10)
            sonuc=faktoriyel(n)
            print(f"Sonuç = {sonuc}")
        elif secim==4:
            print("n sayısını giriniz [1,10]:",end=" ")
            n=sayi_al(1,10)
            print(f"k sayısını giriniz [1-{n}]:",end=" ")
            k=sayi_al(1,n)
            sonuc=kombinasyon(n,k)
            print(f"Sonuç = {sonuc}")
        else:
            cikis=input("Çıkış yapmak istediğinize emin misiniz (e/h)? ")
            while cikis not in ["e","E","h","H"]:
                cikis=input("Hatalı veri girdiniz, lütfen tekrar giriniz: ")
main()
MIN=2
sayi=int(input("1'den büyük bir tam sayı giriniz: "))
while sayi>=2:
    for i in range (MIN,int((sayi**0.5)+1)):
        if (sayi%i==0):
            print("asal değil")
            break
    else:
        print("sayı asaldır")
    sayi=int(input("1'den büyük bir tam sayı giriniz: "))
uzun_kenar=int(input("Üçgenin uzun kenarının uzunluğunu tam sayı olarak giriniz: "))
kisa_kenar1=int(input("Üçgenin kısa kenarlarından birinin uzunluğunu tam sayı olarak giriniz: "))
kisa_kenar2=int(input("Üçgenin diğer kısa kenarının uzunluğunu tam sayı olarak giriniz: "))

if uzun_kenar>=kisa_kenar1+kisa_kenar2:
    print("Bu bir üçgen değildir.")
else:
    uzun_kenar_kare=uzun_kenar**2
    kisa_kenar_kare_top=kisa_kenar1**2+kisa_kenar2**2
    if uzun_kenar_kare==kisa_kenar_kare_top:
        print("Bu bir dik üçgendir.")
    elif uzun_kenar_kare>kisa_kenar_kare_top:
        print("Bu bir geniş açılı üçgendir.")
    else:
        print("Bu bir dar açılı üçgendir.")
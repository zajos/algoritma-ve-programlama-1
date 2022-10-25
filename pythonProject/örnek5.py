ay_no=int(input("Ay numarasını giriniz: "))
if ay_no<1 or ay_no>12 :
    print("Lütfen 1-12 arasında bir tam sayı giriniz.")
else:
    if ay_no==2:
        print("Bu ay 28 gündür.")
    elif ay_no==4 or ay_no==6 or ay_no==9 or ay_no==11:
        print("Bu ay 30 gündür.")
    else:
        print("Bu ay 31 gündür.")
    if ay_no==11 or ay_no==1 or ay_no==2:
        print("Kış Mevsimi")
    elif ay_no==3 or ay_no==4 or ay_no==5:
        print("İlkbahar")
    elif ay_no==6 or ay_no==7 or ay_no==8:
        print("Yaz")
    else:
        print("Sonbahar")

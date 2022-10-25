unvan=input("Çalışanın ünvanını giriniz(s:stajyer, u:uzman, l:takım lideri, m:müdür): ")
calisma_suresi=int(input("Çalışanın çalıştığı yıl sayısını giriniz: "))
ayin_elemani=input("Çalışan bu ay ayın elemanı seçildi mi(e/h)? ")
izin_sayisi=int(input("Çalışanın kullandığı izin sayısını giriniz: "))
if izin_sayisi!=0 or ayin_elemani=="h":
    print("Çalışan tatil kazanmamıştır.")
else:
    if unvan=="s":
        yer="Türkiye"
    elif unvan==u:
        yer="Avrupa"
    elif unvan=="l":
        yer="Uzak Doğu"
    else:
        yer="Amerika"
    if calisma_suresi<2:
        gun=3
    elif calisma_suresi<5:
        gun=4
    elif calisma_suresi<10:
        gun=5
    else:
        gun=7
    print(f"Çalışanın tatil yeri: {yer}, gideceği gün sayısı:{gun}")
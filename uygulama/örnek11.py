def uretim_verilerini_al(uretim_dosyasi,uretim_toplamlari,gun_sayilari):
    gun_no=uretim_dosyasi.readline()
    while gun_no!="":
        makina_no=int(uretim_dosyasi.readline())
        gunluk_uretim=int(uretim_dosyasi.readline())
        uretim_toplamlari[makina_no-1]+=gunluk_uretim
        gun_sayilari[makina_no-1]+=1
        gun_no=uretim_dosyasi.readline()
def istatistikler(uretim_toplamlari,gun_sayilari,makina_say):
    print("Makina no   Aylık Üretim   Üretim Yaptığı Gün Sayisi   Günlük Ortalama")
    print("---------   ------------   -------------------------   ---------------")
    for makina_no in range(makina_say):
        print(f"{makina_no+1:.9d}",end="   ")
        print(f"{uretim_toplamlari[makina_no]:.12d}",end="   ")
        print(f"{gun_sayilari[makina_no]:.25d}",end="   ")
        try:
            print(f"{uretim_toplamlari[makina_no]/gun_sayilari[makina_no]:.15d.2f}")
        except ZeroDivisionError:




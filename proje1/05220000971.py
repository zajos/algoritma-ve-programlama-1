MIN_BILYE_SAYISI=10
MAX_FARKLI_BILYE=1
diger_kutu="e"
kutudaki_bilye_sayisi=0
kutu_no=1
bilye_mg=0
top_bilye_mg=0
farkli_bilye_sayisi=0
uretim_hatali_kutu_sayisi=0
bilye_mg_fark=0
iade_edilen_bilye=0
kabul_edilen_bilye=0
hepsi_esit_kutu=0
digerlerinden_agir_kutu=0
digerlerinden_hafif_kutu=0
daha_agir_mg_farki_top=0
daha_hafif_mg_farki_top=0
daha_agir_yuzde_top=0
daha_hafif_yuzde_top=0
en_cok_bilye=0
en_cok_bilye_mg=0
en_agir_bilye=0
en_agir_bilye_mg=0
en_agirlik_fark=0
agirlik=""
en_agirlik_hafiflik=""
en_agirlik_yuzde=0
min_agirlik_yuzde=100
min_yuzde_mg_fark=0
min_yuzde_agirlik_hafiflik=""
standart_bilye_mg=0
onceki_bilye_mg=0
iade_edilen_kutu=0
while diger_kutu=="e" or diger_kutu=="E":
    kutudaki_bilye_sayisi=int(input(f"{kutu_no}. kutudaki bilye sayısını giriniz: "))
    while kutudaki_bilye_sayisi<MIN_BILYE_SAYISI:
        kutudaki_bilye_sayisi=int(input(f"Kutuda en az {MIN_BILYE_SAYISI} bilye olmalıdır, lütfen tekrar deneyiniz: "))
    for bilye in range(kutudaki_bilye_sayisi):
        bilye_mg=int(input(f"{bilye+1}. bilyenin mg cinsinden ağırlığını tamsayı olarak giriniz: "))
        while bilye_mg<=0:
            bilye_mg=int(input("Lütfen pozitif bir tamsayı giriniz: "))
        top_bilye_mg += bilye_mg
        if bilye==2 and bilye_mg!=standart_bilye_mg:
            standart_bilye_mg=onceki_bilye_mg
        if farkli_bilye_sayisi==1:
            if standart_bilye_mg!=bilye_mg:
                farkli_bilye_sayisi+=1
        elif top_bilye_mg!=(bilye+1)*bilye_mg:
            standart_bilye_mg= (top_bilye_mg - bilye_mg) / bilye
            onceki_bilye_mg=bilye_mg
            farkli_bilye_sayisi+=1
            bilye_mg_fark=bilye_mg-standart_bilye_mg
        if farkli_bilye_sayisi>MAX_FARKLI_BILYE:
            print("Bu kutuda üretim hatası vardır!")
            uretim_hatali_kutu_sayisi+=1
            iade_edilen_bilye+=kutudaki_bilye_sayisi
            iade_edilen_kutu+=1
            break

    if farkli_bilye_sayisi==0:
        print("Bu kutudaki bilyelerin hepsi eşit ağırlıktadır.")
        hepsi_esit_kutu+=1
        if kutudaki_bilye_sayisi>en_cok_bilye:
            en_cok_bilye=kutudaki_bilye_sayisi
            en_cok_bilye_mg=bilye_mg
        if bilye_mg>en_agir_bilye_mg:
            en_agir_bilye_mg=bilye_mg
            en_agir_bilye=kutudaki_bilye_sayisi
        kabul_edilen_bilye+=kutudaki_bilye_sayisi


    elif farkli_bilye_sayisi==1:
        if bilye_mg_fark>0:
            print(f"Farklı bilye diğerlerinden daha ağırdır. Aradaki fark {abs(bilye_mg_fark)} mg, fark yüzdesi %{(bilye_mg_fark / standart_bilye_mg) * 100:.2f}'dir.")
            digerlerinden_agir_kutu+=1
            daha_agir_mg_farki_top+=bilye_mg_fark
            daha_agir_yuzde_top+= (bilye_mg_fark / standart_bilye_mg) * 100
            agirlik="ağır"
        else:
            print(f"Farklı bilye diğerlerinden daha hafiftir. Aradaki fark {abs(bilye_mg_fark)} mg, fark yüzdesi %{(abs(bilye_mg_fark) / standart_bilye_mg) * 100:.2f}'dir.")
            digerlerinden_hafif_kutu+=1
            daha_hafif_mg_farki_top+=bilye_mg_fark
            daha_hafif_yuzde_top= (bilye_mg_fark / standart_bilye_mg) * 100
            agirlik="hafif"
        if abs(bilye_mg_fark)>en_agirlik_fark:
            en_agirlik_fark=abs(bilye_mg_fark)
            en_agirlik_hafiflik=agirlik
            en_agirlik_yuzde= (abs(bilye_mg_fark) / standart_bilye_mg) * 100
        if (abs(bilye_mg_fark) / standart_bilye_mg)*100<min_agirlik_yuzde:
            min_agirlik_yuzde= (abs(bilye_mg_fark) /standart_bilye_mg) * 100
            min_yuzde_mg_fark=abs(bilye_mg_fark)
            min_yuzde_agirlik_hafiflik=agirlik
        kabul_edilen_bilye += kutudaki_bilye_sayisi
    diger_kutu=input("Girilecek başka bir kutu daha mevcut mu(e/h)?")
    while not (diger_kutu=="e" or diger_kutu=="E" or diger_kutu=="h" or diger_kutu=="H"):
        diger_kutu=input("Lütfen geçerli bir cevap giriniz: ")
    kutu_no+=1
    top_bilye_mg=0
    farkli_bilye_sayisi=0
    standart_bilye_mg=0
kabul_edilen_kutu=(kutu_no-1)-iade_edilen_kutu
print(f"Üretim hatası bulunan kutu sayısı {uretim_hatali_kutu_sayisi}, tüm kutular içindeki yüzdesi %{(100*(uretim_hatali_kutu_sayisi/(kutu_no-1))):.2f}'dir.")
print(f"{iade_edilen_bilye} tane bilye iade edilmiş olup, {kabul_edilen_bilye} tane bilye kabul edilmiştir.")
print(f"{hepsi_esit_kutu} tane kutuda bütün bilyeler eşit ağırlıkta ve bu kutuların iade edilmeyen kutular içindeki yüzdesi %{100*(hepsi_esit_kutu/kabul_edilen_kutu):.2f}'dir")
print(f"{digerlerinden_agir_kutu} tane kutuda bir bilye diğerlerinden daha ağır ve bu kutuların iade edilmeyen kutular içindeki yüzdesi %{100*(digerlerinden_agir_kutu/kabul_edilen_kutu):.2f}'dir")
print(f"{digerlerinden_hafif_kutu} tane kutuda bir bilye diğerlerinden daha hafif ve bu kutuların iade edilmeyen kutular içindeki yüzdesi %{100*(digerlerinden_hafif_kutu/kabul_edilen_kutu):.2f}'dir")
if digerlerinden_agir_kutu!=0:
    print(f"Bir bilyenin diğerlerinden daha ağır olduğu kutulardaki ağır olan bilyelerin ağırlık farkı ortalaması {(daha_agir_mg_farki_top/digerlerinden_agir_kutu):.2f}, yüzde olarak ağırlık farkı ortalaması ise %{(daha_agir_yuzde_top/digerlerinden_agir_kutu):.2f}'dir.")
if digerlerinden_hafif_kutu!=0:
    print(f"Bir bilyenin diğerlerinden daha hafif olduğu kutulardaki hafif olan bilyelerin ağırlık farkı ortalaması {(daha_hafif_mg_farki_top/digerlerinden_hafif_kutu):.2f}, yüzde olarak ağırlık farkı ortalaması ise %{(daha_hafif_yuzde_top/digerlerinden_hafif_kutu):.2f}'dir.")
if hepsi_esit_kutu>0:
    print(f"Tüm bilyelerin eşit ağırlıkta olduğu kutular arasında, içinde en çok bilye olan kutuda {en_cok_bilye} tane bilye vardır ve bu bilyelerin ağırlıkları {en_cok_bilye_mg} mg'dır.")
    print(f"Tüm bilyelerin eşit ağırlıkta olduğu kutular arasında, içinde en ağır bilyelerin bulunduğu kutudaki bilye sayısı {en_agir_bilye}, bu kutudaki bir bilyenin ağırlığı ise {en_agir_bilye_mg}'dır.")
if digerlerinden_hafif_kutu>0 or digerlerinden_agir_kutu>0:
    print(f"Farklı olan bilyenin ağırlığının kutudaki diğer bilyelerin ağırlığıyla arasındaki farkın en büyük olduğu ağırlık farkı {en_agirlik_fark}, ağırlık farkı yüzdesi %{en_agirlik_yuzde:.2f}'dir ve bu bilye diğerlerinden {en_agirlik_hafiflik}'dir.")
    print(f"Farklı olan bilyenin ağırlığının kutudaki diğer bilyelerin ağırlığıyla arasındaki farkın yüzdesinin en küçük olduğu ağırlık farkının değeri {min_yuzde_mg_fark}, yüzdesi %{min_agirlik_yuzde:.2f}'dir ve bu bilye diğerlerinden {min_yuzde_agirlik_hafiflik}'dir.")

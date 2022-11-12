GV_ORANI_DUSUK=15/100
GV_ORANI_ORTA=20/100
GV_ORANI_YUKSEK=25/100
brut_maas_tutari=eval(input("Satış temsilcisinin brüt maaş tutarını giriniz: "))
dusuk=0
orta=0
yuksek=0
daha_yuksek=0
count=0
net_maas_top=0
top_gv_tutar=0
top_brut_maas=0
while brut_maas_tutari>0:
    count+=1
    if brut_maas_tutari<10000:
        dusuk+=1
        gv_tutar=brut_maas_tutari*GV_ORANI_DUSUK
    elif brut_maas_tutari<25000:
        orta+=1
        gv_tutar=brut_maas_tutari*GV_ORANI_ORTA
    else:
        yuksek+=1
        gv_tutar=brut_maas_tutari*GV_ORANI_YUKSEK
        if brut_maas_tutari>50000:
            daha_yuksek+=1
    net_maas=brut_maas_tutari-gv_tutar
    net_maas_top=net_maas_top+net_maas
    daha_yuksek_yuzde=(daha_yuksek/yuksek)*100
    net_maas_ort=net_maas_top/count
    top_gv_tutar=top_gv_tutar+gv_tutar
    top_brut_maas=top_brut_maas+brut_maas_tutari
    gv_tutar_yuzde=(top_gv_tutar/top_brut_maas)*100
    print(f"Devlete ödenecek gelir vergisi tutarı {gv_tutar:.2f}TL, satış temsilcisine ödenecek net maaş tutarı ise {net_maas:.2f}TL'dir.")
    brut_maas_tutari = eval(input("Satış temsilcisinin brüt maaş tutarını giriniz: "))
print(f"Brüt maaş seviyesi yüksek olan {yuksek:.0f} kişi, orta olan {orta:.0f} kişi, düşük olan ise {dusuk:.0f} kişi vardır.")
print(f"Brüt maaş tutarı 50000TL'den fazla olan temsilcilerin brüt maaş seviyesi yüksek olan temsilciler arasındaki yüzdesi {daha_yuksek_yuzde:.2f}%'dir.")
print(f"Tüm satış temsilcilerinin net maaş tutarı ortalaması {net_maas_ort:.2f}TL'dir.")
print(f"Devlete ödenecek toplam gelir vergisi tutarı {top_gv_tutar:.2f}TL, bu tutarın toplam brüt maaşlar içerisindeki yüzdesi ise {gv_tutar_yuzde:.2f}%'dir.")


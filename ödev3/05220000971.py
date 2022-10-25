#Mevlüt Emre OKUMUŞ - 05220000971 - Ödev 3
KATILIMCI=14
NS_MAC_SAYI=(KATILIMCI-1)*2
yas=int(input("Yaşınızı giriniz: "))
son_yillik_ucret=eval(input("Son yıllık ücretinizi giriniz(TL): "))
ns_sonu_sira=int(input("Takımınızın normal sezon sonundaki sırasını giriniz: "))
if ns_sonu_sira<=8:
    poff_mac_sayi=int(input("Takımınızın playoff sezonunda oynadığı maç sayısını giriniz: "))
    top_mac_sayi=NS_MAC_SAYI+poff_mac_sayi
else:
    top_mac_sayi=NS_MAC_SAYI
mac_maliyet=son_yillik_ucret/top_mac_sayi
if yas<22:
    sk_hak=False
else:
    sk_hak=True
    if yas==22:
        sk_bedel=son_yillik_ucret*2
    elif yas==23:
        sk_bedel=son_yillik_ucret
    elif yas==24:
        sk_bedel=son_yillik_ucret/2
    else:
        sk_bedel=0
print(f"Oynadığınız maç başına takımınıza maliyetiniz: {mac_maliyet:.2f} TL.")
if not sk_hak:
    print("Serbest kalma(takımınızdan ayrılma) hakkınız bulunmamaktadır.")
else:
    print(f"Serbest kalma(takımınızdan ayrılma) hakkınız bulunmaktadır, serbest kalma bedeliniz: {sk_bedel:.2f} TL.")
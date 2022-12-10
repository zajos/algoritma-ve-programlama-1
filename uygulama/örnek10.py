def notlari_al(notlar):
    devam="e"
    while devam in ["e","E"]:
        bir_not=input("Sıradaki öğrencinin notunu giriniz: ")
        notlar.append(bir_not)
        devam=input("Başka öğrenci var mı (e/h)? ")

def istatistikler(notlar):
    ogr_say=len(notlar)
    sinif_ort=sum(notlar)/ogr_say
    fark_kare_top=0
    ort_ustu_say=0
    for i in range(ogr_say):
        fark_kare_top+=(notlar[i]-sinif_ort)**2
        if notlar[i]>sinif_ort:
            ort_ustu_say+=1
    try:
        std_sapma=(fark_kare_top/(ogr_say-1))**0.5
    except ZeroDivisionError:
        print("Tek öğrenci için standart sapma hesaplanamaz.")
    print("Sınıf ortalaması:",sinif_ort)
    print(f"Standart sapma: {std_sapma}")
    print("Ortalama üstü öğrenci sayısı:",ort_ustu_say)
    print("Maksimum not:",max(notlar))

def main():
    notlar=[]
    notlari_al(notlar)
    istatistikler(notlar)

main()





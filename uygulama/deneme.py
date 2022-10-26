LAB_KATSAYI=0.2
ARASINAV_KATSAYI=0.3
FINAL_KATSAYI=0.5
ogr_no=input("Öğrenci Numarası: ")
ad_soyad=input("Ad Soyad: ")
lab_not=eval(input("Lab notu: "))
ara_not=eval(input("Ara sınav notu: "))
final_not=eval(input("Final sınavı notu: "))
donem_son_not=round(LAB_KATSAYI*lab_not+ARASINAV_KATSAYI*ara_not+FINAL_KATSAYI*final_not)
print(f"Öğrenci no:{ogr_no}\nAd Soyad:{ad_soyad}\nLab Notu:{lab_not}\nAra Sınav Notu:{ara_not}\nFinal Notu:{final_not}\nDönem sonu notu:{donem_son_not}")
AYLIK_BURS=450
NOT_BURS_ORANI=55
EK_BURS=250
MIN_NOT=2
ASGARI_UCRET=5500
ad_soyad=input("Adınızı ve soyadınızı giriniz:")
not_ortalama=eval(input("4 üzerinden not ortalamanızı giriniz: "))
cinsiyet=input("Cinsiyetinizi giriniz: ")
burs=AYLIK_BURS
if cinsiyet=="kız" or cinsiyet=="KIZ" or cinsiyet == "Kız":
    aylik_gelir=eval(input("Aylık gelirinizi giriniz: "))
if (cinsiyet=="kız" or cinsiyet=="KIZ" or cinsiyet == "Kız") and aylik_gelir < ASGARI_UCRET:
    burs=burs+EK_BURS
if not_ortalama>=MIN_NOT:
    burs=burs+not_ortalama*NOT_BURS_ORANI
print(f"{ad_soyad} isimli öğrencinin aylık burs miktarı {burs:.2f} TL'dir")


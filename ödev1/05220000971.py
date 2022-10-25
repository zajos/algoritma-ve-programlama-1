ogr_no=input("Öğrenci numaranızı giriniz: ")
ad_soyad=input("Adınızı ve soyadınızı giriniz: ")
ders1_tds=eval(input("Aldığınız ilk dersin haftalık teorik ders saatini giriniz: "))
ders1_uds=eval(input("Aldığınız ilk dersin haftalık uygulama ders saatini giriniz: "))
ders1_akts=eval(input("Aldığınız ilk dersin haftalık AKTS kredisini giriniz: "))
ders1_not=eval(input("Aldığınız ilk dersin dönem sonu notunu giriniz: "))
ders2_tds=eval(input("Aldığınız ikinci dersin haftalık teorik ders saatini giriniz: "))
ders2_uds=eval(input("Aldığınız ikinci dersin haftalık uygulama ders saatini giriniz: "))
ders2_akts=eval(input("Aldığınız ikinci dersin haftalık AKTS kredisini giriniz: "))
ders2_not=eval(input("Aldığınız ikinci dersin dönem sonu notunu giriniz: "))
der1_y_kredi=ders1_tds+(ders1_uds/2)
ders2_y_kredi=ders2_tds+(ders2_uds/2)
top_y_kredi=ders2_y_kredi+der1_y_kredi
top_akts=ders2_akts+ders1_akts
kredi_agno=(der1_y_kredi*ders1_not+ders2_y_kredi*ders2_not)/top_y_kredi
akts_agno=(ders1_akts*ders1_not+ders2_akts*ders2_not)/top_akts
print(f"Öğrenci numarası: {ogr_no}\nAdı ve soyadı: {ad_soyad}\nBu dönem aldığı toplam yerel kredi miktarı:\
{top_y_kredi:.2f}\nBu dönem aldığı toplam AKTS kredi miktarı: {top_akts:.2f}\n\
Yerel krediye göre bu dönem sonu AGNO: {kredi_agno:.2f}\nAKTS’ye göre bu dönem sonu AGNO: {akts_agno:.2f}")


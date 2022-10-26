BIRIM_UCRET=53.45
HAFTALIK_NORMAL_SURE=40
FAZLA_MESAI_ORANI=1.5
calisma_suresi=int(input("Haftalık çalışma süresini tamsayı olarak giriniz: "))
if calisma_suresi<=HAFTALIK_NORMAL_SURE:
    ucret=calisma_suresi*BIRIM_UCRET
else:
    ucret=HAFTALIK_NORMAL_SURE*BIRIM_UCRET+(calisma_suresi-HAFTALIK_NORMAL_SURE)*FAZLA_MESAI_ORANI*BIRIM_UCRET
print(f"Haftalık çalışma ücretiniz {ucret:.2f} TL")

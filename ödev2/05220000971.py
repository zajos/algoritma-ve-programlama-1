team1_ad=input("İlk takımın adını giriniz: ")
team1_set=int(input(f"{team1_ad} takımının kazandığı set adedini giriniz: "))
team2_ad=input("İkinci takımın adını giriniz: ")
team2_set=int(input(f"{team2_ad} takımının kazandığı set adedini giriniz: "))
if team1_set>team2_set:
    kazanan=team1_ad
    kazanan_set=team1_set
    kaybeden=team2_ad
    kaybeden_set=team2_set
else:
    kazanan=team2_ad
    kazanan_set=team2_set
    kaybeden=team1_ad
    kaybeden_set=team1_set
if kazanan_set==3 and kaybeden_set==2:
    kazanan_puan=2
    kaybeden_puan=1
else:
    kazanan_puan=3
    kaybeden_puan=0
print(f"Maçı kazanan takımın adı: {kazanan}, kazandığı puan: {kazanan_puan}\nMaçı kaybeden takımın adı: {kaybeden}\
, kazandığı puan: {kaybeden_puan}")


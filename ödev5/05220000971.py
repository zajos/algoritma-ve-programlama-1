kazanilan_set=0
kaybedilen_set=0
macta_kazanilan_sayi=0
macta_kaybedilen_sayi=0
toplam_kaz_sayi=0
kazanilan_mac=0
kaybedilen_mac=0
set_kaybetmeden_kaz_mac=0
set5=0
kazanilan_kaybedilen_farki2=0
toplam_mac=int(input("Takımın bir sezonda oynadığı toplam maç adedini giriniz: "))
for mac in range(toplam_mac):
    rakip_takim_ad=input("Rakip takımın adını giriniz: ")
    for set in range(5):
        kazanilan_sayi_set=int(input(f"{set+1}. sette kazandığınız sayı adedi: "))
        kaybedilen_sayi_set=int(input(f"{set+1}. sette kaybettiğiniz sayı adedi: "))
        if kazanilan_sayi_set>kaybedilen_sayi_set:
            kazanilan_set+=1
        else:
            kaybedilen_set+=1
        if kazanilan_set==3 or kaybedilen_set==3:
            break
        macta_kazanilan_sayi+=kazanilan_sayi_set
        macta_kaybedilen_sayi+=kaybedilen_sayi_set
    if kazanilan_set>kaybedilen_set:
        kazanilan_mac+=1
    else:
        kaybedilen_mac+=1
    if kaybedilen_set==0:
        set_kaybetmeden_kaz_mac+=1
    if kazanilan_set+kaybedilen_set==5:
        set5+=1
    kazanilan_kaybedilen_farki=abs(macta_kazanilan_sayi-macta_kaybedilen_sayi)
    if kazanilan_kaybedilen_farki>=kazanilan_kaybedilen_farki2:
        the_mac_toplam_sayi_fark=kazanilan_kaybedilen_farki
        the_rakip_takim_ad=rakip_takim_ad
    kazanilan_kaybedilen_farki2=the_mac_toplam_sayi_fark
    print(f"Maçta toplam {macta_kazanilan_sayi} sayı kazanılmıştır.")
    print(f"Maçta toplam {macta_kaybedilen_sayi} sayı kaybedilmiştir.")
    print(f"Maçta toplam {kazanilan_set} set kazanılmıştır.")
    print(f"Maçta toplam {kaybedilen_set} set kaybedilmiştir.")
    set_basina_kaz_say_ort=macta_kazanilan_sayi/(kazanilan_set+kaybedilen_set)
    set_basina_kayb_say_ort=macta_kaybedilen_sayi/(kazanilan_set+kaybedilen_set)
    print(f"Set başına kazanılan sayı ortalaması {set_basina_kaz_say_ort}, set başına kaybedilen sayı ortalaması {set_basina_kayb_say_ort}'dir.")
    toplam_kaz_sayi+=macta_kazanilan_sayi
    mac_basina_sayi_ort=toplam_kaz_sayi/toplam_mac
    macta_kazanilan_sayi=0
    macta_kaybedilen_sayi=0
    kazanilan_set=0
    kaybedilen_set=0
print(f"Takımın sezonda kazandığı toplam sayı adedi {toplam_kaz_sayi}, maç başına kazandığı sayı ortalaması {mac_basina_sayi_ort}'dir.")
print(f"Takımın sezonda kazandığı maç sayısı {kazanilan_mac}, kaybettiği maç sayısı {kaybedilen_mac}'dır.")
print(f"Takımın sezonda set kaybetmeden kazandığı maç sayısı {set_kaybetmeden_kaz_mac}, bunun tüm maçlar içindeki oranı ise {set_kaybetmeden_kaz_mac/toplam_mac}'dir.")
print(f"Takımın sezonda 5 sette biten maç sayısı {set5}, bunun tüm maçlar içindeki oranı ise {set5/toplam_mac}'dir.")
print(f"Takımın kazandığı toplam sayı ile kaybettiği toplam sayı arasındaki farkın en yüksek olduğu maçtaki kazanılan sayı ve kaybedilen sayı farkı {the_mac_toplam_sayi_fark}, bu maçtaki rakip takım ise {the_rakip_takim_ad}'dir.")

def input_al(min_deger,prompt1,prompt2,prompt3):
    try:
        variable=int(input(prompt1))
    except ValueError:
        while True:
            try:
                variable = int(input(prompt2))
                break
            except ValueError:
                print("Girdiğiniz değer bir tamsayı olmalıdır.")
    while variable<min_deger:
        variable= int(input(prompt3))
    return(variable)

def kullanici_inputs():

    MIN_SPORCU_SAY=8
    x_puan=0
    on_puan=0
    sporcu_bilgiler=[]
    sporcular=[]
    sporcu_sayisi=input_al(min_deger=MIN_SPORCU_SAY,prompt1="Yarışmaya katılan sporcu sayısını giriniz: ",prompt3=f"En az\
 {MIN_SPORCU_SAY} sporcu olmalıdır. Lütfen tekrar deneyiniz: ",prompt2="Lütfen tekrar deneyiniz: ")
    atis_hakki=input_al(min_deger=0,prompt1="Sporculara verilen atış hakkı sayısını giriniz: ",prompt3="Lütfen tekrar deneyiniz: ",prompt2="Lütfen tekrar deneyiniz: ")

    for sporcu in range(sporcu_sayisi):
        ad_soyad=input(f"{sporcu+1}. sporcunun adını ve soyadını giriniz: ")
        sporcu_puan=0
        for atis in range(atis_hakki):
            atis_puan=input_al(min_deger=0,prompt1=f"Sporcunun {atis+1}. atıştaki puanını giriniz: ",prompt3="Lütfen tekrar deneyiniz: ",prompt2="Lütfen tekrar deneyiniz: ")
            while atis_puan>10:
                atis_puan=input_al(min_deger=0,prompt1="En fazla 10 puan alınabilir. Lütfen tekrar deneyiniz: ",prompt3="Lütfen tekrar deneyiniz: ",prompt2="Lütfen tekrar deneyiniz: ")
            if atis_puan<5:
                atis_puan=0
            if atis_puan==10:
                x_sayisi=input("Atış X bölgesine isabet etti mi(e/h)? ")
                while not(x_sayisi=="e" or x_sayisi=="E" or x_sayisi=="h" or x_sayisi=="H"):
                    x_sayisi=input("Lütfen tekrar deneyiniz: ")
                if x_sayisi=="e" or x_sayisi=="E":
                    x_puan+=1
                on_puan+=1
            sporcu_puan += atis_puan
        sporcu_bilgiler.append(ad_soyad)
        sporcu_bilgiler.append(sporcu_puan)
        sporcu_bilgiler.append(on_puan)
        sporcu_bilgiler.append(x_puan)
        sporcular.append(sporcu_bilgiler)
        x_puan = 0
        on_puan = 0
    return(sporcu_sayisi,sporcular)

def sirala():

    sporcular=kullanici_inputs()[1]
    sporcu_puanlar=[]
    sirali_puanlar=[]
    on_puanlar=[]
    x_puanlar=[]
    MIN_SIRA = 1
    sirali_sporcular=[]
    for sporcu in range(len(sporcular)):
        sporcu_puan=(sporcular[sporcu])[1]
        on_puan=(sporcular[sporcu])[2]
        x_puan=(sporcular[sporcu])[3]
        sporcu_puanlar.append(sporcu_puan)
        on_puanlar.append(on_puan)
        x_puanlar.append(x_puan)
    while sporcu_puanlar!=[]:
        sirali_puanlar.append(max(sporcu_puanlar))
        sporcu_puanlar.remove(max(sporcu_puanlar))
    for sporcu in range(len(sporcular)):
        for sira in range(len(sirali_puanlar)):
            if sirali_puanlar[sira] in sporcular[sporcu]:

                if (sira+1) <= (len(sirali_puanlar) - 1):
                    if sirali_puanlar[sira] == sirali_puanlar[sira + 1] :
                        for sporcu_ic in range(len(sporcular)):
                            if sirali_puanlar[sira+1] in sporcular[sporcu_ic]:
                                if on_puanlar[sporcu_ic]>on_puanlar[sporcu]:
                                    sporcular[sporcu_ic].append(sira+1)
                                elif on_puanlar[sporcu_ic] < on_puanlar[sporcu]:
                                    sporcular[sporcu].append(sira+1)
                                elif x_puanlar[sporcu_ic] < x_puanlar[sporcu]:
                                    sporcular[sporcu].append(sira+1)
                                elif x_puanlar[sporcu_ic] > x_puanlar[sporcu]:
                                    sporcular[sporcu_ic].append(sira+1)
                    else:
                        sporcular[sporcu].append(sira+1)

        for index in range(len(sporcular)):

            if (sporcular[index])[4]==MIN_SIRA:
                sirali_sporcular.append(sporcular[index])
        MIN_SIRA+=1

    print("Sıra   Ad Soyad            Puan   10 Sayısı   X Sayısı")
    print("----   --------            ----   ---------   --------")
    for i in range(len(sporcular)):
        print(f"{(sporcular[i])[4]}   {(sporcular[i])[0]}            {(sporcular[i])[1]}   {(sporcular[i])[2]}   {(sporcular[i])[3]}")

sirala()









def kuvvet(taban_sayisi,us):
    if us==0:
        return 1
    else:
        return taban_sayisi*kuvvet(taban_sayisi, us-1)
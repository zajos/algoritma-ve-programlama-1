X_MIN=-3
X_MAX=3
Y_MIN=-3
Y_MAX=3
f_toplam=0
gecersiz_durumlar=0
durum_sayisi=0
for x in range(X_MIN,X_MAX+1):
    for y in range(Y_MIN,Y_MAX+1):
        if x+y!=0:
            f=(2*x+3*y-4*x*y+5)/(x+y)
            f_toplam+=f
            print(f"f({x},{y})={f}")
            durum_sayisi+=1
        else:
            print(f"{x} ve {y} değerleri için geçersizdir.")
            gecersiz_durumlar+=1
print(f"ortalama={f_toplam/durum_sayisi}")

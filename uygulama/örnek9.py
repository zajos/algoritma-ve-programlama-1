from cember import cemberCevre
import kuvvet
import math

yaricap=float(input("Bir yarıçap değeri giriniz: "))
cevre=cemberCevre(r=yaricap)
print("Çemberin çevresi:",cevre)
cevre= cemberCevre(r=yaricap,pi=math.pi)
print("Çemberin çevresi:",cevre)
print(f"2 üzeri 4 = {kuvvet.kuvvet(2,4)}")
taban=int(input("tabanı giriniz:"))
us=int(input("üssü giriniz: "))
print(kuvvet.kuvvet(taban,us))
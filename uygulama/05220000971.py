urun_ad=input("Ürünün adını yazınız: ")
buay_fiyat=eval(input("Ürünün bu ayki fiyatını yazınız: "))
gecenay_fiyat=eval(input("Ürünün geçen ayki fiyatını yazınız: "))
aylik_deg_miktar=abs(buay_fiyat-gecenay_fiyat)
aylik_deg_yuzde=(aylik_deg_miktar/gecenay_fiyat)*100
print(f"{urun_ad} ürününün fiyatındaki aylık değişim miktarı {aylik_deg_miktar:.2f}$, aylık değişim yüzdesi %{aylik_deg_yuzde:.2f}'dir.")
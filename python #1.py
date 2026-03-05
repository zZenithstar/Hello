#İlk defa python kullanıyorum hadi bakalımmm!...
print("ismim İbrahim YILDIZ")
print("Ben Giresun Üniversitesinde okuyorum")
print("Bölümümde Bilgisayar Mühendisliği")

#biraz değişkenli yapalım string float integer boolen gibi
#str and int
isim = "İbrahim"
yas = 19
cinsiyet = "erkek"

print(f"Merhaba {isim} tanıştığımıza memnun oldum.")
print(f"Yaşını gözlerinden tahmin edebilirim... kesin sen {yas} yaşında bir {cinsiyet}sin...")
yas = 20
yas = str(yas)
print(type(yas))

#isim = input("İsmin Nedir?:")
#yas = int(input("Yaşın Kaç?:"))
#yas = yas + 1
#print(f"Merhaba{isim}!")
#print("Yarın Senin Doğum Günün!!")
#print(f"O günden sonra {yas} yaşında olacaksın yuppii!!!")
"""
#alan hesabı
uzunluk1 = float(input("Uzunluğu giriniz:"))
uzunluk2 = float(input("Uzunluğu giriniz:"))
alan = uzunluk1 * uzunluk2
print(f"Alanınız {alan:.2f} ")
"""

#alısverıs algorıtması
esya = input("Ne almak istersiniz?:")
fiyat = float(input("Fiyatı ne kadar?:"))
adet = float(input("Adet ne kadar?:"))
toplam = adet * fiyat
print(f"satın aldığınız {adet} x {esya}/lar ")
print(f"Toplam ödemeniz gereken tutar: {toplam}₺")














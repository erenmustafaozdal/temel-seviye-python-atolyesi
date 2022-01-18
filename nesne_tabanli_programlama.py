"""
Nesne tabanlı programlama ile ortak niteliklere ve davranış şekillerine sahip
gruplar tanımlamamızı sağlar. (?)

ÖRNEK:
--------
Öğrenci bilgilerini tutan bir veritabanımız var. Veri tabanındaki her satır bir
öğrenciyi temsil ediyor.

Öğrenci
- Okul
- No
- Ad
- Soyad
- Doğum Yılı
...

Yukarıdaki örnek öğrenci bilgilerine yazılımda karşılık gelen nesne (class)
oluşturalım. Bu öğrenci nesnesinin okul, no, ad, soyad, dogum_yili
özellikleri (attributes) olsun. Ayrıca doğum tarihinden otomatik yaş hesaplayan
bir davranışı (method) olsun.
"""


# Öğrenci nesnesine ait sınıfı tanımlayalım
#   ⚪ Okul her öğrenciye göre değişmeyeceği senaryosu üzerinden; okul
#       değişkenini sınıf özelliği olarak ekleyelim
#   ⚪ No, Ad, Soyad ve Doğum Yılı her öğrenciye göre değişeceği örnek
#       özelliği tanımlayacağız
#   ⚪ Öğrencinin adını ve soyadını birleştirip döndüren metot ekleyelim
#   ⚪ Öğrencinin yaşını hesaplayıp döndüren metot ekleyelim
class Ogrenci:

    okul = "Halime Hatun İlkokulu"

    def __init__(self, no, ad, soyad, dogum_yili):
        self.ogrenci_no = no
        self.ogrenci_ad = ad
        self.ogrenci_soyad = soyad
        self.ogrenci_dy = dogum_yili

    def ad_soyad(self):
        return self.ogrenci_ad + " " + self.ogrenci_soyad

    def yas(self, buyil):
        return buyil - self.ogrenci_dy


# ayrı nesne örnekleri oluşturduk
# ahmet = Ogrenci()
# print(ahmet)
# print(ahmet.okul)
# ayse = Ogrenci()

# Sınıfın (nesnenin) bir örneğini oluşturalım ve değişkene atayalım
# Ardından farklı örneklerini de oluşturalım
ogrenci = Ogrenci(12, "Eren", "Özdal", 2012)
# print(ogrenci)
# print(ogrenci.ogrenci_no)
# print(ogrenci.ogrenci_ad)
# print(ogrenci.ogrenci_soyad)
# print(ogrenci.ogrenci_dy)
# print(ogrenci.ad_soyad())
# print(ogrenci.ogrenci_ad + " " + ogrenci.ogrenci_soyad)  # bunu kullanma
print(ogrenci.yas(2022))

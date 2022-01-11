# METOT: range()
# //////////////////////////////////////////////////////////////////////////////
# range() fonksiyonunu belli bir aralıkta bulunan sayıları göstermek
# için kullanıyoruz.

# 1-10 sayılarından oluşan bir liste oluşturup ekrana yazdıralım
liste = list(range(1, 10))
# print(liste)

# Ekrana 50 defa Python yazdıralım
# for i in range(50):
#     print(f"{i+1}: Python")

# 100-200 arasındaki çift sayıları ekrana 1 saniye bekleyerek yazdıralım
# import time
#
# for i in range(100,200):
#     if i % 2 == 0:
#         print(i)
#         time.sleep(1)


# METOT: enumerate()
# //////////////////////////////////////////////////////////////////////////////
# İngilizcede enumerate kelimesi ‘numaralandırmak’ anlamına gelir. enumerate()
# fonksiyonunun görevi de kelimenin bu anlamıyla aynıdır. Yani bu fonksiyonu
# kullanarak nesneleri numaralandırabiliriz.

# "python" kelimesini enumerate ile numaralandıralım ve liste içine ekleyelim.
# Ardından ekrana yazdıralım
kelime = "python"
# kelime_enum = list(enumerate(kelime))
# print(kelime_enum)

# for döngüsü içinde numarası ile birlikte ekrana yazdıralım
# for i, harf in enumerate(kelime):
#     print(i, harf)


# METOT: zip()
# //////////////////////////////////////////////////////////////////////////////

# Sayılardan ve o sayıların okunuşlarından oluşan iki liste tanımlayalım
sayilar = [1, 2, 3]
okunus = ["bir", "iki", "üç"]

# Bu listeleri zip() ile birleştirip, liste içine alıp ekrana yazdıralım
# sayilar_zip = list(zip(sayilar, okunus))
# print(sayilar_zip)

# for döngüsü içinde sayıları ve okunuşlarını ekrana yazdıralım
for sayi, oku in zip(sayilar, okunus):
    print(sayi, oku)

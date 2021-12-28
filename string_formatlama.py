# Değişkenlerimize str verileri ekleyelim
ad = "Eren"
soyad = "Özdal"
yas = "35"

# Bir karakter dizisinin içine değişkenimizdeki verileri yerleştirelim: format()
# Adınız: Eren, soyadınız: Özdal, yaşınız: 35
# print("Adınız: " + ad + ", soyadınız: " + soyad + ", yaşınız: " + yas)
# print("Adınız: {}, soyadınız: {}, yaşınız: {}".format(ad, soyad, yas))

# Formatlama esnasında değişken sıralarını değiştirelim
# print("Adınız: {1}, soyadınız: {2}, yaşınız: {0}".format(ad, soyad, yas))

# Formatlama esnasında değişkenlere isimler verelim
# print("Adınız: {x}, soyadınız: {y}, yaşınız: {z}".format(x=ad, y=soyad, z=yas))

# f string ile karakter dizisini formatlama
# print(f"Adınız: {ad}, soyadınız: {soyad}, yaşınız: {yas}")

# UYGULAMA
# //////////////////////////////////////////////////////////////////////////////
url = "https://istanbulakademi.meb.gov.tr/akademiler.php?pID=759"
atolye  = "Temel Seviye Python Atölyesi"

# 1- 'url' içinde kaç karakter bulunmaktadır ?

# 2- 'url' içinden istanbulakademi karakterlerini alın
# print(url[8:23])

# 3- 'url' içinden kurs ID'sini karakterlerini alın
# print(url[-3:])

# 4- 'atolye' ifadesindeki karakterleri tersten yazdırın
# print(atolye[::-1])

# 5- 'İstanbul öğretmen Akademileri' ifadesindeki ö harfini 'Ö' ile değiştirin.

# 6- 'abc' ifadesini yan yana 5 defa yazdırın.
print("Yazılar")
print("-"*50)
print("Başka Yazılar")

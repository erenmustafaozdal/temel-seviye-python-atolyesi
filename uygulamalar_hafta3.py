# UYGULAMALAR
# Her uygulama örneği bir yorum parçasının altına yapılabilir
# //////////////////////////////////////////////////////////////////////////////

sayilar = [4, 6, 18, 25, 30, 37, 41, 48, 50, 55, 58]
# 1- sayilar listesini while ile ekrana yazdıralım

# 2- sayilar listesindeki sayılardan 3'ün katı olanları ekrana yazdıralım

# 3- sayilar listesindeki sayilarin toplamını ekrana yazdıralım

ogrenciler = ["Eren", "Mustafa", "Sultan", "Zeynep", "Nazlı", "Sare", "Ahmet"]
# 4- Öğrencilerden ismi sesli harfle başlayanları ekrana yazdırın

ogrenci_sinavlari = [
    {"ad": "Eren", "notlar": [90, 72]},
    {"ad": "Mustafa", "notlar": [40, 55]},
    {"ad": "Sultan", "notlar": [81, 95]},
    {"ad": "Zeynep", "notlar": [90, 96]},
    {"ad": "Nazlı", "notlar": [56, 40]},
    {"ad": "Sare", "notlar": [46, 40]},
    {"ad": "Ahmet", "notlar": [70, 70]},
]
# 5- Öğrenci sınav notu ortalamalarını ekrana yazdıralım
# ➡ Ör: Eren isimli öğrencinin not ortalaması: 55


# 6- Öğrencilerden 2. sınavda notunu artıranları tebrik edelim

# 7- Sayi tahmin oyunu yapalım
#   Öğrenci sayıyı tahmin eder: input()
#   Sayımızdan küçük bir sayı tahmin edildiyse "Yukarı" yazdıralım
#   Sayımızdan büyük bir sayı tahmin edildiyse "Aşağı" yazdıralım
#   Sayımızı bulduruğunda tebrik edelim
import random  # rastgele modülünü içeri aktardık
sayi = random.randint(1,10)  # 1-10 arası rastgele tam sayı ürettik

# 8- Yukarıdaki öğrencileri ve aşağıdaki numaraları zip ile birleştirip ekrana
# döngü içinde yazdıralım
numaralar = [66, 102, 82, 654, 182, 45, 59]

# 9- Öğrencinin dakikada okuduğu kelime sayısını ve sınıf bilgisini alalım.
# Aldığımız bilgileri aşağıdaki tablo ile karşılaştıralım. Aralığın altında
# ise "düşük", aralık içinde ise "normal", aralığın üstünde ise "yüksek"
# ifadelerini ekrana yazdıralım.
# +-------+-----------------------+
# | Sınıf | Kelime/Dakika Aralığı |
# +-------+-----------------------+
# | 1     | 50 - 70               |
# +-------+-----------------------+
# | 2     | 70-80                 |
# +-------+-----------------------+
# | 3     | 80-90                 |
# +-------+-----------------------+
# | 4     | 90-100                |
# +-------+-----------------------+

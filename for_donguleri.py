"""
Python'da kullanabileceğimiz 2 tane döngü tipinden birisi for'dur.
Tekrarlayacak işlemlerimizde döngüleri kullanırız.
"for" döngüsü bir eleman grubundaki her elemana sırayla ulaşmak için kullanılır.
"""

# Öğrenci isimlerinden oluşan bir liste oluşturalım
ogrenciler = ["Eren", "Mustafa", "Sultan", "Zeynep"]

# Listenin her elemanını ekrana yazdıralım: for ogrenci in ogrenciler
# for isim in ogrenciler:
#     print(isim)

# Listenin her elemanını bir metin içinde ekrana yazdıralım.
# ➡ Ör: Öğrencinin adı Eren
# for ogrenci in ogrenciler:
#     print(f"Öğrencinin adı: {ogrenci}")

# İçinde ikili sayılardan oluşan tuple'ların yer aldığı bir liste oluşturalım.
sayilar = [(1,2), (5,9), (16,12)]

# tuple içindeki sayılara ulaşıp yazdıralım: for a,b in sayilar
# for a, b in sayilar:
#     print(a, b)

# Aşağıdaki string'in içindeki karakterlere ulaşıp ekrana yazdıralım
atolye = "Temel Seviye Python Atölyesi"
# for k in atolye:
#     print(k)

# Öğrencilerin yer aldığı dict
ogrenciler_dict = {
    66: {
        "ad": "Eren",
        "soyad": "Özdal",
        "cinsiyet": True,
        "dersler": ["Matematik", "Fen Bilimler"]
    },
    75: {
        "ad": "Sultan",
        "soyad": "Demir",
        "cinsiyet": False,
        "dersler": ["Türkçe", "Hayat Bilgisi"]
    }
}

# Öğrencilerin numaralarını ekrana yazdıralım
# for no in ogrenciler_dict.keys():
#     print(no)

# Öğrencilerin numara, isim ve derslerini ekrana yazdıralım
# ➡ Ör: 66 nolu Eren isimli öğrencinin dersleri: Matematik, Fen Bilimleri
for no, bilgiler in ogrenciler_dict.items():
    print(f"{no} nolu {bilgiler['ad']} isimli öğrencinin dersleri: {'-'.join(bilgiler['dersler'])}")

"""
Dictionary "anahtar", "değer" ikililerinden oluşur
    66 => Eren
    75 => Mustafa
"""

# Belirli bir numaraya sahip öğrenciyi bulma işlemini liste ile yapalım
# numaralar = [66, 75]
# isimler = ["Eren", "Mustafa"]
# numara = int(input("Öğrenci No Yazınız: "))
# indis = numaralar.index(numara)
# print(f"{numara} nolu öğrenci {isimler[indis]}")

# Belirli bir numaraya sahip öğrenciyi bulma işlemini dict ile yapalım
dictionary = {66: "Eren", 75: "Mustafa"}
# numara = int(input("Öğrenci No Yazınız: "))
# print(f"{numara} nolu öğrenci {dictionary[numara]}")

# Dict verisini ekrana yazdıralım
# print(dictionary)
# print(type(dictionary))

# Dict'e yeni veri ekleyelim
dictionary[95] = "Sultan"
# print(dictionary)

# Detaylı Örnek

ogrenciler = {
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

print(ogrenciler[66]["dersler"])

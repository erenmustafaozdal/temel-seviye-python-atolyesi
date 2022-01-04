# Boş liste tanımlayalım -> []
liste = []
# print(liste)
# print(type(liste))

kelimeler  = "Temel Seviye Python Atölyesi".split()
# Kelimeleri ekrana yazdır
# ['Temel', 'Seviye', 'Python', 'Atölyesi']
# print(kelimeler)

# Belirli sıradaki kelimeleri ekrana yazdır
# print(kelimeler[0])
# print(kelimeler[1])
# print(kelimeler[2])
# print(kelimeler[3])
# print(kelimeler[4])  # hata

# Yeni bir liste tanımlayıp ekrana yazdıralım
liste2 = [1, 25, "Python", True, 12.6, [1, 2, 3] ]
# print(liste2)

# İki liste tanımlayıp, bu listeleri birleştirelim
liste3 = [1, 2, 3]
liste4 = [4, 5, 6]
liste5 = liste3 + liste4
liste6 = liste4 + liste3
print(liste6)

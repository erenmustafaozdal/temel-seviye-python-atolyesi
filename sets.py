"""
✔ sets listeleri süslü parantezler '{}' içinde tanımlanır
✔ sets listelerine indeks numaraları ile ulaşılamaz
✔ sets liste elemanlarına döngü içinde ulaşılır
✔ sets listeleri sıralanamaz
✔ sets listeleri içinde aynı eleman birden fazla yer alamaz
"""

# sets listesi oluşturalım
sets_liste = {1, 2, 3, 4}

# sets listesinin içindeki bir elemana ulaşalım
# print(sets_liste[0])  # hata

# sets listesi elemanlarını ekrana döngü ile yazdıralım
# for x in sets_liste:
#     print(x)

# sets listesine bir eleman ekleyelim: add()
# print("Önce: ", sets_liste)
# sets_liste.add(5)
# print("Sonra: ", sets_liste)
# exit()
# print(sets_liste)

# sets listesine bir veya birden fazla eleman ekleyelim: update([])
sets_liste.update([9, 15, 23])
# print(sets_liste)

# sets listesinden bir eleman silelim: remove()
sets_liste.remove(2)
# print(sets_liste)

# sets listesini temizleyelim: clear()
sets_liste.clear()
# print(sets_liste)

# Tekrarlayan elemanları olan bir listeyi sets listesine çevirelim: set()
liste = [1, 1, 3,8,16,16,1]
sets_liste = set(liste)
print(sets_liste)

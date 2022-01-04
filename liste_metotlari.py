sayilar = [9, 12, 85, 3, 16, 34, 42, 99]
harfler = ['t', 'c', 'a', 'f', 'y', 'm', 's']

# Listenin eleman sayısını bulalım: len(liste)
# print( len(sayilar) )
# print( len(harfler) )

# En küçük değerli elemanı ekrana yazdıralım: min()
# print(min(sayilar))
# print(min(harfler))

# En büyük değerli elemanı ekrana yazdıralım: max()
# print(max(sayilar))
# print(max(harfler))
# print(max(sayilar + harfler))  # string ve int veri tipleri karşılaştırılamıyor
# nums=[1,2,3,4,5]
# letters=["a","b","c","d","e"]
# print(max(nums), max(letters), sep="---")

# Listenin sonuna eleman ekleyelim: append()
sayilar.append(0)
# print(sayilar)

# Listenin istediğimiz konumuna eleman ekleyelim: insert()
harfler.insert(3, "m")
# print(harfler)

# Listenin sonuncu elemanını silelim: pop()
harfler.pop()
# print(harfler)

# Listenin belirli bir indeksindeki elemanı silelim: pop(indeks)
harfler.pop(2)
# print(harfler)

# Listeden belirli bir değere sahip elemanı silelim: remove("değer")
harfler.remove("c")
# harfler.remove("m")
# print(harfler)

# Listedeki elemanları sıralayalım: sort()
# print(sayilar)
# sayilar.sort()
# print(sayilar)
# print("-"*50)
# print(harfler)
# harfler.sort()
# print(harfler)

# Listedeki elemanları ters sıralayalım: reverse()
# print(sayilar)
# sayilar.sort()
# print(sayilar)
# sayilar.reverse()
# print(sayilar)

# Liste içinde bir değerin kaç defa olduğunu bulalım: count()
# print(harfler.count("m"))  # m harfi 2 adet var

# Listeyi temizleyelim: clear()
print(sayilar)
sayilar.clear()
print(sayilar)

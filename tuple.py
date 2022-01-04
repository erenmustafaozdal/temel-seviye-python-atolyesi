liste = [1, 2, 3]
tuple = ('bir', 'iki', 'üç', 'iki')

# Tuple'ı ekrana yazdır
# print(liste)
# print(type(liste))
# print(tuple)
# print(type(tuple))

# Tuple'dan belirli sıradaki elemanı ekrana yazdır
# print(tuple[0])

# Tuple'ın eleman sayısını bulalım: len(tuple)
# print(len(tuple))

# Liste'nin bir elemanını değiştirelim
# Tuple'ın bir elemanını değiştirelim
# liste[0] = 0
# print(liste)
# tuple[0] = "sıfır"
# print(tuple)

# Tuple içinde bir değerin kaç defa olduğunu bulalım: count()
# print(tuple.count("iki"))

# Tuple içindeki belirli bir elemanın indeks numarasını alalım: index()
# print(liste.index(2))
# print(tuple.index("üç"))

# iki tuple'ı birleştirelim
tuple1 = (1, 2, 3)
tuple2 = "bir", "iki", "üç"
tuple3 = tuple1 + tuple2
print(tuple3)

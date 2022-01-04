"""
ATAMA OPERATÖRLERİ
//////////////////////////////////////////////////////////////////////////////
Python'da değişkenlere veri ataması yaparken kullanırız.

+----------+-----------+----------------+
| Operatör | Kullanımı | Uzun Kullanımı |
+----------+-----------+----------------+
| =        | x = y     |                |
+----------+-----------+----------------+
| +=       | x += y    | x = x + y      |
+----------+-----------+----------------+
| -=       | x -= y    | x = x - y      |
+----------+-----------+----------------+
| *=       | x *= y    | x = x * y      |
+----------+-----------+----------------+
| /=       | x /= y    | x = x / y      |
+----------+-----------+----------------+
| %=       | x %= y    | x = x % y      |
+----------+-----------+----------------+
| **=      | x **= y   | x = x ** y     |
+----------+-----------+----------------+
| //=      | x //= y   | x = x // y     |
+----------+-----------+----------------+

"""

# Sayısal verilere sahip 3 adet değişken tanımlayalım
a = 2
b = 3
c = 4
# print(a, b, c)

# Üç değişkene tek satırda veri atayalım
x, y, z = 5, 6, 7
# print(x, y, z)

# Üç değişken içindeki verileri değiştirelim
x, y, z = z, x, y
# print(x, y, z)

# Değişkenin içindeki değere 10 ekleyelim
# x = x + 10
x += 10
# print(x)

# Değişkenin içindeki değerden 10 çıkaralım
# x = x - 10
x -= 10
# print(x)

# Değişkenin içindeki değeri 5 ile çarpalım
# x = x * 5
x *= 5
print(x)

# Değişkenin içindeki değeri 5'e bölelim

# Değişkenin içindeki değerin 5'e bölümünden kalanı bulalım (mod)

# Değişkenin içindeki değeri 4. üssünü alalım

# Değişkenin içindeki değeri 5'e kalansız bölelim

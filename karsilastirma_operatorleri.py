"""
KARŞILAŞTIRMA OPERATÖRLERİ
//////////////////////////////////////////////////////////////////////////////
Python'da değişkenlerin içindeki verileri karşılaştırmak için kullanırız

+----------+----------------+-----------+
| Operatör | Açıklama       | Kullanımı |
+----------+----------------+-----------+
|    ==    | eşit mi?       |   x == y  |
+----------+----------------+-----------+
|    !=    | eşit değil mi? |   x != y  |
+----------+----------------+-----------+
|     >    | büyük mü?      |   x > y   |
+----------+----------------+-----------+
|     <    | küçük mü?      |   x < y   |
+----------+----------------+-----------+
|    >=    | büyük eşit mi? |   x >= y  |
+----------+----------------+-----------+
|    <=    | küçük eşit mi? |   x <= y  |
+----------+----------------+-----------+

"""

kullanici_adi = "eren"  # veritabanından gelen kullanıcı adı olabilir
sifre = "123456"  # veritabanından gelen şifre olabilir

# Kullanıcıdan "kullanıcı adı" ve "şifre" bilgilerini alalım ve yukarıdaki bilgilere "eşit mi?" kontrolü yapalım
# k_kadi = input("Kullanıcı adınız: ")
# k_sifre = input("Şifreniz: ")
# print(f"Kullanıcı adınız: {k_kadi}. Eşitlik durumu: {kullanici_adi == k_kadi}")
# print(f"Şifreniz: {k_sifre}. Eşitlik durumu: {sifre == k_sifre}")

# Kullanıcıdan iki sayı alalım ve birbirine "eşit değil mi?" kontrolü yapalım
# sayi1 = input("Sayı yazınız: ")
# sayi2 = input("Sayı yazınız: ")
# print(f"sayı 1: {sayi1}, sayı 2: {sayi2}. Eşit değil mi?: {sayi1 != sayi2}")

# Kullanıcıdan aldığımız sayıların birbirinden "büyük mü?" kontrolü yapalım
# print(sayi1 > sayi2)

# Kullanıcıdan aldığımız sayıların birbirinden "küçük mü?" kontrolü yapalım

# Kullanıcıdan aldığımız sayıların birbirinden "büyük eşit mi?" kontrolü yapalım

# Kullanıcıdan aldığımız sayıların birbirinden "küçük eşit mi?" kontrolü yapalım

# "erik" kelimesi "erişte" kelimesinden alfabetik olarak
# önce mi gelir kontrolü yapalım
kelime1 = "erik"
kelime2 = "erişte"
print(kelime1 < kelime2)

"""
DİĞER OPERATÖRLER
//////////////////////////////////////////////////////////////////////////////

+----------+------------------+-----------+
| Operatör | Açıklama         | Kullanımı |
+----------+------------------+-----------+
| is       | kimlik operatörü | x is y    |
+----------+------------------+-----------+
| in       | üyelik operatörü | "a" in x  |
+----------+------------------+-----------+

"""

# Tek liste ile 2 farklı ve aynı değerlere sahip diğer bir liste ile de
# 1 değişken oluşturalım
a = b = [1,2,3]
c = [1,2,3]

# Değişkenlerin değer eşitliği (==) ve kimlik eşitliği (is) kontrollerini yapalım
# print(a == b)  # True
# print(a == c)  # True
# print(a is b)  # True
# print(a is c)  # False

dersler = ["Türkçe", "Hayat Bilgisi", "Matematik", "Fen Bilimleri"]
# "Türkçe" dersi dersler listesinin bir üyesi midir?
# print("Türkçe" in dersler)  # True
# print("Müzik" in dersler)  # False

atolye = "Temel Seyive Python Atölyesi"
# "Python" ifadesi atolye değerinin bir üyesi midir?
# print("Python" in atolye)  # True
print("PHP" in atolye)  # False

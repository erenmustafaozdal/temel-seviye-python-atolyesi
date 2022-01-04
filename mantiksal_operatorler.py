"""
MANTIKSAL OPERATÖRLER
//////////////////////////////////////////////////////////////////////////////
Python'da birden fazla koşulu beraber değerlendirmek için kullanırız.

+----------+----------+-----------------+
| Operatör | Açıklama |    Kullanımı    |
+----------+----------+-----------------+
|    and   | ve       | (x<y) and (a>b) |
+----------+----------+-----------------+
|    or    | veya     |  (x<y) or (a>b) |
+----------+----------+-----------------+
|    not   | değil    |    not (x<y)    |
+----------+----------+-----------------+

"""

# Kullanıcıdan "öğretmenlik süresi (yıl)" ve "uzman öğretmenlik sınav notu" alalım.
# Öğretmenlik süresi 10 yıla büyük eşittir ve sınav notu 45 üzerinde ise
# ekrana "True", değilse "False" yazdıralım
# ➡ Örnek ekran çıktısı: Öğretmenlik süreniz: 12 yıl. Sınav Notunuz: 65. Uzman öğretmenlik durumunuz: True
# o_sure = int(input("Öğretmenlik Süreniz: "))
# u_sinav = int(input("Sınav Notunuz: "))
# print(f"Öğretmenlik süreniz: {o_sure} yıl. Sınav Notunuz: {u_sinav}. Uzman öğretmenlik durumunuz: {(o_sure>=10) and (u_sinav>45)}")

# Kullanıcıdan "yüksek lisans" bilgisini "e/h" (evet/hayır) formatında alalım.
# Öğretmenlik süresi 10 yıla büyük eşittir ve sınav notu 45 üzerinde veya
# yüksek lissans yaptı ise ekrana "True", değilse "False" yazdıralım
# ➡ Örnek ekran çıktısı: Öğretmenlik süreniz: 10 yıl. Sınav Notunuz: 30.
#                        Yüksek lisans: e. Uzman öğretmenlik durumunuz: True
# y_lisans = input("Yüksek Lisans Yaptınız mı? (e/h): ")
# kosul = ((o_sure>=10) and (u_sinav>45)) or (y_lisans == "e")
# print(f"Uzman öğretmenlik durumunuz: {kosul}")

# Kullanıcıdan bir sayı alalım. Bu sayının 10 ve 20 arasında olmadığını (değil)
# ekrana "True" veya "False" şeklinde yazdıralım
# ➡ Örnek ekran çıktısı: Girdiğiniz sayı: 5. 10 ve 20 arasında olmama durumu: True
sayi = int(input("Sayı: "))
print(f"Girdiğiniz sayı: {sayi}. 10 ve 20 arasında olmama durumu: {not(10 < sayi < 20)}")

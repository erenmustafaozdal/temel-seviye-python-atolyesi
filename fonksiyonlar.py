"""
Fonksiyonlar, karmaşık işlemleri bir araya toplayarak, bu işlemleri tek adımda
yapmamızı sağlar. Fonksiyonlar çoğu zaman, yapmak istediğimiz işlemler için bir
şablon vazifesi görür. Fonksiyonları kullanarak, bir veya birkaç adımdan
oluşan işlemleri tek bir isim altında toplayabiliriz.

1. Her fonksiyonun bir adı bulunur ve fonksiyonlar sahip oldukları
bu adlarla  anılır.

2. Şekil olarak, her fonksiyonun isminin yanında birer parantez işareti
bulunur. (open(), print(), input(), len() vb.)

3. Bu parantez işaretlerinin içine, fonksiyonlara işlevsellik kazandıran bazı
parametreler yazılır. (open(dosya_adı), print("Merhaba") vb.)

4. Fonksiyonlar farklı sayıda parametre alabilir. Örneğin print() fonksiyonu
toplam 256 adet parametre alabilirken, input() fonksiyonu yalnızca tek bir parametre alır.

5. Fonksiyonların isimli ve isimsiz parametreleri vardır. print() fonksiyonundaki
sep, end ve file parametreleri isimli parametrelere örnekken, mesela print("Merhaba Dünya!")
kodunda "Merhaba Dünya!" parametresi isimsiz bir parametredir.

6. Fonksiyonların, isimli ve isimsiz parametreleri dışında, bir de varsayılan değerli
parametreleri vardır. Örneğin print() fonksiyonunun sep, end ve file parametreleri
varsayılan değerli parametrelere birer örnektir. Eğer bir parametrenin varsayılan
bir değeri varsa, o parametreye herhangi bir değer vermeden de fonksiyonu kullanabiliriz.
"""

# PRINT FONKSİYONU İNCELEMESİ
# //////////////////////////////////////////////////////////////////////////////

# Adı: print
# Tanımlarken ve kullanırken parantez işaretleri kullanılır: print()
# Çalışırken içine parametre alır. 256 adet parametre alabilir.
# sep, end, file isimli ve varsayılan değerli parametrelerdendir.
#   ➡ sep: ' ' (Boşluk karakteri)
#   ➡ end: '\n' (Yeni satır karakteri)
#   ➡ file: None (Dosya yok. Komut istemine çıktı veriyor)
print("Eren", "Özdal", sep="-")

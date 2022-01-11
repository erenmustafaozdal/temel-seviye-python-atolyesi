# 1-10 sayılarını numaralar isimli bir listeye ekleyelim
# numaralar = []
# for sayi in range(1, 10):
#     numaralar.append(sayi)
#
# print(numaralar)

# Yukarıdaki örneği List Comprehensions ile yapalım
# numaralar = [sayi for sayi in range(1, 10)]
# print(numaralar)

# 100-200 arasındaki çift sayıları bir listeye aktaralım
# numaralar = [sayi for sayi in range(100, 200) if sayi % 2 == 0]
# print(numaralar)

# 100-200 arasındaki tek sayılar "{sayi} TEK", çift sayılar için "{sayi} ÇİFT"
# ifadelerini bir listeye aktaralım
# numaralar = [f"{sayi} ÇİFT" if sayi % 2 == 0 else f"{sayi} TEK" for sayi in range(100, 200)]
# print(numaralar)

# Yukarıdaki doğum yıllarını kullanarak öğrencilerin yaşlarını listeye aktaralım

# Aşağıdaki işlemi List Comprehensions ile tekrar yapalım
result = []
for x in range(3):
    for y in range(3):
        result.append((x,y))

print(result)

sonuc = [(x, y) for x in range(3) for y in range(3)]

print(sonuc)

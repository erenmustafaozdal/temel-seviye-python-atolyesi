"""
break: döngüyü sonlandırır
continue: döngünün ilgili turunu sonlandırır
"""

# 0'dan 10'a kadar olan sayıları 5 hariç ekrana yazdıralım
# for sayi in range(10):
#     if sayi == 5:
#         continue
#
#     print(sayi)

# 0'dan 10'a kadar olan sayıları ekrana yazdıralım. Ancak 5 gelince durduralım
# for sayi in range(10):
#     if sayi == 5:
#         break
#
#     print(sayi)

# 1'den 100'e kadar olan tek sayıları ekrana yazdıralım
for sayi in range(1, 100):
    if sayi % 2 == 0:
        continue

    print(sayi)

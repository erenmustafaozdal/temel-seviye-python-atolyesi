"""
IF, ELIF VE ELSE BLOKLARI
//////////////////////////////////////////////////////////////////////////////
Python'da bazen birden fazla koşul yazmak isteyebiliriz. Bu koşulları ilk "if"
bloğundan sonra "elif" ifadeleri ile yeni bloklar oluşturarak ekleyebiliriz.
Her bloktan dönen "False" sonucu, alttaki "elif" bloğunu tetikler
"""

# Kullanıcıdan iki sayı alalım.
# Bu sayıların hangisinin büyük veya eşit olduğunu ekrana yazdıralım.
sayi1 = int(input("Sayı yazınız: "))
sayi2 = int(input("Sayı yazınız: "))

if sayi1 > sayi2:
    print(f"1. sayı ({sayi1}), 2. sayıdan ({sayi2}) büyüktür.")
elif sayi2 > sayi1:
    print(f"2. sayı ({sayi2}), 1. sayıdan ({sayi1}) büyüktür.")
else:
    print(f"1. sayı ({sayi1}), 2. sayıya ({sayi2}) eşittir.")

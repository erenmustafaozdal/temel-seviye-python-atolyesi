"""
IF VE ELSE BLOKLARI
//////////////////////////////////////////////////////////////////////////////
Python'da koşul ifadelerinden elde ettiğimiz mantıksal sonuçlar ile programın
akışını değiştirebiliriz
"""

# Kullanıcıdan iki sayı alalım.
# Bu sayıların hangisinin büyük olduğunu ekrana yazdıralım.
sayi1 = int(input("Sayı yazınız: "))
sayi2 = int(input("Sayı yazınız: "))

if sayi1 > sayi2:  # 5 - 5
    print(f"1. sayı ({sayi1}), 2. sayıdan ({sayi2}) büyüktür.")
else:
    print(f"2. sayı ({sayi2}), 1. sayıdan ({sayi1}) büyüktür.")

# ❗ if koşulunun sonuna eklediğimiz iki nokta (:) ile if bloğu oluşturmuş oluyoruz.
# Sonraki satır mutlaka içeriden başlaması gerekir.

"""
Python'da kullanabileceğimiz 2 tane döngü tipinden diğeri while'dır.
Belirttiğimiz koşul doğru (True) olduğu sürece devam eden döngü tipidir.
"""

# 0'dan 10'a kadar olan sayıları ekrana yazdıralım
# sayi = 0
# while sayi < 10:
#     print(sayi)
#     sayi += 1

# 1'den 100'e kadar olan sayıları tek ve çift şeklinde ekrana yazdıralım
# ➡ Ör: 1 tek sayıdır
# ➡ Ör: 2 çift sayıdır
# sayi = 1
# while sayi < 100:
#     if sayi % 2 == 0:
#         print(f"{sayi} çift sayıdır")
#     else:
#         print(f"{sayi} tek sayıdır")
#
#     sayi += 1

# Excel dosyasından alınan öğrenci dikte bilgilerinin ortalamalarını
# ekrana yazdıralım

# Harici bir modül olan xlrd Excel dosyalarını okumamızı sağlar. Öncelikle
# bu modülün komut isteminde 'pip install xlrd' komutu ile yüklenmesi gerekir
# Dokümantasyon: https://xlrd.readthedocs.io/en/latest/
# https://www.python-excel.org/

# modülü kod içine aktaralım
import xlrd

# Excel dosyasını (çalışma kitabını) açalım
ck = xlrd.open_workbook_xls("dikte-kontrol.xls")  # çalışma kitabını aldık

# Excel çalışma sayfasını alalım
cs = ck.sheet_by_index(0)  # çalışma sayfasını aldık

# Toplam kullanılan satır ve sütun sayılarını bulalım
satir_sayisi = cs.nrows
sutun_sayisi = cs.ncols

# while ile öğrencilerin olduğu satırlarda döngüye girelim
#   ➡ Öğrenci adını alalım ✅
#   ➡ Diktelerin olduğu sütunlarda döngüye girelim
#       ➡ Kontrol edilen dikte sayısını bulalım
#       ➡ Dikte kontrollerinde başarılı kelime sayısını toplayalım
#       ➡ Dikte ortalamasını hesaplayıp öğrenci adıyla ekrana yazdıralım
satir = 3
while satir < satir_sayisi:
    ad = cs.cell_value(satir, 0)

    # dikteleri dolaşan döngü
    dikte_sayisi = 0
    dikte_toplami = 0
    for sutun in range(1, 6):
        dikte = cs.cell_value(satir, sutun)

        # if dikte:  # boş değer False, tek karakter bile True anlamına gelir
        if dikte != "":
            dikte_sayisi += 1
            dikte_toplami += int(dikte)

    ortalama = round(dikte_toplami / dikte_sayisi, 2)
    print(f"{ad}: {ortalama}")

    satir += 1

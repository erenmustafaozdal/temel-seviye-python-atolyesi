"""
DRY = don't repeat yourself

Yazdığımız yazılım büyüdükçe karmaşıklaşır. Bu sebeple yazılımımızı anlamlı
parçalara (modüllere) ayırmamız gerekir. Her bir modül kendi sorumluluğundaki
işi yapmakla görevli yazılım parçasıdır.

1. Hazır modüller
    1.1. Standart Python modülleri
    1.2. Üçüncü parti modüller
2. Kendi yazdığımız modüller

PYTHON MODÜL HAVUZU
3. parti modüller aşağıdaki havuzdan bulunabilir. 'pip install modul_adi'
şeklinde sistem içine yüklenir.
https://pypi.org
"""

# STANDART PYTHON MODÜLLERİ
# //////////////////////////////////////////////////////////////////////////////

# random hazır modülünü içeri aktaralım
import random

# dir ile içeriğine bakalım
# print(dir(random))

# help ile dokümantasyonuna bakalım
# print(help(random))

# help ile sadece bir metodun dokümantasyonuna bakalım
# print(help(random.randint))

# Rastgele sayılar üretelim
# print(random.randint(1, 100))

# Rastgele elemanlar seçelim
atolye = "Temel Seviye Python Atölyesi"
dersler = ["Türkçe", "Matematik", "Hayat Bilgisi", "Fen Bilimleri", "Müzik"]
# print(random.choice(atolye))
# print(random.choice(dersler))


# 3. PARTİ MODÜL KULLANIMI
# //////////////////////////////////////////////////////////////////////////////

# pip install selenium
# Tarayıcı ile "Temel Seviye Python Atölyesi" katılım durumu "Onaylandı" olan
# öğretmenleri ekrana yazdıralım
chromedriver = "chromedriver.exe"
url = "https://istanbulakademi.meb.gov.tr/akademiler.php?pID=759"
tablo_secici = "//div[@id='FG_1']/table[1]//tr"

# İçeri aktarmaları yapalım
#   selenium içindeki webdriver
#   selenium.webdriver.common.by içindeki By
from selenium import webdriver
from selenium.webdriver.common.by import By

# Tarayıcı oluşturalım. Tam ekran yapalım. Adrese gidelim.
tarayici = webdriver.Chrome(chromedriver)
tarayici.maximize_window()
tarayici.get(url)

# Tablo satılarını alalım
satirlar = tarayici.find_elements(By.XPATH, tablo_secici)
# print(len(satirlar))  # kaç satır alındı

# Tablo satırlarında döngüye girelim
#   ⚪ İlk 3 satır başlık satıları. Es geçelim
#   ⚪ Öğretmen no, ad ve durum bilgilerini alalım
#   ⚪ Durumu "Onaylandı" olan öğretmenleri ekrana yazdıralım
sayi = 0
for i, satir in enumerate(satirlar):
    if i < 3:
        continue

    no = satir.find_element(By.XPATH, "./td[1]").text
    ad = satir.find_element(By.XPATH, "./td[3]").text
    # isimleri boşluklardan ayırdık. soyadı hariç boşluk ile birleştirdik
    ad_islenmis = " ".join(ad.split()[:-1])
    durum = satir.find_element(By.XPATH, "./td[5]").text

    if durum == "Onaylandı":
        sayi += 1
        print(f"{no} - {ad_islenmis}: {durum}")


print("-"*50)
print(f"{sayi} tane öğretmen onaylandı")
# from time import sleep
# sleep(3)

# Tarayıcıyı kapatalım
tarayici.quit()

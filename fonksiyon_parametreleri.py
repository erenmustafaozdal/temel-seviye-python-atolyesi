# no = int(input("Öğrenci no: "))
# ad = input("Öğrenci ad: ")
# notlar = input("Ders notları (virgülle ayırarak yazın): ")

# notlar_liste = [int(x) for x in notlar.split(",")]
# ortalama = sum(notlar_liste) / len(notlar_liste)
#
# print(f"{no} nolu {ad} ortalama: {ortalama}")

# no, ad, notlar parametreleri alıp not ortalamasını ekrana yazdıran
# not_ortalamasi fonksiyonu tanımlayalım
def not_ortalamasi(ogrenci_no, ogrenci_ad, ogrenci_notlar):
    # virgül ile ayırıp liste haline getiriyoruz
    # "70,80" -> [70,80]
    notlar_liste = [int(x) for x in ogrenci_notlar.split(",")]
    # liste içindeki notları topluyoruz (sum())
    # liste içindeki not sayısına bölüyoruz (len())
    ortalama = sum(notlar_liste) / len(notlar_liste)

    print(f"{ogrenci_no} nolu {ogrenci_ad} ortalama: {ortalama}")


# not_ortalamasi(no, ad, notlar)

# notlar parametresi varsayılan değerli olarak değiştirelim
def not_ortalamasi2(ogrenci_no, ogrenci_ad, ogrenci_notlar=""):

    ortalama = "sınav yok"
    if ogrenci_notlar != "":
        notlar_liste = [int(x) for x in ogrenci_notlar.split(",")]
        ortalama = sum(notlar_liste) / len(notlar_liste)

    print(f"{ogrenci_no} nolu {ogrenci_ad} ortalama: {ortalama}")


# not_ortalamasi2(75, "Eren")
# not_ortalamasi2(75, "Eren", "90,100")

# notlar parametresini değişken sayıda olacak şekilde değiştirelim
def not_ortalamasi3(no, ad, *notlar):  # tuple olarak alınır
    ortalama = sum(notlar) / len(notlar)
    print(f"{no} nolu {ad} ortalama: {ortalama}")


# not_ortalamasi3(99, "Eren", 90, 100, 75, 65)

# //////////////////////////////////////////////////////////////////////////////

# Değişken öğrenci parametrelerine sahip ogrenci_bilgileri fonksiyonu
# tanımlayalım. Bu fonksiyon ile öğrenci bilgilerini anahtar-değer ikilisi
# olarak parametre ile gönderelim
def ogrenci_bilgileri(**bilgiler):
    print(bilgiler)
    print(type(bilgiler))


ogrenci_bilgileri(ad="Eren", no=66, dogum_yili=2014, notlar=[55,66,74])

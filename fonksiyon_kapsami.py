# global scope
x = 0


def fonk():
    # local scope
    x = 1
    return x


# Fonksiyon dışındaki x değerini ve "fonk" fonksiyonundan dönen x değerini
# ekrana yazdıralım
# a = fonk()
# print(a)
# print(x)


a = []
print('a\'nın ilk hali:', a)


def degistir():
    print('a\'i değiştiriyoruz...')

    def degistir2():
        a.append(1)

    degistir2()
    return a


degistir()
print('a\'in son hali: ', a)

# BURADA A LİSTESİ FONKSİYON İÇİNDE NASIL DEĞİŞTİ?
# //////////////////////////////////////////////////////////////////////////////
# Python önce istenen değişkeni ilk önce mevcut isim alanı içinde arar.
# Eğer aranan değişkeni mevcut isim alanı içinde bulamazsa yukarıya doğru
# bütün isim alanlarını tek tek kontrol eder.

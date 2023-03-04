ogrenciler = {
    '120': {
    'ad': 'Ali',
    'soyad': 'Yilmaz',
    'telefon': '532 000 00 01'
    },
    '125': {
    'ad': 'Can',
    'soyad': 'Korkmaz',
    'telefon': '532 000 00 02'
    },
    '128': {
    'ad': 'Volkan',
    'soyad': 'Yukselen',
    'telefon': '532 000 00 03'
    },
}

#1-Bilgileri verilen ogrencileri kullanicidan aldiginiz bilgilerle dictionary icinde saklayiniz.
while True:
    no = input("ogrenci numaranizi giriniz: ")
    ad = input("adinizi giriniz: ")
    soyad = input("soyadinizi griniz: ")
    telefon = input("telefon numaranizi giriniz: ")

    ogrenciler.update({
        no: {
            'ad': ad,
            'soyad': soyad,
            'telefon': telefon
        }
    })

print(ogrenciler)

#2-Ogrenci numarasini kullanicidan alip ilgili ogrenci bilgisini gosterin.
bilgi = input("ogrenci numaranizi giriniz: ")
if bilgi in ogrenciler:
    print(ogrenciler[bilgi])
else:
    print(bilgi, "numarali ogrenci bulunmamaktadir.")
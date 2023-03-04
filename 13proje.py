'''
Kisinin ad, kilo ve boy bilgilerini alip indekslerini hesaplayiniz.
Formul: (Kilo / boy uzunlugunun karesi)
Asagidaki tabloya gore kisi hangi gruba girmektedir.
0 - 18.4    => Zayif
18.5 - 24.9 => Normal
25.0 - 29.9 => Fazla kilolu
30.0 - 34.9 => Sisman(Obez)
'''

ad = input("adinizi giriniz: ")
kilo = float(input("kilonuzu giriniz(kg): "))
boy = float(input("boyunuzu giriniz(m): "))

index = kilo / (boy * boy)

if index < 18.4:
    durum = "Zayif"
elif 18.5 < index < 24.9:
    durum = "Normal"
elif 25.0 < index < 29.9:
    durum = "Fazla kilolu"
else:
    durum = "Sisman(Obez)"

print(ad, ":", durum)
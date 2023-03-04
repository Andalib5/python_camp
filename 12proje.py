''' 
Daire alani : πr²
Daire cevresi : 2πr
?Yaricapi verilen bir dairenin alan ve cevresini hesaplayiniz(π : 3.14)
?Girilen sayinin tek mi cift mi oldugunu yazdirin
'''

r = int(input("dairenin yaricapini giriniz: "))
π = 3.14
alan = r * r * π
cevre = 2 * π * r
print("dairenin alani: " + str(alan) + '\n' + "dairenin cevresi: " + str(cevre))
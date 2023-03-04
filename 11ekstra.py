#Kullanicidan 2 vize (%60) ve final(%40) notunu alip ortalama hesaplayiniz.
#Eger ortalama 50 ve ustundeyse gecti degilse kaldi yazdirin.

vize1 = int(input("1. vizenin notunu giriniz: "))
vize2 = int(input("2. vizenin notunu giriniz: "))
final = int(input("finalin notunu giriniz: "))

ort = (vize1 + vize2) * 0.3 + final * 0.4

print(ort)

if ort >= 50:
    print("Gectiniz.")
else:
    print("Kaldiniz.")
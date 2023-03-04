#parola ve email bilgisini isteyip dogrulugunu kontrol ediniz.
email = "email@ytubmk.com"
parola = "abc123"

email1 = input("emailiniz giriniz: ")
parola1 = input("parolanizi giriniz: ")

if email1 == email:
    print("email dogru")
else:
    print("email yanlis")

if parola1 == parola:
    print("parola dogru")
else:
    print("parola yanlis")
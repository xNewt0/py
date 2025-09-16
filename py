import requests

soru = input("Soru: ")
yanit = requests.get("https://suqul3162.vercel.app/api/gpt4", params={"promt": soru})
print(yanit.text)


sayi1 = int(input("1. sayıyı girin: "))
islem = input("İşlem seç (+, -, *, /): ")
sayi2 = int(input("2. sayıyı girin: "))

if islem == "+":
    print("Sonuç:", sayi1 + sayi2)
elif islem == "-":
    print("Sonuç:", sayi1 - sayi2)
elif islem == "*":
    print("Sonuç:", sayi1 * sayi2)
elif islem == "/":
    if sayi2 != 0:
        print("Sonuç:", sayi1 / sayi2)
    else:
        print("Sıfıra bölme hatası!")
else:
    print("Geçersiz işlem.")

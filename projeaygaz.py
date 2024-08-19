import random

print("Merhaba, Taş, Kağıt, Makas oyununa hoş geldin.\nSizden Taş, Kağıt, Makas seçeneklerinden birisini seçmenizi isteyeceğiz.")
print("Sizin seçtiğiniz seçeneğe karşılık bilgisayar da size karşılık verecek.")
print("Oyun kuralları:\n1-Taş, Makası yener.\n2-Makas, Kağıdı yener.\n3-Kağıt, Taşı yener\nOyundan çıkmak için `exit` yazmanız yeterlidir.")

secenekler = ["Taş", "Kağıt", "Makas", "exit"]

while True:
    oyunSayisi = 0
    oyuncuGalibiyet = 0
    bilgisayarGalibiyet = 0

    while True:
        oyuncuSecenek = input("Lütfen Taş, Kağıt, Makas seçeneklerinden birini giriniz.\n")
        bilgisayarSecenek = random.choice(secenekler[0:3])

        if oyuncuSecenek == "exit":
            break
        if oyuncuSecenek not in secenekler:
            print("Geçersiz seçenek.")
            continue

        print(f"Bilgisayarın Seçimi: {bilgisayarSecenek}")

        if oyuncuSecenek == bilgisayarSecenek:
            print("Berabere!")
        elif (oyuncuSecenek == "Taş" and bilgisayarSecenek == "Makas" or 
              oyuncuSecenek == "Kağıt" and bilgisayarSecenek == "Taş" or
              oyuncuSecenek == "Makas" and bilgisayarSecenek == "Kağıt"):
            oyuncuGalibiyet += 1
            print(f"Tebrikler, kazandınız! Oyuncu: {oyuncuGalibiyet} - {bilgisayarGalibiyet} Bilgisayar")
        else:
            bilgisayarGalibiyet += 1
            print(f"Kaybettiniz! Oyuncu: {oyuncuGalibiyet} - {bilgisayarGalibiyet} Bilgisayar")

        if oyuncuGalibiyet == 2:
            print(f"Tebrikler, turu kazandınız. Oyuncu: {oyuncuGalibiyet} - {bilgisayarGalibiyet} Bilgisayar")
            break
        elif bilgisayarGalibiyet == 2:
            print(f"Turu kaybettiniz. Oyuncu: {oyuncuGalibiyet} - {bilgisayarGalibiyet} Bilgisayar")
            break

    if oyuncuSecenek == "exit":
        break

    bilgisayarDevam = random.choice(["evet", "hayır"])
    

    tekrarSecim = input("Tekrar oynamak istiyor musun? (Evet/Hayır)").lower()
    
    if tekrarSecim == "hayır":
        break
    elif bilgisayarDevam == "hayır":
        print("Bilgisayar devam etmek istemiyor.")
        break
    else :
        continue
    

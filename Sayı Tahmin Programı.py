from random import uniform

sayi = int(uniform(1,101))
deneme = 0
print("Tahmin programına hoşgeldiniz.\nSistem sizin için bir sayi belirledi.\nDoğru sayıyı kaç denemede bulabilirsin?")
while True:
    tahmin = int(input("Tahmininiz:"))

    if tahmin > sayi:
        print("Daha küçük bir sayi giriniz:")
        deneme += 1
    elif tahmin < sayi:
        print("Daha büyük bir sayi giriniz:")
        deneme += 1
    else:
        deneme += 1
        print(f"{deneme} denemede doğru bildiniz.")
        break


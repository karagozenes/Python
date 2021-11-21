from math import sqrt
sayi = 1
toplam = 1
while True:
    bolen_sayisi = 1
    for i in range(2,int(sqrt(toplam))+1):
        if toplam % i == 0:
            bolen_sayisi += 1
        else:
            continue
    if bolen_sayisi < 250:
        sayi += 1
        toplam += sayi
    else:
        print(toplam)
        break

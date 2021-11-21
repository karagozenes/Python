def hesapla(sayi):
    liste = [2]
    toplam = 2
    for bolunen in range(3,sayi+1):
        for bolen in range(2,int(bolunen**0.5)+1):
            if bolunen % bolen == 0:
                break
        else:
            toplam += bolunen
    print(toplam)

hesapla(2000000)
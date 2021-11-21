max_devir = 0
max_sayi = 0

for i in range(2,1001):
	kalan_listesi = []
	bolunen = 1

	while True:
		kalan = bolunen % i
		if kalan in kalan_listesi:
			ilk_index =	kalan_listesi.index(kalan)
			son_index = len(kalan_listesi)
			if son_index - ilk_index > max_devir:
				max_devir = son_index - ilk_index
				max_sayi = i
			break
		else:
			bolunen = 10 * kalan
			kalan_listesi.append(kalan)

print(max_devir)
print(max_sayi)
uptonine = "onetwothreefourfivesixseveneightnine"     # 8*uptoten = 20'ler,30'lar ... ve 90'lar için
tentotwenty = "teneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen"
ty_hundred = "twentythirtyfortyfiftysixtyseventyeightyninety"   # twenty*10 + thirty*10 +......+ ninety*10 = ty_hundred*10
first = 0   # 1-9
second = 0  # 10-19
third = 0   #10,20,30, ... ,90
fourth = 0  #100ve..,200ve..,300ve.., .... ,900ve..
fifth = 0   #100,200,300, .... ,1000

for i in uptonine:
    first += 1
for i in tentotwenty:
    second += 1
for i in ty_hundred:
    third += 1

upto_100 = 9*first + second + 10*third    #100'e kadar olan sayıların toplamı

hundreds= "onehundredandtwohundredandthreehundredandfourhundredandfivehundredandsixhundredandsevenhundredandeighthundredandninehundredand"     #100lü sayılar için.
dzero = "onehundredtwohundredthreehundredfourhundredfivehundredsixhundredsevenhundredeighthundredninehundredonethousand"

# hundreds*99 + upto_100*10 kere tane harf kullanılıyor.
for i in hundreds:
    fourth += 1
for i in dzero:
    fifth += 1

upto_1000 = fourth*99 + upto_100*10 + fifth
print(upto_1000)

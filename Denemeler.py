#!/usr/bin/env python
# coding: utf-8

# In[1]:


def yazma(metin):
    for i in range(10):
        print(metin)
deneme = input("Bir metin giriniz:")
yazma(deneme)


# In[2]:


def fonk(*args):
    print(args)
fonk(10,20,30,40,50,60,70,80)


# In[19]:


yil = 1942
yuzyil = int(yil/100)

if yuzyil+1 != 21:
    print("{}. yüzyıl" .format(yuzyil+1))
else:
    print("20. yüzyıl")


# In[3]:


def asal(a,b):
    liste = []
    for i in range(a,b+1):
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            liste.append(i)
    if 1 in liste:
        liste.remove(1)
    if 0 in liste:
        liste.remove(0)
    print(liste)
asal(254,5763)


# In[4]:


def tambolen(sayi):
    tambolenliste = [bolen for bolen in range(2,sayi+1) if sayi%bolen==0]
    print(tambolenliste)
tambolen(54)


# In[5]:


liste = ["1","2","5a","10b","abc","10","50"]
sayisal_degerler = []
for i in liste:
    try:
        sayisal_degerler.append(int(i))
    except ValueError:
        continue
print(sayisal_degerler)


# In[6]:


while True:
    sayi = input('Çıkmak için "q" ya basınız veya bir sayi giriniz:')
    if sayi == "q":
        break
    try:
        int(sayi)
    except ValueError:
        print(f'{sayi} bir sayi değil.')
        continue


# In[8]:


turkce_karakterler = "şçğüöı"
parola = input("Parolanız:")

for harf in parola:
    if harf in turkce_karakterler:
        raise TypeError("Parolanızda türkçe karakter olamaz.")
else:
    print(f"şifreniz {parola} olarak oluşturuldu.")


# In[9]:


def ort_hesapla(vize,final):
    ortalama = (vize+final)/2
    if 85 <= ortalama <= 100:
        print("Harf notunuz: AA")
    elif 70 <= ortalama <85 and final >= 50:
        print("Harf notunuz: BB")
    elif 60 <= ortalama < 70 and final >= 50:
        print("Harf notunuz: CC")
    elif 45 <= ortalama < 60 and final >= 50:
        print("Harf notunuz: DD")
    elif ortalama < 45:
        print("Kaldınız.")
    else:
        print("Hatalı not girdiniz.")
    return ortalama

ort_hesapla(62,89)


# In[11]:


ad = input("Adınız:") ; soyad  = input("Soyadınız:") ; vize = int(input("Vize Notunuz:")) ; final = int(input("Final Notunuz:"))
ortalama = ort_hesapla(vize,final)
if vize and final <=100 and 0 < ortalama < 100:
    with open("Öğrenci Kayıt Dosyası.txt", "a", encoding="utf-8") as file:
        file.write(f"Adı: {ad}\nSoyadı: {soyad}\nNotlar:{vize},{final}\nOrtalama: {ortalama}\n\n")
else:
    raise Exception("Notunuz yanlış girdiniz. Lütfen tekrar deneyiniz.")


# In[13]:


### DECORATORS
import time
def zaman_hesapla(fonk):
    def wrapper(*args,**kwargs):
        baslangıc = time.time()
        sonuc = fonk(*args,**kwargs)
        bitis = time.time()
        print(f"islem {bitis-baslangıc} kadar sürdü.")
        return sonuc
    return wrapper
@zaman_hesapla
def kareleri_al(liste):
    sonuc = []
    for i in liste:
        sonuc.append(i*i)
    return sonuc
@zaman_hesapla
def kupleri_al(liste):
    sonuc = []
    for i in liste:
        sonuc.append(i*i*i)
    return sonuc
@zaman_hesapla
def topla(*args):
    return sum(args)

print(kareleri_al(range(10000)))


# In[14]:


def decorator(func):
    def wrapper():
        mukemmel_list = []
        for i in range(1001):
            bolen_list = []
            for j in range(1,i):
                if i % j == 0:
                    bolen_list.append(j)
            if sum(bolen_list) == i:
                mukemmel_list.append(i)
        func()
        print(mukemmel_list)
    return wrapper

@decorator
def prime():
    prime_list = []
    for i in range(1001):
        prime = True
        for j in range(2,i):
            if i%j == 0:
                prime = False
                break
        else:
            prime_list.append(i)
    prime_list.remove(0)
    prime_list.remove(1)
    print(prime_list)

prime()


# In[15]:


text = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"

letter_dict = {}

for i in text:
    if i in letter_dict:
        letter_dict[i] += 1
    else:
        letter_dict[i] = 1

for k,v in (enumerate(letter_dict.items())):
    print(k,v)


# In[16]:


with open("şiir.txt","r",encoding= "UTF-8") as file:
    for satir in file:
        list += satir[0]
print(bas_harfler)
mailler = []
content = ""
with open("mailler2.txt","r",encoding="utf-8") as file:
    for satir in file:
        if satir.endswith(".com\n") and satir.rfind("@") != -1:
            print(satir)


# In[17]:


isim = ["Kerim", "Tarık", "Ezgi", "Kemal", "İlkay", "Şükran", "Merve"]

soyisim = ["Yılmaz", "Öztürk", "Dağdeviren", "Atatürk", "Dikmen", "Kaya", "Polat"]

adsoyad = list(zip(isim,soyisim))
adsoyad.sort()

for i,j in adsoyad:
    print(i,j)


# In[18]:


def carpim_tablosu():
    for i in range(1,11):
        print("\n")
        for j in range(1,11):
            yield(f"{i}x{j} = {i*j}")

for i in carpim_tablosu():
    print(i)


# In[ ]:





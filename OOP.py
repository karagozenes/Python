"""
class calisan:
    personelsayisi = 0
    def __init__(self,name,surname,age):
        # print("init calisiyor")
        # sleep(5)
        # print("5 sn sonra")
        self.name = name
        self.surname = surname
        self.age = age
        calisan.personelsayisi += 1
    def show_info(self):
        print(f"ad: {self.name}\nsoyad: {self.surname}")
calisan1 = calisan("ali","yılmaz",42)
calisan2 = calisan("ayşe","turan",23)
calisan3 = calisan("hasan","tokmak",24)
calisan4 = calisan("mehmet","uslu",32)
print(calisan.personelsayisi)

class calisan:
    def __init__(self,isim,soyisim,maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim + soyisim + "@sirket.com"

calisan1 = calisan("Ali","caliskan",5000)
calisan2 = calisan("Veli", "Uzun", 6000)

class yazilimci(calisan):
    pass

yazilimci1 = yazilimci("Ayşe","Yıldız",2000)
yazilimci2 = yazilimci("Fatma", "Ay", 4000)

print(yazilimci1.email)
""""

            # @property , @setter , @deleter

class kisi:
    def __init__(self,ad,soyad):
        self.ad = ad
        self.soyad = soyad
        self.adsoyad = ad + " " + soyad
    @property
    def email(self):
        return f"{self.ad}.{self.soyad}@sirket.com"


kisi1 = kisi("Ali","Uzun")

print(kisi1.ad)
print(kisi1.adsoyad)
print(kisi1.email)              # property olmasa kisi1.email() olarak erişecektik.

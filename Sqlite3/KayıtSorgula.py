import sqlite3

def tumkayıtlar():
    connection = sqlite3.connect("ÖğrenciKayıt.db")
    mycursor = connection.cursor()
    mycursor.execute("select * from students")
    liste = mycursor.fetchall()
    for i in liste:
        print(i)

def isim_soyisim_no():
    connection = sqlite3.connect("ÖğrenciKayıt.db")
    mycursor = connection.cursor()

    mycursor.execute("SELECT number,name,surname FROM students")
    liste = mycursor.fetchall()
    for i in liste:
        print(f"numara: {i[0]}\nisim: {i[1]}\nsoyisim: {i[2]}\n")

def sadece_kızlar():
    connection = sqlite3.connect("ÖğrenciKayıt.db")
    mycursor = connection.cursor()

    mycursor.execute("SELECT name,surname FROM students where gender='Kız'")
    liste = mycursor.fetchall()
    for i in liste:
        print(i)

def an_gecenler():
    connection = sqlite3.connect("ÖğrenciKayıt.db")
    mycursor = connection.cursor()

    mycursor.execute("select * from students where name like '%an%' or surname like '%an%'")
    liste = mycursor.fetchall()
    for i in liste:
        print(i)

def erkek_sayisi():
    connection = sqlite3.connect("ÖğrenciKayıt.db")
    mycursor = connection.cursor()

    mycursor.execute("SELECT COUNT(number) FROM students where gender='Erkek'")
    liste = mycursor.fetchall()
    print(liste)

erkek_sayisi()
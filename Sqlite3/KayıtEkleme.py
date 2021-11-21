import sqlite3
from datetime import datetime
class student():

    connection = sqlite3.connect("ÖğrenciKayıt.db")
    mycursor = connection.cursor()
    mycursor.execute("CREATE TABLE IF NOT EXISTS students(number INT,name TEXT,surname TEXT,birtdate DATETIME,gender TEXT)")

    def __init__(self,number,name,surname,birthdate,gender):
        self.number = number
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

    @staticmethod
    def add_students(student_list):
        query = "INSERT INTO students Values (?,?,?,?,?)"
        student.mycursor.executemany(query,student_list)
        try:
            student.connection.commit()
            print(f"{student.mycursor.rowcount} kadar öğrenci eklendi.")
        except student.connection.Error as err:
            print("hata", err)
        finally:
            student.connection.close()


list_ = [(101,"Ahmet","Yılmaz",datetime(2005,5,17),"Erkek"),
         (102,"Ali","Can",datetime(2005,6,17),"Erkek"),
         (103,"Canan","Tan",datetime(2005,7,17),"Kız"),
         (104,"Ayşe","Taner",datetime(2005,9,23),"Kız"),
         (105,"Bahadır","Toksöz",datetime(2005,7,27),"Erkek"),
         (106,"Ali","Cenk",datetime(2003,8,25),"Erkek"),
         (202,"Ahmet","Yılmaz",datetime(2005,5,17),"Erkek"),
         (301,"Ahmet","Yılmaz",datetime(2005, 5, 17),"Erkek"),
         (302,"Ali","Can",datetime(2005,6,17),"Erkek"),
         (303,"Canan","Tan",datetime(2005,7,17),"Kız"),
         (104,"Ayşe","Taner",datetime(2005,9,23),"Kız"),
         (105,"Bahadır","Toksöz",datetime(2005,7,27),"Erkek"),
         (106,"Ali","Cenk",datetime(2003,8,25),"Erkek")
        ]

student.add_students(list_)
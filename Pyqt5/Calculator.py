
                ###     LAYOUT'SUZ HESAP MAKİNESİ
#
# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import QIcon
#
#
# class calculator(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Calculator")
#         self.icon = QIcon("icon.png")
#         self.setWindowIcon(self.icon)
#         self.setGeometry(600,300,400,300)
#         self.initUI()
#
#     def initUI(self):
#
#         self.lbl_sayi1 = QLabel(self)
#         self.lbl_sayi1.setText("1.SAYI:")
#         self.lbl_sayi1.move(100,33)
#         self.txt_sayi1 = QLineEdit(self)
#         self.txt_sayi1.move(150,30)
#
#         self.lbl_sayi2 = QLabel(self)
#         self.lbl_sayi2.setText("2.SAYI:")
#         self.lbl_sayi2.move(100,63)
#         self.txt_sayi2 = QLineEdit(self)
#         self.txt_sayi2.move(150,60)
#
#         self.toplam = QPushButton(self)
#         self.toplam.setText("Topla")
#         self.toplam.move(50,90)
#         self.toplam.clicked.connect(self.hesaplama)
#
#         self.cikar = QPushButton(self)
#         self.cikar.setText("Çıkar")
#         self.cikar.move(125,90)
#         self.cikar.clicked.connect(self.hesaplama)
#
#         self.carp = QPushButton(self)
#         self.carp.setText("Çarp")
#         self.carp.move(200, 90)
#         self.carp.clicked.connect(self.hesaplama)
#
#         self.bol = QPushButton(self)
#         self.bol.setText("Böl")
#         self.bol.move(275, 90)
#         self.bol.clicked.connect(self.hesaplama)
#
#         self.sonuc = QLabel(self)
#         self.sonuc.setText("SONUÇ:")
#         self.sonuc.move(175,130)
#         self.sonuc.resize(150,20)
#         self.show()
#
#     def hesaplama(self):
#         sender = self.sender()
#         if sender.text() == "Topla":
#             result = int(self.txt_sayi1.text()) + int(self.txt_sayi2.text())
#             self.sonuc.setText("SONUÇ: " + str(result))
#         elif sender.text() == "Çıkar":
#             result = int(self.txt_sayi1.text()) - int(self.txt_sayi2.text())
#             self.sonuc.setText("SONUÇ: " + str(result))
#         elif sender.text() == "Çarp":
#             result = int(self.txt_sayi1.text()) * int(self.txt_sayi2.text())
#             self.sonuc.setText("SONUÇ: " + str(result))
#         elif sender.text() == "Böl":
#             result = float(self.txt_sayi1.text()) / float(self.txt_sayi2.text())
#             self.sonuc.setText("SONUÇ: " + str(result))
#
#
#
#
# app = QApplication(sys.argv)
# makine = calculator()
# sys.exit(app.exec())



                ###     LAYOUT'LU HESAP MAKİNESİ

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QPixmap


class calculator(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.icon = QIcon("icon.png")
        self.setWindowIcon(self.icon)
        self.setGeometry(900,400,250,150)
        self.initUI()


    def initUI(self):
        self.value1 = QLabel("1.SAYI")
        self.value1_text = QLineEdit()
        self.value2 = QLabel("2.SAYI")
        self.value2_text = QLineEdit()
        self.plus = QPushButton("Topla")
        self.minus = QPushButton("Çıkar")
        self.multiply = QPushButton("Çarp")
        self.slash = QPushButton("Böl")
        self.result = QLabel("SONUÇ:")

        v_box = QVBoxLayout()

        h_box1 = QHBoxLayout()
        h_box1.addStretch()
        h_box1.addWidget(self.value1)
        h_box1.addWidget(self.value1_text)
        h_box1.addStretch()
        v_box.addLayout(h_box1)

        h_box2 = QHBoxLayout()
        h_box2.addStretch()
        h_box2.addWidget(self.value2)
        h_box2.addWidget(self.value2_text)
        h_box2.addStretch()
        v_box.addLayout(h_box2)

        h_box3 = QHBoxLayout()
        h_box3.addStretch()
        h_box3.addWidget(self.plus)
        self.plus.clicked.connect(self.hesaplama)
        h_box3.addWidget(self.minus)
        self.minus.clicked.connect(self.hesaplama)
        h_box3.addStretch()
        v_box.addLayout(h_box3)

        h_box4 = QHBoxLayout()
        h_box4.addStretch()
        h_box4.addWidget(self.multiply)
        self.multiply.clicked.connect(self.hesaplama)
        h_box4.addWidget(self.slash)
        self.slash.clicked.connect(self.hesaplama)
        h_box4.addStretch()
        v_box.addLayout(h_box4)

        h_box5 = QHBoxLayout()
        h_box5.addStretch()
        h_box5.addWidget(self.result)
        h_box5.addStretch()
        v_box.addLayout(h_box5)
        v_box.addStretch()

        self.setLayout(v_box)
        self.show()

    def hesaplama(self):
        sender = self.sender()
        if sender.text() == "Topla":
            result = int(self.value1_text.text()) + int(self.value2_text.text())
            self.result.setText("SONUÇ: " + str(result))
        elif sender.text() == "Çıkar":
            result = int(self.value1_text.text()) - int(self.value2_text.text())
            self.result.setText("SONUÇ: " + str(result))
        elif sender.text() == "Çarp":
            result = int(self.value1_text.text()) * int(self.value2_text.text())
            self.result.setText("SONUÇ: " + str(result))
        elif sender.text() == "Böl":
            result = float(self.value1_text.text()) / float(self.value2_text.text())
            self.result.setText("SONUÇ: " + str(result))




app = QApplication(sys.argv)
makine = calculator()
sys.exit(app.exec())






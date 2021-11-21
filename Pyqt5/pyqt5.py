import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
# def pencere():
    # app = QtWidgets.QApplication(sys.argv)          # iskelet başlangıcı
    # pencere = QtWidgets.QWidget()                   # pencere isimli widget nesnesi oluşturmak için
    # pencere.setWindowTitle("İlk Deneme")            # pencerenin başlığını belirlemek için
    # pencere.setGeometry(100,100,500,500)            # pencerenin ekranda  ilk açılacağı konumlar(ilk 2) ve pencerenin açılma büyüklüğü(son 2)
    # etiket1 = QtWidgets.QLabel(pencere)             # etiket1'in pencere üzerinde gözükmesini sağlamak için
    # etiket2 = QtWidgets.QLabel(pencere)
    # buton = QtWidgets.QPushButton(pencere)          # penceye buton eklemek için




    # etiket1.setText("Benim adım Enes")              # etiket1'in yazısı
    # etiket1.move(50,100)                            # etiket1'in pencere üzerindeki konumunu ayarlamak için
    # etiket2.setPixmap(QtGui.QPixmap("deneme.jpg"))  # etiket2 nesnesi ile pencereye bir görsel ekledik
    # buton.setText("Erdem")                          # buton üzerindeki yazı


    # pencere.show()                                  # pencereyi ekranda göstermek için
    # sys.exit(app.exec())                            # pencereyi ekranda açık tutabilmek için(iskelet bitişi)

# pencere()

                    #   BUTONA FONKSİYON EKLEME
#
# class pencere(QtWidgets.QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.init_ui()
#
#     def init_ui(self):
#
#         self.yazı_alanı = QtWidgets.QLabel("Butona hiç tıklanmadı")
#         self.buton = QtWidgets.QPushButton("Tıkla")
#         self.say = 0
#
#         v_box = QtWidgets.QVBoxLayout()         # Vertical Box Layout
#         h_box = QtWidgets.QHBoxLayout()         # Hortizonal Box Layout
#
#         v_box.addWidget(self.buton)             # VBOX'a buton atama
#         v_box.addWidget(self.yazı_alanı)
#         v_box.addStretch()                      # Widgetleri sağa veya sola dayama (v_box üstüne yazarsak sola, altına yazarsak sağa dayar)
#
#         h_box.addStretch()
#         h_box.addLayout(v_box)
#         h_box.addStretch()
#
#         self.setLayout(h_box)                   # Layoutu aktif etmek için kullanılır
#
#         self.buton.clicked.connect(self.click)  # butona fonksiyon atamak için kullanılan komut
#         self.show()
#
#     def click(self):                            # butona tıklanınca çalışacak fonksiyonun kendisi
#         self.say += 1
#         self.yazı_alanı.setText(f"Butona {self.say} kere tıklandı")
#
#
# app = QtWidgets.QApplication(sys.argv)
# pencere = pencere()
# sys.exit(app.exec())


                    # QLineEdit ve INPUT ALANLARI

# class pencere(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#         self.init_ui()
#
#     def init_ui(self):

                ### RENK EKLEME ve LAYOUT

# import sys
# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
# from PyQt5.QtGui import QPalette,QColor
#
# class Color(QWidget):
#     def __init__(self,color):
#         super(Color,self).__init__()
#         self.setAutoFillBackground(True)
#         palette = self.palette()
#         palette.setColor(QPalette.Window, QColor(color))
#         self.setPalette(palette)
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow,self).__init__()
#         self.setGeometry(300,300,500,500)
#
#         hlayout1 = QtWidgets.QHBoxLayout()
#
#         hlayout1.addWidget(Color("red"))
#         hlayout1.addWidget(Color("green"))
#         hlayout1.addWidget(Color("yellow"))
#         # hlayout1.setContentsMargins(50,0,0,0)               # soldan 50 piksel boşluk bırakır
#         # hlayout1.setSpacing(50)                               # üstteki her layout'un arasına 50 piksel boşluk bırakır
#
#         hlayout2 = QtWidgets.QHBoxLayout()
#
#         hlayout2.addWidget(Color("blue"))
#         hlayout2.addWidget(Color("purple"))
#
#         vlayout = QtWidgets.QVBoxLayout()
#         vlayout.addLayout(hlayout1)
#         vlayout.addLayout(hlayout2)
#
#         widget = QWidget()
#         widget.setLayout(vlayout)
#
#
#         self.setCentralWidget(widget)
#
# app = QApplication(sys.argv)
# win = MainWindow()
# win.show()
# sys.exit(app.exec())

        ###  FORM LAYOUT

# def window():
#     app = QApplication(sys.argv)
#     win = QWidget()
#     win.setWindowTitle("Form Layout")
#
#     nm_lbl = QLabel("Name")
#     nm_txt = QLineEdit()
#
#     adr_lbl = QLabel("Address")
#     adr_txt1 = QLineEdit()
#     adr_txt2 = QLineEdit()
#
#     f_layout = QFormLayout()
#     f_layout.addRow(nm_lbl,nm_txt)
#
#     v_box = QVBoxLayout()
#     v_box.addWidget(adr_txt1)
#     v_box.addWidget(adr_txt2)
#
#     f_layout.addRow(adr_lbl,v_box)
#
#     rbtn1 = QRadioButton("Male")
#     rbtn2 = QRadioButton("Female")
#
#     h_box = QHBoxLayout()
#     h_box.addWidget(rbtn1)
#     h_box.addWidget(rbtn2)
#
#     f_layout.addRow(QLabel("Sex"),h_box)
#     f_layout.addRow(QPushButton("Submit"),QPushButton("Cancel"))
#
#
#     win.setLayout(f_layout)
#     win.show()
#     sys.exit(app.exec())
#
# window()

                    ### LABELLAR
#
# def window():
#     app = QApplication(sys.argv)
#     win = QWidget()
#
#     l1 = QLabel()
#     l2 = QLabel()
#     l3 = QLabel()
#
#     l1.setText("Hello World!")
#     l2.setText("<A href = '#' >PyQt Dersleri Labellar< /a>")
#     l3.setText("<A href = 'www.google.com' >GOOGLE< /a>")
#
#     l1.setAlignment(Qt.AlignCenter)             # Alignmet hizalama yapmak için kullanılır. QtCore gereklidir.
#     l2.setAlignment(Qt.AlignRight)
#     l3.setAlignment(Qt.AlignLeft)
#
#     l2.linkHovered.connect(hovered)             # l2 üzerine gidildiğinde hovered fonksiyonu çalışır.
#     l3.linkActivated.connect(click)             # l3 üzerine tıklandığında click fonksiyonu çalışır.
#
#     l1.setTextInteractionFlags(Qt.TextSelectableByMouse)        # Mouse ile metin üzerinden seçme yapılabilir.
#
#     vbox = QVBoxLayout()
#     vbox.addWidget(l1)
#     vbox.addStretch()
#     vbox.addWidget(l2)
#     vbox.addStretch()
#     vbox.addWidget(l3)
#     vbox.addStretch()
#
#     win.setLayout(vbox)
#     win.show()
#     sys.exit(app.exec())
#
# def hovered():
#     print("hovering")
# def click():
#     print("Clicked")
#
# window()

                ### QLINEEDIT
#
# def window():
#     app  = QApplication(sys.argv)
#     win = QWidget()
#     win.setWindowTitle("QLineEdit")
#     win.setFont(QFont("Times New Roman",10))
#
#
#     e1 = QLineEdit()
#     e1.setValidator(QIntValidator())
#     e1.setMaxLength(4)
#     e1.setAlignment(Qt.AlignRight)
#     e1.setFont(QFont("Arial",20))
#
#     e2 = QLineEdit()
#     e2.setValidator(QDoubleValidator(0.99,99.99,2))
#
#     e3 =QLineEdit()
#     e3.setInputMask("(555) (000   00   00)")                # 0'lar kullanıcının değer girmesini sağlar. 0 dışında yazılanlar değiştirilemez.
#
#     e4 = QLineEdit()
#     e4.textChanged.connect(fonk1)
#
#     e5 = QLineEdit()
#     e5.setEchoMode(QLineEdit.Password)                      # Parola görünümü kazandırma
#     e5.editingFinished.connect(fonk2)
#
#     e6 = QLineEdit("Enes Karagöz")
#     e6.setReadOnly(True)
#
#     flo = QFormLayout()
#     flo.addRow("Integer Validator:", e1)
#     flo.addRow("Double Validator:", e2)
#     flo.addRow("Input Mask:", e3)
#     flo.addRow("Text Changed:", e4)
#     flo.addRow("Password", e5)
#     flo.addRow("Read Only", e6)
#
#     win.setLayout(flo)
#     win.show()
#     sys.exit(app.exec())
#
#
# def fonk1(text):
#     print("harf :" + text)
# def fonk2():
#     print("Enter Press")
#
# window()

            ### PUSHBUTTON

# class MainWin(QWidget):
#     def __init__(self):
#         super(MainWin,self).__init__()
#
#         self.b1 = QPushButton("Button1")
#         self.b1.setCheckable(True)
#         self.b1.toggle()
#         self.b1.clicked.connect(self.btnstate)
#         self.b1.clicked.connect(lambda:self.whichbtn(self.b1))
#
#         self.b2 = QPushButton("Button2")
#         self.b2.setEnabled(False)
#
#         self.b3 = QPushButton("&Default")                            # &Default yazınca alt+D kısayoluyla butona tıklanmış olur.
#         self.b3.setDefault(True)
#         self.b3.clicked.connect(lambda:self.whichbtn(self.b3))
#
#         vbox = QVBoxLayout()
#         vbox.addWidget(self.b1)
#         vbox.addWidget(self.b2)
#         vbox.addWidget(self.b3)
#
#         self.setLayout(vbox)
#
#     def btnstate(self):
#         if self.b1.isChecked():
#             print("button Pressed")
#         else:
#             print("button released")
#
#     def whichbtn(self,btn):
#         print("Clicked button is " + btn.text())
#
#
# def main():
#     app = QApplication(sys.argv)
#     win = MainWin()
#     win.show()
#     sys.exit(app.exec())
# main()

            ### RADIO BUTTON
#
# class MainWin(QWidget):
#     def __init__(self):
#         super(MainWin,self).__init__()
#         self.rb1 = QRadioButton("Radio1")
#         self.rb2 = QRadioButton("Radio2")
#
#         self.rb1.setChecked(False)
#         self.rb1.toggled.connect(lambda:self.fonk1(self.rb1))           # toggled'ı clicked'dan ayıran açma-kapama durumudur. clicked sadece tıklayınca çalışır.
#
#
#         hbox = QHBoxLayout()
#         hbox.addWidget(self.rb1)
#         hbox.addWidget(self.rb2)
#
#         self.setLayout(hbox)
#
#     def fonk1(self,rb):
#         if rb.text() == "Radio1":
#             if rb.isChecked() == True:
#                 print(rb.text() + " is selected")
#             else:
#                 print(rb.text() + " is deselected")
# def main():
#     app = QApplication(sys.argv)
#     win = MainWin()
#     win.show()
#     sys.exit(app.exec())
# main()

                ### QSLINDER

class MainWin(QWidget):
    def __init__(self):
        super(MainWin,self).__init__()
        self.lbl = QLabel("Hello!")
        self.setFont(QFont("Times New Roman",55))
        self.setWindowTitle("Font Büyüklüğü")
        self.qs = QSlider(Qt.Horizontal)
        self.qs.setMinimum(10)
        self.qs.setMaximum(100)
        self.qs.setSingleStep(1)
        self.qs.setTickPosition(QSlider.TicksBelow)
        self.qs.setTickInterval(10)
        self.qs.setValue(55)

        self.qs.valueChanged.connect(self.font_size)

        self.lbl.setAlignment(Qt.AlignCenter)


        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.lbl)
        self.vbox.addWidget(self.qs)


        self.setLayout(self.vbox)

    def font_size(self):
        value = self.qs.value()
        self.setFont(QFont("Times New Roman",value))

def main():
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec())
main()


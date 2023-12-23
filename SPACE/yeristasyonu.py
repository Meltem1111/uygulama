import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget,QMainWindow,QTableWidgetItem,QTableWidget,QHeaderView,QMessageBox,QPushButton,QLineEdit,QVBoxLayout,QLineEdit
from PyQt5.QtGui import QPixmap,QIcon
from istasyonui import Ui_MainWindow
import sys
import sqlite3
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvas
import folium


conn= sqlite3.connect("yeristasyonu.db")
cursor = conn.cursor()
conn.commit()



cursor.execute("""CREATE TABLE IF NOT EXISTS yeristasyonu  (

PAKET_NUMARASI PRIMARY KEY,
UYDU_STATUSU TEXT NOT NULL,
HATA_KODU TEXT NOT NULL,
GONDERME_SAATİ TEXT NOT NULL,
BASINC1 INTEGER NOT NULL,
BASINC2 INTEGER NOT NULL ,
YUKSEKLIK1 INTEGER NOT NULL,
YUKSEKLIK2 INTEGER NOT NULL,
IRTIFA_FARKI TEXT NOT NULL,
INIS_HIZI TEXT NOT NULL,
SICAKLIK TEXTNOT NULL,
PIL_GERILIMI TEXT NOT NULL,
GPS1_LATIDAUDE TEXT NOT NULL,
GPS1_LONGITUDE NOT NULL,
PITCH TEXT 
)""");


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.label.setPixmap(QPixmap("ustlogo.png"))
        self.setWindowIcon(QIcon("logo.png"))
        self.setWindowTitle("SPACE")
        self.label.setScaledContents(True)
        self.pushButton.clicked.connect(self.ekle)

        # self.listele()



        
        # self.figure=plt.figure()
        # self.ax=plt.axes
        
        # self.canvas=FigureCanvas(self.figure)
        # layout= QVBoxLayout(self.basinc1)
        # layout= QVBoxLayout(self.basinc2)

        # layout.setContentsMargins(0,0,0,0)
        # layout.addWidget(self.canvas)
        # self.setLayout(layout)


    # def listele(self):
    #     # kayitSayisi = 0
    #     cursor.execute("SELECT * FROM yeristasyonu")
    #     kayitlar = cursor.fetchall()
    #     # for indexsatir,indexsutun

    #     # for i in kayitlar:
    #     #     kayitSayisi += 1
    #     #     print(i)
        
    #     # if kayitSayisi == 0:
    #     #     print("Listede herhangi bir kayıt bulunmamaktadır.") 
    def listele(self):
        cursor.execute("SELECT * FROM yeristasyonu")
        for indexSatir,kayitNumarasi in enumerate(cursor):
            for indexSutun , kayitSutun in enumerate(kayitNumarasi):
                self.tableWidget.setItem(indexSatir,indexSutun,QTableWidgetItem(str(kayitSutun)))

        conn.commit()
        conn.close()
            
    def harita_cız(self):
        latitude = 41.0082
        longitude = 28.9784


        harita = folium.Map(location=[latitude, longitude], zoom_start=10)


        folium.Marker([latitude, longitude], popup='Merhaba, buradayım!').add_to(harita)

        harita.save('harita.html')  
        harita.show()


      
    def basinc_grafik_ciz(self):
        veri_sayisi = int(input("Kaç veri olacak "))

        basinc_degerleri = []
        for i in range(veri_sayisi):
            basinc = float(input(f"{i+1}. basınç değerini girin= "))
            basinc_degerleri.append(basinc)
        plt.plot(basinc_degerleri, marker='o', linestyle='-', color='b')
        plt.title('Basınç Grafiği')
        plt.xlabel('Veri Sırası')
        plt.ylabel('Basınç Değeri')
        plt.grid(True)
        plt.show()

       

    def ekle(self):
        uydu_statusu=self.lineEdit.text()
        hata_kodu=self.lineEdit_2.text()
        gönderme_saat=self.timeEdit.text()
        basinc1=self.lineEdit_3.text()
        basinc2=self.lineEdit_4.text()
        yukseklik1=self.lineEdit_5.text()

        cursor.execute("""INSERT INTO yeristasyonu  (UYDU_STATUSU, HATA_KODU, GONDERME_SAATİ ,BASINC1  ,BASINC2  ,YUKSEKLIK1 ) VALUES (?,?,?,?,?,?)""",
                       (uydu_statusu,hata_kodu,gönderme_saat,basinc1,basinc2,yukseklik1))
        # self.listele()

        conn.commit()
        self.listele()




def app():
    app=QtWidgets.QApplication(sys.argv)
    win=Window()
    win.show()
    sys.exit(app.exec_())
app()



# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'konsumen.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(613, 548)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 0, 591, 531))
        self.pushButton_Keluar = QPushButton(self.groupBox)
        self.pushButton_Keluar.setObjectName(u"pushButton_Keluar")
        self.pushButton_Keluar.setGeometry(QRect(380, 280, 80, 24))
        self.pushButton_Hapus = QPushButton(self.groupBox)
        self.pushButton_Hapus.setObjectName(u"pushButton_Hapus")
        self.pushButton_Hapus.setGeometry(QRect(270, 280, 80, 24))
        self.pushButton_Simpan = QPushButton(self.groupBox)
        self.pushButton_Simpan.setObjectName(u"pushButton_Simpan")
        self.pushButton_Simpan.setGeometry(QRect(50, 280, 80, 24))
        self.pushButton_Ubah = QPushButton(self.groupBox)
        self.pushButton_Ubah.setObjectName(u"pushButton_Ubah")
        self.pushButton_Ubah.setGeometry(QRect(160, 280, 80, 24))
        self.label_idPelanggan = QLabel(self.groupBox)
        self.label_idPelanggan.setObjectName(u"label_idPelanggan")
        self.label_idPelanggan.setGeometry(QRect(40, 70, 81, 16))
        self.label_namaPerusahaan = QLabel(self.groupBox)
        self.label_namaPerusahaan.setObjectName(u"label_namaPerusahaan")
        self.label_namaPerusahaan.setGeometry(QRect(40, 100, 111, 16))
        self.label_Alamat = QLabel(self.groupBox)
        self.label_Alamat.setObjectName(u"label_Alamat")
        self.label_Alamat.setGeometry(QRect(40, 130, 111, 16))
        self.label_Telpon = QLabel(self.groupBox)
        self.label_Telpon.setObjectName(u"label_Telpon")
        self.label_Telpon.setGeometry(QRect(40, 220, 111, 16))
        self.lineEdit_IdPelanggan = QLineEdit(self.groupBox)
        self.lineEdit_IdPelanggan.setObjectName(u"lineEdit_IdPelanggan")
        self.lineEdit_IdPelanggan.setGeometry(QRect(220, 70, 191, 24))
        self.lineEdit_Telpon = QLineEdit(self.groupBox)
        self.lineEdit_Telpon.setObjectName(u"lineEdit_Telpon")
        self.lineEdit_Telpon.setGeometry(QRect(220, 170, 191, 24))
        self.lineEdit_NamaPerusahaan = QLineEdit(self.groupBox)
        self.lineEdit_NamaPerusahaan.setObjectName(u"lineEdit_NamaPerusahaan")
        self.lineEdit_NamaPerusahaan.setGeometry(QRect(220, 100, 191, 24))
        self.lineEdit_Alamat = QLineEdit(self.groupBox)
        self.lineEdit_Alamat.setObjectName(u"lineEdit_Alamat")
        self.lineEdit_Alamat.setGeometry(QRect(220, 130, 191, 24))
        self.textEdit = QTextEdit(self.groupBox)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(220, 200, 191, 41))
        self.tableWidget = QTableWidget(self.groupBox)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 340, 571, 131))
        self.lineEdit_NamaPemilik = QLabel(self.groupBox)
        self.lineEdit_NamaPemilik.setObjectName(u"lineEdit_NamaPemilik")
        self.lineEdit_NamaPemilik.setGeometry(QRect(40, 170, 111, 16))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"GroupBox", None))
        self.pushButton_Keluar.setText(QCoreApplication.translate("Form", u"Keluar", None))
        self.pushButton_Hapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
        self.pushButton_Simpan.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.pushButton_Ubah.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.label_idPelanggan.setText(QCoreApplication.translate("Form", u"ID Pelanggan", None))
        self.label_namaPerusahaan.setText(QCoreApplication.translate("Form", u"Nama Perusahaan", None))
        self.label_Alamat.setText(QCoreApplication.translate("Form", u"Alamat", None))
        self.label_Telpon.setText(QCoreApplication.translate("Form", u"Telpon / fax", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"id_pel", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"nm_perusahaan", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"nm_pemilik", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"alamat", None));
        self.lineEdit_NamaPemilik.setText(QCoreApplication.translate("Form", u"Nama Pemilik", None))
    # retranslateUi


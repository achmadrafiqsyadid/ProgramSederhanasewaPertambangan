# File: logika_alat_berat.py
# Berisi semua logika untuk Tampilan Form Alat Berat

import sys
from PySide6.QtWidgets import (
    QWidget, QMessageBox, QTableWidgetItem
)
from PySide6.QtCore import Qt

# Impor UI yang sudah di-compile
try:
    # PASTIKAN nama kelas di ui_alat_berat.py adalah 'Ui_Form'
    from ui_alat_berat import Ui_Form as Ui_AlatBeratForm
except ImportError:
    print("Error: 'ui_alat_berat.py' belum ada.")
    print("Jalankan: pyside6-uic alat_berat.ui -o ui_alat_berat.py")
    sys.exit()

# Impor fungsi koneksi database kita
from database import connect_db

class AlatBeratWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AlatBeratForm()
        self.ui.setupUi(self)

        self.db = None
        self.hubungkan_ke_db()
        self.konfigurasi_tabel()
        self.isi_combobox()
        self.hubungkan_tombol()
        self.load_data()

    def hubungkan_ke_db(self):
        self.db = connect_db()
        if not self.db:
            QMessageBox.critical(self, "Error Database", "Tidak bisa terhubung ke database.")
            self.close()

    def konfigurasi_tabel(self):
        # Sesuaikan jumlah kolom dengan tabel database
        self.ui.tableWidget.setColumnCount(8)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ["Kode Alat", "Nama Alat", "Merk", "Jenis/Tipe",
             "Spesifikasi", "Tahun", "Sewa Harian", "Status"]
        )
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)

    def isi_combobox(self):
        # Isi comboBox Status
        self.ui.comboBox_Status.addItems(['tersedia', 'disewa', 'perbaikan', 'nonaktif'])

        # Isi comboBox Jenis/Tipe (Anda bisa tambahkan lagi)
        self.ui.comboBox_Jenis.addItems(['Dump Truck', 'Tronton', 'Excavator', 'Bulldozer', 'Bak'])

    def hubungkan_tombol(self):
        # Hubungkan tombol ke fungsi (Pastikan objectName sesuai)
        self.ui.pushButton_Baru.clicked.connect(self.bersihkan_form)
        self.ui.pushButton_Simpan.clicked.connect(self.simpan_data)
        self.ui.pushButton_Ubah.clicked.connect(self.simpan_data) # Ubah = Simpan
        self.ui.pushButton_Hapus.clicked.connect(self.hapus_data)
        self.ui.pushButton_Keluar.clicked.connect(self.close)
        self.ui.tableWidget.cellClicked.connect(self.data_tabel_diklik)

    def bersihkan_form(self):
        self.ui.lineEdit_KodeAlat.clear()
        self.ui.lineEdit_NamaAlat.clear()
        self.ui.lineEdit_Merk.clear()
        self.ui.comboBox_Jenis.setCurrentIndex(0)
        self.ui.textEdit_Spesifikasi.clear()
        self.ui.lineEdit_Tahun.clear()
        self.ui.lineEdit_Sewa.clear()
        self.ui.comboBox_Status.setCurrentIndex(0) # Kembali ke 'tersedia'
        self.ui.lineEdit_KodeAlat.setFocus()
        self.ui.lineEdit_KodeAlat.setReadOnly(False) # Pastikan bisa diedit

    def load_data(self):
        if not self.db or not self.db.is_connected():
            return
        try:
            cursor = self.db.cursor()
            # Ambil semua data dari tabel (menggunakan nama tabel 'alat_berat' yang ada di DB Anda)
            cursor.execute("SELECT id_alat, nama_alat, merk, jenis_alat, spesifikasi, tahun_pembuatan, harga_sewa_per_jam, status_alat FROM alat_berat")
            records = cursor.fetchall()

            self.ui.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(records):
                self.ui.tableWidget.insertRow(row_number)
                for col_number, data in enumerate(row_data):
                    self.ui.tableWidget.setItem(row_number, col_number, QTableWidgetItem(str(data)))
            cursor.close()
        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Gagal memuat data: {e}")

    def simpan_data(self):
        if not self.db or not self.db.is_connected():
            return

        # 1. Ambil data dari form
        kode = self.ui.lineEdit_KodeAlat.text()
        nama = self.ui.lineEdit_NamaAlat.text()
        merk = self.ui.lineEdit_Merk.text()
        jenis = self.ui.comboBox_Jenis.currentText() # Ambil teks dari combo box
        spesifikasi = self.ui.textEdit_Spesifikasi.toPlainText()
        status = self.ui.comboBox_Status.currentText()

        # Validasi input angka
        try:
            # Mengizinkan input kosong untuk tahun dan sewa, mengubahnya jadi None
            tahun_text = self.ui.lineEdit_Tahun.text()
            tahun = int(tahun_text) if tahun_text else None

            sewa_text = self.ui.lineEdit_Sewa.text()
            sewa = float(sewa_text) if sewa_text else 0.0

        except ValueError:
            QMessageBox.warning(self, "Input Error", "Tahun Pembuatan dan Sewa Harian harus berupa angka.")
            return

        # 2. Validasi sederhana
        if not kode or not nama:
            QMessageBox.warning(self, "Input Error", "Kode Alat dan Nama Alat wajib diisi.")
            return

        try:
            cursor = self.db.cursor()
            # 3. Query SQL (Gunakan REPLACE INTO untuk Simpan/Ubah)
            sql = """
            REPLACE INTO alat_berat
            (id_alat, nama_alat, merk, jenis_alat, spesifikasi, tahun_pembuatan, harga_sewa_per_jam, status_alat)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            val = (kode, nama, merk, jenis, spesifikasi, tahun, sewa, status)

            cursor.execute(sql, val)
            self.db.commit()
            cursor.close()

            QMessageBox.information(self, "Sukses", "Data alat berat berhasil disimpan.")
            self.load_data()
            self.bersihkan_form()

        except Exception as e:
            self.db.rollback()
            QMessageBox.critical(self, "Database Error", f"Gagal menyimpan data: {e}")

    def data_tabel_diklik(self, row, column):
        # Fungsi ini akan mengisi form saat baris di tabel diklik
        self.ui.lineEdit_KodeAlat.setText(self.ui.tableWidget.item(row, 0).text())
        self.ui.lineEdit_KodeAlat.setReadOnly(True) # Kode Alat tidak boleh diubah (PK)

        self.ui.lineEdit_NamaAlat.setText(self.ui.tableWidget.item(row, 1).text())
        self.ui.lineEdit_Merk.setText(self.ui.tableWidget.item(row, 2).text())
        self.ui.comboBox_Jenis.setCurrentText(self.ui.tableWidget.item(row, 3).text())

        # Menangani nilai 'None' dari database
        spesifikasi_text = self.ui.tableWidget.item(row, 4).text()
        self.ui.textEdit_Spesifikasi.setPlainText("" if spesifikasi_text == "None" else spesifikasi_text)

        tahun_text = self.ui.tableWidget.item(row, 5).text()
        self.ui.lineEdit_Tahun.setText("" if tahun_text == "None" else tahun_text)

        self.ui.lineEdit_Sewa.setText(self.ui.tableWidget.item(row, 6).text())
        self.ui.comboBox_Status.setCurrentText(self.ui.tableWidget.item(row, 7).text())

    def hapus_data(self):
        # Mengambil Kode Alat dari form
        kode = self.ui.lineEdit_KodeAlat.text()
        if not kode:
            QMessageBox.warning(self, "Error", "Pilih data dari tabel yang ingin dihapus.")
            return

        konfirmasi = QMessageBox.question(self, "Hapus Data",
            f"Anda yakin ingin menghapus data dengan Kode Alat: {kode}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if konfirmasi == QMessageBox.StandardButton.Yes:
            try:
                cursor = self.db.cursor()
                sql = "DELETE FROM alat_berat WHERE id_alat = %s" # Menggunakan 'alat_berat'
                val = (kode,)

                cursor.execute(sql, val)
                self.db.commit()
                cursor.close()

                QMessageBox.information(self, "Sukses", "Data berhasil dihapus.")
                self.load_data()
                self.bersihkan_form()

            except Exception as e:
                self.db.rollback()
                # Cek jika error karena foreign key
                if "1451" in str(e):
                    QMessageBox.critical(self, "Database Error",
                        "Gagal menghapus: Alat ini sedang dipakai di tabel Penyewaan.")
                else:
                    QMessageBox.critical(self, "Database Error", f"Gagal menghapus data: {e}")

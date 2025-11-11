# File: logika_konsumen.py
# File ini berisi SEMUA logika khusus untuk jendela konsumen.

import sys
from PySide6.QtWidgets import (
    QWidget, QMessageBox, QTableWidgetItem
)
from PySide6.QtCore import Qt

# Impor UI yang sudah di-compile (dari ui_konsumen.py)
try:
    from ui_konsumen import Ui_Form as Ui_KonsumenForm
except ImportError:
    print("Error: 'ui_konsumen.py' belum ada. Jalankan: pyside6-uic konsumen.ui -o ui_konsumen.py")
    sys.exit()

# Impor fungsi koneksi database kita
from database import connect_db

# --- KELAS UNTUK WINDOW KONSUMEN ---
# (Ini adalah kelas yang kita pindahkan dari main.py)
class KonsumenWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_KonsumenForm()
        self.ui.setupUi(self)

        self.db = None # Variabel untuk menampung koneksi
        self.hubungkan_ke_db() # Panggil fungsi koneksi
        self.konfigurasi_tabel() # Atur header tabel
        self.hubungkan_tombol() # Hubungkan tombol ke fungsi
        self.load_data() # Muat data saat window dibuka

    def hubungkan_ke_db(self):
        self.db = connect_db()
        if not self.db:
            QMessageBox.critical(self, "Error Database", "Tidak bisa terhubung ke database. Aplikasi akan tertutup.")
            self.close()

    def konfigurasi_tabel(self):
        # PASTIKAN nama object tabel Anda 'tableWidget' di Qt Designer
        try:
            self.ui.tableWidget.setColumnCount(5)
            self.ui.tableWidget.setHorizontalHeaderLabels(
                ["ID Pelanggan", "Nama Perusahaan", "Nama Pemilik", "Alamat", "Telpon/Fax"]
            )
            # Atur agar lebar kolom menyesuaikan isi
            self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        except AttributeError:
            print("Error: 'tableWidget' tidak ditemukan di 'ui_konsumen.py'.")

    def hubungkan_tombol(self):
        # PASTIKAN nama object tombol Anda sesuai
        try:
            # Sesuai 'objectName' Anda: pushButton_Simpan
            self.ui.pushButton_Simpan.clicked.connect(self.simpan_data)
            # Sesuai 'objectName' Anda: pushButton_Hapus
            self.ui.pushButton_Hapus.clicked.connect(self.hapus_data)
            # Sesuai 'objectName' Anda: tableWidget
            self.ui.tableWidget.cellClicked.connect(self.data_tabel_diklik)

            # ===============================================
            # --- TOMBOL KELUAR ---
            # (Saya lihat Anda menggunakan pushButton_Keluar di file lama,
            # tapi di file baru Anda, objectName-nya adalah pushB_keluar.
            # Saya akan pakai nama dari screenshot terakhir Anda)
            self.ui.pushB_keluar.clicked.connect(self.close)
            self.ui.pushB_Baru.clicked.connect(self.bersihkan_form)
            self.ui.pushb_ubah.clicked.connect(self.simpan_data)
            self.ui.pushB_Hapus.clicked.connect(self.hapus_data)
            # ===============================================

        except AttributeError as e:
            print(f"Error menghubungkan tombol: {e}. Periksa 'objectName' di Qt Designer.")

    def bersihkan_form(self):
        # Mengosongkan semua input
        self.ui.lineEdit_IdPelanggan.clear()
        self.ui.lineEdit_NamaPerusahaan.clear()
        self.ui.lineEdit_NamaPemilik.clear()
        self.ui.lineEdit_Alamat.clear()         # --- DIUBAH --- (Sesuai objectName Anda)
        self.ui.textEdit.clear()                # --- DIUBAH --- (Sesuai objectName Anda)

    def load_data(self):
        if not self.db or not self.db.is_connected():
            return

        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT id_pel, nm_perusahaan, nm_pemilik, alamat, telp_fax FROM konsumen")
            records = cursor.fetchall()

            self.ui.tableWidget.setRowCount(0) # Kosongkan tabel dulu

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

        # 1. Ambil data dari form (SESUAIKAN NAMA WIDGET)
        id_pel = self.ui.lineEdit_IdPelanggan.text()
        nm_perusahaan = self.ui.lineEdit_NamaPerusahaan.text()
        nm_pemilik = self.ui.lineEdit_NamaPemilik.text()
        alamat = self.ui.lineEdit_Alamat.text()            # --- DIUBAH --- (dari .textEdit_Alamat.toPlainText())
        telp_fax = self.ui.textEdit.toPlainText()          # --- DIUBAH --- (dari .lineEdit_Telpon.text())

        # 2. Validasi sederhana
        if not id_pel or not nm_perusahaan:
            QMessageBox.warning(self, "Input Error", "ID Pelanggan dan Nama Perusahaan wajib diisi.")
            return

        try:
            cursor = self.db.cursor()
            # 3. Buat query SQL (Gunakan 'REPLACE INTO' agar bisa 'Simpan' dan 'Ubah')
            sql = "REPLACE INTO konsumen (id_pel, nm_perusahaan, nm_pemilik, alamat, telp_fax) VALUES (%s, %s, %s, %s, %s)"
            val = (id_pel, nm_perusahaan, nm_pemilik, alamat, telp_fax)

            # 4. Eksekusi
            cursor.execute(sql, val)
            self.db.commit()

            cursor.close()
            QMessageBox.information(self, "Sukses", "Data konsumen berhasil disimpan.")

            # 5. Muat ulang data & bersihkan form
            self.load_data()
            self.bersihkan_form()

        except Exception as e:
            self.db.rollback()
            QMessageBox.critical(self, "Database Error", f"Gagal menyimpan data: {e}")

    def data_tabel_diklik(self, row, column):
        # Fungsi ini akan mengisi form saat baris di tabel diklik
        self.ui.lineEdit_IdPelanggan.setText(self.ui.tableWidget.item(row, 0).text())
        self.ui.lineEdit_NamaPerusahaan.setText(self.ui.tableWidget.item(row, 1).text())
        self.ui.lineEdit_NamaPemilik.setText(self.ui.tableWidget.item(row, 2).text())
        self.ui.lineEdit_Alamat.setText(self.ui.tableWidget.item(row, 3).text())      # --- DIUBAH --- (dari .textEdit_Alamat.setPlainText())
        self.ui.textEdit.setPlainText(self.ui.tableWidget.item(row, 4).text())      # --- DIUBAH --- (dari .lineEdit_Telpon.setText())

    def hapus_data(self):
        # Mengambil ID Pelanggan dari form (yang terisi saat tabel diklik)
        id_pel = self.ui.lineEdit_IdPelanggan.text()
        if not id_pel:
            QMessageBox.warning(self, "Error", "Pilih data dari tabel yang ingin dihapus.")
            return

        # Konfirmasi penghapusan
        konfirmasi = QMessageBox.question(self, "Hapus Data",
            f"Anda yakin ingin menghapus data dengan ID: {id_pel}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if konfirmasi == QMessageBox.StandardButton.Yes:
            try:
                cursor = self.db.cursor()
                sql = "DELETE FROM konsumen WHERE id_pel = %s"
                val = (id_pel,)

                cursor.execute(sql, val)
                self.db.commit()
                cursor.close()

                QMessageBox.information(self, "Sukses", "Data berhasil dihapus.")
                self.load_data()
                self.bersihkan_form()

            except Exception as e:
                self.db.rollback()
                QMessageBox.critical(self, "Database Error", f"Gagal menghapus data: {e}")

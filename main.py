# File: main.py
# File ini HANYA berisi logika untuk window menu utama.

import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow
)
from PySide6.QtCore import Qt

# Impor UI yang sudah di-compile (window utama)
from ui_form import Ui_main

# --- IMPOR LOGIKA ---
# Impor kelas KonsumenWindow dari file logika_konsumen.py
try:
    from logika_konsumen import KonsumenWindow
except ImportError as e:
    print(f"Error: Gagal mengimpor 'logika_konsumen.py'. Detail: {e}")
    sys.exit()

# === IMPOR BARU ===
# Impor kelas AlatBeratWindow dari file logika_alat_berat.py
try:
    from logika_alat_berat import AlatBeratWindow
except ImportError as e:
    print(f"Error: Gagal mengimpor 'logika_alat_berat.py'. Pastikan file sudah ada. Detail: {e}")
    sys.exit()
# ==================


# --- KELAS UNTUK WINDOW UTAMA (MENU) ---
class main(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_main()
        self.ui.setupUi(self)

        # Simpan referensi ke window
        self.window_konsumen = None
        self.window_alat_berat = None # === TAMBAHAN BARU ===

        # Hubungkan menu
        try:
            self.ui.actionKonsumen.triggered.connect(self.tampilkan_konsumen)
            # === KONEKSI BARU ===
            # Pastikan objectName di 'form.ui' Anda adalah 'actionAlat_Berat'
            self.ui.actionAlat_Berat.triggered.connect(self.tampilkan_alat_berat)
            # ====================
        except AttributeError as e:
            print(f"Peringatan: 'action' tidak ditemukan. Periksa 'objectName' di form.ui. Detail: {e}")

    # Fungsi untuk menampilkan window Konsumen
    def tampilkan_konsumen(self):
        if self.window_konsumen is None:
            self.window_konsumen = KonsumenWindow()
        self.window_konsumen.show()
        self.window_konsumen.activateWindow()

    # === FUNGSI BARU ===
    # Fungsi untuk menampilkan window Alat Berat
    def tampilkan_alat_berat(self):
        if self.window_alat_berat is None:
            self.window_alat_berat = AlatBeratWindow()
        self.window_alat_berat.show()
        self.window_alat_berat.activateWindow()
    # ===================


# --- TITIK MASUK UTAMA APLIKASI ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = main()
    widget.show()
    sys.exit(app.exec())

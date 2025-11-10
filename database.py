# File: database.py
import mysql.connector
from mysql.connector import Error

def connect_db():
    """Membuat koneksi ke database pertambangan"""
    try:
        db = mysql.connector.connect(
            host="localhost",       # Sesuaikan jika host Anda berbeda
            user="root",            # Sesuaikan user Anda
            password="",            # Sesuaikan password Anda
            database="pertambangan"
        )
        return db
    except Error as e:
        print(f"Error saat koneksi ke MySQL: {e}")
        return None

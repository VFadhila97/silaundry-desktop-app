"""
Modul storage.py
Mengatur proses membaca dan menyimpan data pesanan laundry ke file CSV
secara permanen menggunakan context manager 'with open()'.
"""

import csv
import os
import typing
from app.models import PesananLaundry

# Lokasi file CSV untuk menyimpan data pesanan laundry
FILE_PATH = "data/pesanan_Laundry.csv"

# Nama kolom pada file CSV
KOLOM_CSV = ["no_nota", "nama_pelanggan", "berat", "layanan","total_harga", "status"]

def inisialisasi_file(path: str = FILE_PATH) -> None:
    """
    Membuat folder 'data' dan file CSV baru jika belum ada.
    Menggunakan mode 'w' untuk menulis header kolom.
    """
    # Membuat folder 'data' otomatis jika belum ada
    folder = os.path.dirname(path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)

    if not os.path.exists(path):
        with open(path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=KOLOM_CSV)
            writer.writeheader()

def muat_seluruh_pesanan(path: str = FILE_PATH) ->list[PesananLaundry]:
     """
     Membaca sluruh data pesanan laundry dari file CSV dan mengubahnya menjadi list berisi objek PesananLaundry.
     Dilengkapi try except untuk menangani error saat menangani file error atau file tidak ditemukan.
     """
     daftar_pesanan = []
      
     try:
          with open(path, mode="r", newline="", encoding="utf-8") as file:
               reader = csv.DictReader(file)
               for baris in reader:
                    pesanan = PesananLaundry.from_dict(baris)
                    daftar_pesanan.append(pesanan)
                    
     except FileNotFoundError:
          print("Info: File data belum ditemukan. Membuat file database baru...")
          inisialisasi_file(path)
          
     except (ValueError, KeyError) as error:
          print(f"Peringatan: Ada data rusak di dalam file CSV ({error}).")
          
     return daftar_pesanan

def simpan_seluruh_pesanan(daftar_pesanan: list[PesananLaundry], path: str = FILE_PATH) -> None:
     """
     Menyimpan ulang seluruh list objek PesananLaundry ke dalam file CSV (mode 'w').
     Digunakan setiap kali ada penambahan, update status, atau penghapusan data.
     """
     inisialisasi_file(path) 
     
     with open(path, mode="w", newline="", encoding="utf-8") as file:
          writer = csv.DictWriter(file, fieldnames=KOLOM_CSV)
          writer.writeheader()
          for pesanan in daftar_pesanan:
               writer.writerow(pesanan.to_dict())
               
def tambah_satu_pesanan(pesanan: PesananLaundry, path: str = FILE_PATH) -> None:
     """
     Menambahkan satu baris pesanan baru ke bagian paling bawah file CSV
     menggunakan mode append ('a').
     """
     inisialisasi_file(path)
     
     with open(path, mode="a", newline="", encoding="utf-8") as file:
          writer = csv.DictWriter(file, fieldnames=KOLOM_CSV)
          writer.writerow(pesanan.to_dict())
          
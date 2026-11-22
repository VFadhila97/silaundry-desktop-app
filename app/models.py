"""
Modul models.py
Berisi definisi class utama untuk merepresentasikan entitas data
pada aplikasi SiLaundry (Sistem Informasi Manajemen Laundry Kiloan).
"""

from typing import Optional


class PesananLaundry:
     # Konstanta daftar tarif layanan per kilogram (dalam Rupiah)
     TARIF_LAYANAN = {
          "Reguler" : 5000,
          "Express" : 10000,
          "Setrika" : 3000
     }
     
     def __init__(self, no_nota: str, nama_pelanggan: str, layanan: str, berat_kg: float, total_harga: Optional[int] = None, status: str = "Proses",):
          """
          Inisialisasi objek pesananLaundry.

          Args:
               no_nota (str): Nomor nota pesanan.
               nama_pelanggan (str): Nama pelanggan.
               berat_kg (float): Berat laundry dalam kilogram.
               layanan (str): Jenis layanan laundry (Reguler, Express, Setrika).
               status (str): Status pesanan (default: "Proses").
               total_harga (int): Total harga pesanan (default: None).
          """
          self.no_nota = no_nota
          self.nama_pelanggan = nama_pelanggan
          self.berat = float(berat_kg)
          self.layanan = layanan
          self.status = status
          
          # Menggunakan fungsi lambda untuk kalkulasi harga otomatis jika belum diisi
          hitung_otomatis = lambda b, tarif: int(round(b * tarif))
          if total_harga is None:
               tarif_per_kg = self.TARIF_LAYANAN.get(layanan, 6000)
               self.total_harga = hitung_otomatis(self.berat, tarif_per_kg)
          else:
               self.total_harga = int(total_harga)
               
     def to_dict(self) -> dict:
          return {
               "no_nota": self.no_nota,
               "nama_pelanggan": self.nama_pelanggan,
               "berat": self.berat,
               "layanan": self.layanan,
               "status": self.status,
               "total_harga": self.total_harga
          }
     
     @classmethod
     def from_dict(cls, data: dict) -> "PesananLaundry":
        """
        Membuat kembali objek PesananLaundry dari baris dictionary
        hasil pembacaan file CSV.
        """
        return cls(
            no_nota=data["no_nota"],
            nama_pelanggan=data["nama_pelanggan"],
            layanan=data["layanan"],
            berat_kg=float(data["berat_kg"]),
            total_harga=int(data["total_harga"]),
            status=data["status"],
        )
        
     def __str__(self) -> str:
          return (
            f"PesananLaundry(no_nota='{self.no_nota}', "
            f"nama='{self.nama_pelanggan}', total={self.total_harga})"
        )
          
# =======================================================
# Project Based Learning: Sistem Manajemen Data Mahsiswa
# Dibuat oleh: Febryanto Nugroho
# NPM: 202243500473
# Kelas: S7D
# =======================================================

class Mahasiswa:
    def __init__(self, npm, nama, prodi, angkatan):
        self.npm = npm
        self.nama = nama
        self.prodi = prodi
        self.angkatan = angkatan

    def tampilkan_data(self):
        print(f"NPM: {self.npm}")
        print(f"Nama: {self.nama}")
        print(f"Program Studi: {self.prodi}")
        print(f"Angkatan: {self.angkatan}")
        print("-" * 40)


class SistemMahsiswa:
    def __init__(self):
        self.data_mahasiswa = []

    def tambah_data(self):
        npm = input("Masukan NPM: ")
        nama = input("Masukkan Nama: ")
        prodi = input("Masukkan Tahun Prodi: ")
        angkatan = input("Masukkan Tahun Angkatan ")
        mahasiswa = Mahasiswa(npm, nama, prodi, angkatan)
        self.data_mahasiswa.append(mahasiswa)
        print("✅ Data berhasil ditambahkan!\n")

    def tampilkan_semua(self):
        if not self.data_mahasiswa:
            print("⚠️ Belum ada data mahasiswa.\n")
        else:
            print("\n=== Daftar Mahasiswa ===")
            for mhs in self.data_mahasiswa:
                mhs.tampilkan_data()

    def cari_data(self):
        npm = input("Masukkan NPM yang dicari: ")
        for mhs in self.data_mahasiswa:
            if mhs.npm == npm:
                print("\n=== Data Ditemukan.\n")
                mhs.tampilkan_data()
                return
        print("❌ Data tidak ditemukan.\n")

    def ubah_data (self):
        npm = input("Masukkan NPM yang akan diubah: ")
        for mhs in self.data_mahasiswa:
            if mhs.npm == npm:
                mhs.nama = input("Nama baru: ")
                mhs.prodi = input("Prodi baru: ")                                   
                mhs.angkatan = input("Angkatan baru: ")
                print("✅ Data berhasil diubah!\n")
                return
        print("❌ Data tidak ditemukan.\n")
            
    def hapus_data(self):
        npm = input("Masukkan NPM yang akan dihapus!\n")
        for mhs in self.data_mahasiswa:
            if mhs.npm == npm:
                self.data_mahasiswa.remove(mhs)
                print("✅ Data berhasil dihapus!\n")
                return
        print("❌ Data tidak ditemukan.\n")


def main():
    sistem = SistemMahsiswa()

    while True:
        print("""
======= MENU SISTEM MAHASISWA =======
1. Tambah Data Mahasiswa
2. Tampilkan Semua Data
3. Cari Data Mahasiswa
4. Ubah Data Mahasiswa
5. Hapus Data Mahasiswa
6. Keluar
====================================
""")             
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            sistem.tambah_data()
        elif pilihan == "2":
            sistem.tampilkan_semua()
        elif pilihan == "3":
            sistem.cari_data()
        elif pilihan == "4":
            sistem.ubah_data()
        elif pilihan == "5":
            sistem.hapus_data()
        elif pilihan == "6":
            print("Terima kasih telah menggunakan sistem ini. 👋")
            break
        else:
            print("⚠️ Pilihan tidak valid, coba lagi.\n")


if __name__ == "__main__":
    main()
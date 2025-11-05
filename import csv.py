import csv

# ======= Fungsi Menyimpan Data ke File =======
def simpan_data(data):
    with open("data_pasien.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Nama", "Umur", "Jenis Kelamin", "Keluhan", "Dokter"])
        writer.writerows(data)

# ======= Fungsi Membaca Data dari File =======
def baca_data():
    try:
        with open("data_pasien.csv", mode="r") as file:
            reader = csv.reader(file)
            next(reader) # Lewati header
            return list(reader)
    except FileNotFoundError:
        return []

# ======= Fungsi Menambah Data Pasien =======
def tambah_pasien():
    print("\n--- Tambah Data Pasien ---")
    nama = input("Nama Pasien       : ")
    umur = input("Umur              : ")
    jk = input("Jenis Kelamin (L/P): ")
    keluhan = input("Keluhan           : ")
    dokter = input("Dokter Penanggung : ")

    data = baca_data()
    data.append([nama, umur, jk, keluhan, dokter])
    simpan_data(data)
    print("✅ Data pasien berhashil disimpan!\n")

# ======= Fungsi Menampilkan Semua Data =======
def tampilkan_data():
    data = baca_data()
    if not data:
         print("\n⚠️ Belum ada data pasien.\n")
         return

    print("\n--- Daftar Pasien ---")
    for i, pasien in enumerate(data, start=1): 
        print(f"{i}. Nama: {pasien[0]} | Umur: {pasien[1]} | JK: {pasien[2]} | Keluhan: {pasien}[3] | Dokter: {pasien[4]}")
    print()

# ======= Fungsi Menghapus Data =======
def hapus_data():
    tampilkan_data()
    data = baca_data()
    if not data:
        return

    try:
        index = int(input("Masukkan nomor pasien yang akan dihapus: ")) -1
        if 0 <= index < len(data):
            del data[index]
            simpan_data
            print("🗑️ Data pasien berhasil dihapus!\n")
        else:
            print("❌ Nomor tidak valid.\n")
    except ValueError:
        print("❌ Input harus berupa angka.\n")

# ======= Menu Utama =======
def menu():
    while True:
        print("====== APLIKASI KLINIK MINI ======")
        print("1. Tambah Data pasien")
        print("2. Lihat Data Pasien")
        print("3. Hapus Data Pasien")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            tambah_pasien()
        elif pilihan == "2":
            hapus_data()
        elif pilihan == "3":
            hapus_data()
        elif pilihan == "4":
             print("Terima kasih telah menggunakan applikasi klinik mini 😊")
        break
    else:
        print("❌ Pilihan tidak valid, coba lago.\n")

# ======= Jalankan Program =======
menu()                                    
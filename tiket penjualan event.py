# ===========================
# APLIKASI PENJUALAN TIKET EVENT
# Dibuat oleh: Fberyanto Nugroho
# NPM: 202243500473
# Kelas: S7D
# ===========================

# Daftar event harga tiket
daftar_event = {
    "Konser Musik": 150000,
    "Seminar Teknologi": 100000,
    "Festival kuliner": 80000,
    "Lomba Esport": 120000
}

# Menampilkan daftar event
print("=== APLIKASI PENJUALAN TIKER EVENT ===")
print("Daftar Event yang tersedia:")
for i, (event, harga) in enumerate(daftar_event.items(), start=1):
    print(f"{i}. {event} - Rp{harga}")

# Input data pembelian
nama = input("\nMasukkan Nama Pembeli: ")
pilih = int(input("Pilih Nomor Event (1-4): "))
jumlah = int(input("Masukkan Jumlah Tiket: "))

# Mengambil nama event berdasarkan pilihan
event_terpilih = list(daftar_event.keys())[pilih - 1]
harga_tiket = daftar_event[event_terpilih]
total = harga_tiket * jumlah

# Menampilkan ringkasan pembelian
print("\n=== STRUK PEMBELIAN TIKET ===")
print(f"Nama Pembeli      : {nama}")
print(f"Event             : {event_terpilih}")
print(f"Harga per Tiket   : Rp{harga_tiket}")
print(f"Jumlah Tiket      : {jumlah}")
print(f"Total Bayar       : Rp{total}")

# Input pembayaran
bayar = int(input("\nMasukkan Uang Pembeli: Rp"))
kembalian = bayar - total

print(f"kembalian            : Rp{kembalian}")
print("======================================")
print("Terima kasih telah membeli tiket!")
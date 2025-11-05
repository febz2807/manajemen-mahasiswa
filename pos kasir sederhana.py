# =========================
# Aplikasi Kasir Sederhana
# Dibuat oleh: Febryanto Nugroho
# NPM: 202243500473
# Kelas: S7D
# =========================

# Membuat List untuk menyimpan data barang
daftar_barang = []

print("=== APLIKASI KASIR SEDERHANA ===")
print("Masukan data barang menampilkan total\n")
print("Ketik 'selesai' untuk menampilkan total\n")

# Loop untuk input data barang
while True:
    nama = input("Nama Barang: ")
    if nama.lower() == 'selesai':
        break # keluar dari perulangan jika user mengetik 'selesai'

    harga = int(input("Harga Barang"))
    jumlah = int(input("Jumlah Barang"))

    subtotal = harga * jumlah
    daftar_barang.append({
        "nama": nama,
        "harga": harga,
        "jumlah": jumlah,
        "subtotal": subtotal
    })
    print(f"Subtotal untuk {nama}: Rp{subtotal}")
    print("----------------------------")

# Menampilkan struk belanja
print("\n======== STRUK PEMBAYARAN ========")
total = 0
for barang in daftar_barang:
    print(f"{barang['nama']} ({barang['jumlah']} x {barang['harga']}) = Rp{barang['subtotal']}")
    total += barang['subtotal']

print("--------------------------------------")
print(f"TOTAL BAYAR: Rp{total}")

# Input pembayaran
bayar = int(input("Masukkan Uang Pembeli: Rp"))
kembalian = bayar - total
print(f"kembalian: Rp{kembalian}")

print("===============================")
print("Terima kasih telah berbelanja di toko kami")

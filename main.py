from penyimpanan import baca_data, menulis_data

from barang_tambah_tampil import tambah_barang, tampilkan_barang
from barang_kelola import edit_barang, hapus_barang, kelompok_kategori
from stok import tambah_stok, kurangi_stok, tampilkan_stok

from transaksi import buat_transaksi
from pembayaran import proses_pembayaran

from Riwayat import simpan_riwayat, tampilkan_riwayat, total_pendapatan

data = baca_data()

# Menu manajemen barang
def menu_barang():
    while True:
        print("\n=== MANAJEMEN BARANG ===")
        print("1. Tambah Barang")
        print("2. Tampilkan Barang")
        print("3. Edit Barang")
        print("4. Hapus Barang")
        print("5. Kelompokkan Barang")
        print("0. Kembali")
 
        pilihan = input("Pilih menu: ")
 
        if pilihan == "1":
            tambah_barang(data)
            menulis_data(data)
 
        elif pilihan == "2":
            tampilkan_barang(data)
 
        elif pilihan == "3":
            edit_barang(data)
            menulis_data(data)
 
        elif pilihan == "4":
            hapus_barang(data)
            menulis_data(data)
 
        elif pilihan == "5":
            kelompok_kategori(data)
 
        elif pilihan == "0":
            break
 
        else:
            print("Pilihan tidak tersedia!")

# Menu manajemen stok
def menu_stok():
    while True:
        print("\n=== MANAJEMEN STOK ===")
        print("1. Tambah Stok")
        print("2. Kurangi Stok")
        print("3. Tampilkan Stok")
        print("0. Kembali")
 
        pilihan = input("Pilih menu: ")
 
        if pilihan == "1":
            tambah_stok(data)
            menulis_data(data)
 
        elif pilihan == "2":
            kurangi_stok(data)
            menulis_data(data)
 
        elif pilihan == "3":
            tampilkan_stok(data)
 
        elif pilihan == "0":
            break
 
        else:
            print("Pilihan tidak tersedia!")

# Menu transaksi penjualan
def menu_transaksi():
    print("\n=== TRANSAKSI PENJUALAN ===")
 
    transaksi = buat_transaksi(data)
 
    if transaksi != None:
        hasil = proses_pembayaran(data, transaksi)
 
        if hasil != None:
            simpan_riwayat(data, hasil)
            menulis_data(data)

# Menu riwayat penjualan
def menu_riwayat():
    while True:
        print("\n=== MENU RIWAYAT PENJUALAN ===")
        print("1. Tampilkan Riwayat")
        print("2. Total Pendapatan")
        print("0. Kembali")
 
        pilihan = input("Pilih menu: ")
 
        if pilihan == "1":
            tampilkan_riwayat(data)
 
        elif pilihan == "2":
            total_pendapatan(data)
 
        elif pilihan == "0":
            break
 
        else:
            print("Pilihan tidak tersedia!")

# Menu utama
def menu_utama():
    while True:
        print("\n================================")
        print(" SISTEM INVENTARIS TOKO KataLoGue")
        print("================================")
        print("1. Manajemen Barang")
        print("2. Manajemen Stok")
        print("3. Transaksi Penjualan")
        print("4. Riwayat Penjualan")
        print("0. Keluar")
        print("================================")
 
        pilihan = input("Pilih menu: ")
 
        if pilihan == "1":
            menu_barang()
 
        elif pilihan == "2":
            menu_stok()
 
        elif pilihan == "3":
            menu_transaksi()
 
        elif pilihan == "4":
            menu_riwayat()
 
        elif pilihan == "0":
            menulis_data(data)
            print("Terima kasih telah menggunakan program kami!")
            break
 
        else:
            print("Pilihan tidak tersedia!")

# Menjalankan program
menu_utama()
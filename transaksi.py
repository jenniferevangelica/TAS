
from utils import input_teks, input_angka_positif

# mencari barang berdasarkan kode
def cari_barang(data, kode):
    for barang in data["barang"]:
        if barang["kode"] == kode:
            return barang
 
    return None
 
 
# Fungsi membuat transaksi
def buat_transaksi(data):
    print("\n=== TRANSAKSI PENJUALAN ===")
 
    keranjang = []
 
    if len(data["barang"]) == 0:
        print("Belum ada barang yang tersedia.")
        return None
 
    while True:
        print("\n=== DAFTAR BARANG ===")
 
        for barang in data["barang"]:
            print("------------------------------")
            print("Kode :", barang["kode"])
            print("Nama :", barang["nama"])
            print("Harga: Rp", barang["harga"])
            print("Stok :", barang["stok"])
 
        kode = input_teks("\nMasukkan kode barang (0 untuk selesai): ")
 
        if kode == "0":
            break
 
        barang = cari_barang(data, kode)
        # Menghitung jumlah barang yang sudah masuk keranjang
        if barang == None:
            print("Barang tidak ditemukan!")
        else:
            
            jumlah_di_keranjang = 0
 
            for item in keranjang:
                if item["kode"] == kode:
                    jumlah_di_keranjang = jumlah_di_keranjang + item["jumlah"]
 
            stok_tersedia = barang["stok"] - jumlah_di_keranjang
 
            if stok_tersedia <= 0:
                print("Stok barang tidak tersedia!")
            else:
                print("Nama barang :", barang["nama"])
                print("Stok tersedia:", stok_tersedia)
 
                jumlah = input_angka_positif(
                    "Masukkan jumlah pembelian: "
                )
 
                if jumlah > stok_tersedia:
                    print("Jumlah pembelian melebihi stok!")
                else:
                    subtotal = barang["harga"] * jumlah
 
                    item_baru = {
                        "kode": barang["kode"],
                        "nama": barang["nama"],
                        "harga": barang["harga"],
                        "jumlah": jumlah,
                        "subtotal": subtotal
                    }
 
                    keranjang.append(item_baru)
 
                    print("Barang berhasil dimasukkan ke keranjang!")
                    print("Subtotal: Rp", subtotal)


    # Menghitung total belanja
    if len(keranjang) == 0:
        print("Tidak ada barang yang dibeli.")
        return None
 
    
    total = 0
 
    print("\n=== RINCIAN BELANJA ===")
 
    for item in keranjang:
        print("------------------------------")
        print("Nama barang :", item["nama"])
        print("Harga       : Rp", item["harga"])
        print("Jumlah      :", item["jumlah"])
        print("Subtotal    : Rp", item["subtotal"])
 
        total = total + item["subtotal"]
 
    print("------------------------------")
    print("TOTAL BELANJA: Rp", total)
 
    transaksi = {
        "daftar_barang": keranjang,
        "total": total
    }
 
    return transaksi

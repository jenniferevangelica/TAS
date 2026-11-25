from utils import input_angka

def proses_pembayaran(data, transaksi):

    print("\n=== PEMBAYARAN ===")

    # Cek transaksi
    if transaksi == None:
        print("Tidak ada transaksi!")
        return None

    # total belanja
    total = transaksi["total"]

    print("Total belanja: Rp", total)

    # Mengambil uang pembayaran
    while True:
        bayar = input_angka("Masukkan uang pembayaran: ")

        if bayar >= total:
            break
        else:
            print("Uang pembayaran kurang!")
            print("Kekurangan: Rp", total - bayar)

    # Menghitung kembalian
    kembalian = bayar - total

    # Mengurangi stok barang
    for item in transaksi["daftar_barang"]:
        for barang in data["barang"]:
            if barang["kode"] == item["kode"]:
                barang["stok"] -= item["jumlah"]
                break

    # Menampilkan struk
    print("\n=== STRUK PEMBAYARAN ===")
    print("Total belanja :", total)
    print("Uang bayar    :", bayar)
    print("Kembalian     :", kembalian)
    print("Pembayaran berhasil!")

    # Menyimpan data pembayaran
    transaksi["bayar"] = bayar
    transaksi["kembalian"] = kembalian

    return transaksi
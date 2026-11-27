from utils import input_angka

def proses_pembayaran(data, transaksi):

    print("\n=== PEMBAYARAN ===")

    
    if transaksi == None:
        print("Tidak ada transaksi!")
        return None

    
    total = transaksi["total"]

    print("Total belanja: Rp", total)

    
    while True:
        bayar = input_angka("Masukkan uang pembayaran: ")

        if bayar >= total:
            break
        else:
            print("Uang pembayaran kurang!")
            print("Kekurangan: Rp", total - bayar)

    
    kembalian = bayar - total

    
    for item in transaksi["daftar_barang"]:
        for barang in data["barang"]:
            if barang["kode"] == item["kode"]:
                barang["stok"] -= item["jumlah"]
                break

    
    print("\n=== STRUK PEMBAYARAN ===")
    print("Total belanja :", total)
    print("Uang bayar    :", bayar)
    print("Kembalian     :", kembalian)
    print("Pembayaran berhasil!")

    
    transaksi["bayar"] = bayar
    transaksi["kembalian"] = kembalian

    return transaksi
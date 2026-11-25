from datetime import datetime


def simpan_riwayat(data, transaksi, uang_diterima, kembalian):

    if transaksi is None:
        return

    if "riwayat_transaksi" not in data:
        data["riwayat_transaksi"] = []

    nomor = len(data["riwayat_transaksi"]) + 1

    riwayat_baru = {
        "nomor_transaksi": "KLG" + str(nomor).zfill(3),
        "tanggal": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "daftar_barang": transaksi["daftar_barang"],
        "total": transaksi["total"],
        "uang_diterima": uang_diterima,
        "kembalian": kembalian
    }

    data["riwayat_transaksi"].append(riwayat_baru)

    return riwayat_baru


def tampilkan_riwayat(data):

    print("\n=== RIWAYAT PENJUALAN ===")

    riwayat = data.get("riwayat_transaksi", [])

    if len(riwayat) == 0:
        print("Belum ada transaksi penjualan.")
        return

    for transaksi in riwayat:
        print("----------------------------------")
        print("Nomor Transaksi :", transaksi["nomor_transaksi"])
        print("Tanggal         :", transaksi["tanggal"])
        print("Total Belanja   : Rp", transaksi["total"])

    print("----------------------------------")


def tampilkan_detail_transaksi(data):

    riwayat = data.get("riwayat_transaksi", [])

    if len(riwayat) == 0:
        print("\nBelum ada transaksi penjualan.")
        return

    tampilkan_riwayat(data)

    nomor = input("\nMasukkan nomor transaksi: ").strip()

    transaksi_ditemukan = None

    for transaksi in riwayat:
        if transaksi["nomor_transaksi"] == nomor:
            transaksi_ditemukan = transaksi
            break

    if transaksi_ditemukan is None:
        print("Nomor transaksi tidak ditemukan.")
        return

    print("\n=== DETAIL TRANSAKSI ===")
    print("Nomor Transaksi :", transaksi_ditemukan["nomor_transaksi"])
    print("Tanggal         :", transaksi_ditemukan["tanggal"])

    print("\nBarang yang dibeli:")

    for barang in transaksi_ditemukan["daftar_barang"]:
        print("----------------------------------")
        print("Kode Barang :", barang["kode"])
        print("Nama Barang :", barang["nama"])
        print("Harga       : Rp", barang["harga"])
        print("Jumlah      :", barang["jumlah"])
        print("Subtotal    : Rp", barang["subtotal"])

    print("----------------------------------")
    print("Total Belanja : Rp", transaksi_ditemukan["total"])

    print("Uang Diterima : Rp", transaksi_ditemukan["uang_diterima"])
    print("Kembalian     : Rp", transaksi_ditemukan["kembalian"])


def total_pendapatan(data):

    total_pendapatan = 0

    riwayat = data.get("riwayat_transaksi", [])

    for transaksi in riwayat:
        total_pendapatan += transaksi["total"]

    return total_pendapatan


def tampilkan_laporan_pendapatan(data):

    jumlah_transaksi = len(data.get("riwayat_transaksi", []))

    total_pendapatan = hitung_total_pendapatan(data)

    print("\n=== LAPORAN PENDAPATAN TOKO ===")
    print("----------------------------------")
    print("Jumlah Transaksi :", jumlah_transaksi)
    print("Total Pendapatan : Rp", total_pendapatan)
    print("----------------------------------")


def menu_riwayat_laporan(data):

    while True:
        print("\n=== MENU RIWAYAT DAN LAPORAN ===")
        print("1. Tampilkan Riwayat Penjualan")
        print("2. Tampilkan Detail Transaksi")
        print("3. Tampilkan Total Pendapatan")
        print("0. Kembali ke Menu Utama")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_riwayat(data)

        elif pilihan == "2":
            tampilkan_detail_transaksi(data)

        elif pilihan == "3":
            tampilkan_laporan_pendapatan(data)

        elif pilihan == "0":
            break

        else:
            print("Pilihan tidak tersedia. Silakan coba lagi.")
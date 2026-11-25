from utils import input_teks, imput_angka, input_angka_positif

def cari_barang(data, kode):
    for barang in data["barang"]:
        if barang["kode"] == kode:
            return barang

    return None

def edit_barang(data):
    print("\n=== EDIT BARANG ===")

    kode = input_teks("Masukkan kode barang yang ingin diedit: ")

    barang = cari_barang(data, kode)

    if barang == None:
        print("Barang tidak ditemukan!")
    else:
        print("\nData barang ditemukan:")

        print("Nama lama:", barang["nama"])
        print("Kategori lama:", barang["kategori"])
        print("Harga lama: Rp", barang["harga"])

        print("\nMasukkan data baru.")
        nama = input_teks("Nama barang: ")
        kategori = input_teks("Kategori barang: ")
        harga = input_angka_positif("Harga barang: ")

        barang["nama"] = nama
        barang["kategori"] = kategori
        barang["harga"] = harga

        print("\nData barang berhasil diperbarui!")

def hapus_barang(data):
    print("\n=== HAPUS BARANG ===")

    kode = input_teks("Masukkan kode barang yang ingin dihapus: ")

    barang = cari_barang(data, kode)

    if barang == None:
        print("Barang tidak ditemukan!")
    else:
        print("\nData barang ditemukan:")
        print("Nama barang :", barang["nama"])

        konfirmasi = input("Apakah Anda yakin ingin menghapus barang ini? (y/n): ")

        if konfirmasi.lower() == "y":
            data["barang"].remove(barang)
            print("Barang berhasil dihapus!")
        else:
            print("Penghapusan barang dibatalkan.")

def kelompok_kategori(data):
    print("\n=== KELOMPOKKAN BARANG BERDASAARKAN KATEGORI ===")

    if len(data["barang"]) == 0:
        print("Belum ada barang yang tersedia")
    else:
        kategori_ditemukan = []

        for barang in data["barang"]:
            kategori = barang["kategori"]

            if kategori not in kategori_ditemukan:
                kategori_ditemukan.append(kategori)

        for kategori in kategori_ditemukan:
            print("\nKategori:", kategori)

            for barang in data["barang"]:
                if barang["kategori"] == kategori:
                    print("-----------------------------")
                    print("Kode :", barang["kode"])
                    print("Nama :", barang["nama"])
                    print("Harga :Rp", barang["harga"])
                    print("Stok :", barang["stok"])
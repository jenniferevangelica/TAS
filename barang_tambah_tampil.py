from utils import input_teks, input_angka, input_angka_positif

def tambah_barang(data):
    print("\n=== TAMBAH BARANG ===")

    kode = input_teks("Masukkan kode barang: ")

    for barang in data["barang"]:
        if barang["kode"] == kode:
            print("Kode barang sudah digunakan.")
            return 

    nama = input_teks("Masukkan nama barang: ")
    kategori = input_teks("Masukkan kategori barang: ")
    harga = input_angka_positif("Masukkan harga barang: ")
    stok = input_angka("Masukkan stok barang")

    barang_baru = {
        "kode" : kode,
        "nama" : nama,
        "kategori" : kategori, 
        "harga" : harga,
        "stok" : stok
    }

    data["barang"].append(barang_baru)
    print("\nBarang berhasil ditambahkan. ")

def tampilkan_barang(data):
    print("\n=== DAFTAR BARANG TOKO KataLoGue")

    if len(data["barang"]) == 0:
        print("Belum ada barang yang tersedia.")
    else:
        for barang in data["barang"]:
            print("------------------------------")
            print("Kode Barang :", barang["kode"])
            print("Nama Barang :", barang["nama"])
            print("Kategori    :", barang["kategori"])
            print("Harga Barang : Rp", barang["harga"])
            print("Stok         :", barang["stok"])

        print("------------------------------")
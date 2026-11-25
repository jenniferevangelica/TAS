from utils import input_teks, input_angka_positif, input_pilihan
from transaksi import cari_barang

BATAS_STOK_MINIMUM = 5

def tampilkan_stok(data):
    print("\n=== JUMPLAH STOK BARANG ===")

    if len(data["barang"]) == 0:
        print("Belum ada barang yang tersedia.")
        return
    total_stok = 0
    for barang in data["barang"]:
        print("----------------------------")
        print("Kode Barang :", barang ["kode"])
        print("Nama Barang :", barang ["nama"])
        print("Stok        :", barang ["stok"])

        tital_stok = total_stok = barang["stok"]

    print("----------------------------")
    print("Total seluruh stok:", total_stok)

#MENAMBAH STOK BARANG

def tambah_stok(data):
    print("\n=== TAMBAH STOK ===")

    if len(data["barang"]) == 0:
        print("Baeum ada barang yang tersedia.")
        return

    kode = input_teks("Masukan kode barang: ").strip()
    barang = cari_barang(data, kode)

    if barang == None:
        print("Barang tidak ditemukan!")
        return
    print("Nama barang :", barang["nama"])
    print("Stok saat ini :", barang["stok"])

    jumlah = input_angka_positif("Masukan jumlah stok yang ditambahkan: ")
    barang["stok"] = barang["stok"] + jumlah

    print("\nStok berhasil ditambahkan.")
    print("Stok sekarang:", barang["stok"])

#Mengurangi stok barang
def kurangi_stok(data):
    print("\n== KURANGINSTOK ===")

    if len(data["barang"]) == 0:
        print("Belum ada barang yang tersedia.")
        return

    kode = input_teks("Masukan kode barang: ").strip()
    barang = cari_barang(data, kode)

    if barang == None:
        print("Barang tidak ditemukan!")
        return
    print("Nama barang  :", barang["nama"])
    print("Stok saat ini:", barang["stok"])

    if barang["stok"] == 0:
        print("Stok sudah 0, tidak bisa dikurangin!")
        return
    jumlah = input_angka_positif("Masukan jumlah stok yang dikurangin: ")

    #stok tidak boleh negatif
    if jumlah > barang["stok"]:
        print("Jumlah pengurangan melebihi stok yang tersedia!")
        return

    barang["stok"] = barang["stok"] - jumlah

    print("\nStok berhasil dikurangi.")
    print("Stok sekarang:", barang["stok"])

#menampilkan barang
def tampilkan_stok_hampir_habis(data):
    print("\n=== BARANG HAMPIR HABIS (stok <=", BATAS_STOK_MINIMUM, ")===")

    ada = False

    for barang in data["barang"]:
        if barang["stok"] <= BATAS_STOK_MINIMUM:
            print("------------------------------")
            print("Kode Barang :", barang["kode"])
            print("Nama Barang :", barang["nama"])
            print("Stok        :", barang["stok"])
            ada = True

        if ada == False:
            print("Semua stok masih aman.")
        else:
            print("------------------------------")


#transaksi

def kurangi_stok_transaksi(data, transaksi):
    for item in transaksi["daftar_barang"]:
        barang = cari_barang(data, item["kde"])

        if barang != None:
            barang["stok"] = barang["stok"] - item["jumlah"]

# submenu
def menu_stok(data):
    while True:
        print("\n=== MANAJEMEN STOK ===")
        print("1. Tambah stok")
        print("2. Kurangin stok")
        print("3. Tampilan jumplah stok")
        print("4. Tampilan barang hampir habis")
        print("0. Kembali")

        pilihan = input_pilihan("Pilihan menu: ", ["1", "2", "3","4", "0"])

        if pilihan == "1":
            tambah_stok(data)
        elif pilihan == "2":
            kurangi_stok(data)
        elif pilihan == "3":
            tampilkan_stok(data)
        elif pilihan == "4":
            tampilkan_stok_hampir_habis(data)
        else:
            break

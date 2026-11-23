class Barang:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def info_barang(self):
        return f"Nama: {self.nama}, Harga: {self.harga}, Stok: {self.stok}"
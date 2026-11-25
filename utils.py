def input_teks(pesan):
    while True:
        teks = input(pesan)

        if teks.strip() !="":
            return teks
        else:
            print("Tidak boleh kosong!")

def input_angka(pesan):
    while True:
        try:
            angka = int(input(pesan))

            if angka >+ 0:
                return angka 
            else:
                print("Angka tidak boleh negatif")
        except ValueError:
            print("Harus berupa angka bulat!")

def input_angka_positif(pesan):
    while True:
        try:
            angka = int(input(pesan))

            if angka > 0:
                return angka 
            else:
                print("Angka harus lebih dari 0!")
        except ValueError:
            print("Harus berupa angka bulat!")

def input_pilihan(pesan, pilihan):
    while True:
        pilih = input(pesan)

        if pilih in pilihan:
            return pilih 
        else:
            print("Pilihan tidak tersedia")
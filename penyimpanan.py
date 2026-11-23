import json

def baca_data():
    try:
        file = open("data_toko_KataLoGue.json", "r")
        data = json.load(file)
        file.close()
        return data

    except FileNotFoundError:
        data = {
            "barang": [],
            "riwayat": []
        }
        return data 

    except json.JSONDecodeError:
        print("Data tidak dapat dibaca.")
        data = {
            "barang": [],
            "riwayat": []
        }
        return data

def menulis_data(data):
    file = open("data_toko_KataLoGue.json", "w")
    json.dump(data, file, indent=4)
    file.close()
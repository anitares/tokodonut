# Nama toko
print("Donut Ceria Bikin Mood Selalu Ceria")

# Data menu dalam daftar dictionary
list_menu = [{"id": 1, "nama": "donut greentea", "harga": 12000, "stok": "20pcs"},
    {"id": 2, "nama": "donut vanilla", "harga": 10000, "stok": "20pcs"},
    {"id": 3, "nama": "donut mocca", "harga": 12500, "stok": "15pcs"},]

# Create
def tambah_donut(nama, harga, stok):
    list_menu.append({
        "nama": nama,
        "harga": harga,
        "stok": stok
    })
    print("Data berhasil ditambahkan")

# Read
def tampilkan_donut():
    if not list_menu:
        print("Donut belum tersedia")
    else:
        print("Menu donut:")
        for idx, donut in enumerate(list_menu, start=1):
            print(
                f"ID: {idx}, Nama: {donut['nama']}, harga: {donut['harga']}, Stok: {donut['stok']}")

# Update
def update_donut(id, nama, harga, stok):
    if 1 <= id <= len(list_menu):
        donut = list_menu[id - 1]
        donut["nama"] = nama
        donut["harga"] = harga
        donut["stok"] = stok
        print("Menu donut telah diperbarui")
    else:
        print("Menu donut belum tersedia")

# Delete
def hapus_donut(id):
    if 1 <= id <= len(list_menu):
        del list_menu[id - 1]
        print("Menu donut telah dihapus")
    else:
        print("Menu donut belum tersedia")

# Role
print("Pilihan Role")
print("1. admin")
print("2. pembeli")

pilihan = int(input("Masukkan pilihan (1-2): "))

# Admin
if pilihan == 1:
    print("Admin Donut Ceria")
    while True:
        print("\nPilihan Menu:")
        print("1. Tambah data donut")
        print("2. Tampilkan data donut")
        print("3. Update data donut")
        print("4. Hapus data donut")
        print("5. Keluar")

        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            nama = input("Masukkan menu donut: ")
            harga = int(input("Masukkan harga: "))
            stok = input("Masukkan stok: ")
            tambah_donut(nama, harga, stok)
        elif pilihan == "2":
            tampilkan_donut()
        elif pilihan == "3":
            id = int(input("Masukkan ID data menu yang ingin diperbarui: "))
            nama = input("Masukkan menu donut baru: ")
            harga = int(input("Masukkan harga baru: "))
            stok = input("Masukkan stok baru: ")
            update_donut(id, nama, harga, stok)
        elif pilihan == "4":
            id = int(input("Masukkan ID data menu donut yang ingin dihapus: "))
            hapus_donut(id)
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid")

# Pembeli
elif pilihan == 2:
    print("Welcome Donut Ceria")
    print("\nPilihan donut:")
    for idx, donut in enumerate(list_menu, start=1):
        print(f"{idx}. {donut['nama']} - Rp {donut['harga']}")

    pilihan = int(input("Masukkan nomor pilihan: "))

    if 1 <= pilihan <= len(list_menu):
        donut_terpilih = list_menu[pilihan - 1]
        jumlah_pcs = float(input(f"Berapa pcs {donut_terpilih['nama']} yang ingin Anda beli? "))
        total_harga = jumlah_pcs * donut_terpilih['harga']
        print(f"Pilihan {jumlah_pcs} pcs {donut_terpilih['nama']}.")
        print(f"Total yang harus Anda bayar adalah Rp.{total_harga:.2f}")
        print("ENJOY YOUR DONUT")
    else:
        print("Pilihan tidak valid.")
else:
    print("Pilihan tidak valid.")
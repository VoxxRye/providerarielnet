daftar_paket = {
    1: {
        "nama": "Paket Warrior",
        "deskripsi": "4GB kuota internet, 20 menit telepon",
        "harga": 25000
    },
    2: {
        "nama": "Paket Epic",
        "deskripsi": "8GB kuota internet, 40 menit telepon",
        "harga": 45000
    },
    3: {
        "nama": "Paket Immortal",
        "deskripsi": "16GB kuota internet, 80 menit telepon",
        "harga": 80000
    }
}

# Program untuk menampikan daftar paket internet menggunakan prosedur
def tampilkan_daftar_paket():
    print("Daftar Paket Internet:")
    for nomor, paket in daftar_paket.items():
        print(f"{nomor}. {paket['nama']} - {paket['deskripsi']} - Harga: Rp{paket['harga']}")

# Program untuk memilih paket internet menggunakan fungsi
def pilih_paket():
    nomor_pilihan = int(input("Masukkan nomor paket internet yang ingin Anda beli: "))
    if nomor_pilihan in daftar_paket:
        return daftar_paket[nomor_pilihan]
    else:
        print("Nomor paket yang dimasukkan tidak valid.")
        return None

# Program utama menggunakan prosedur
def main():
    while True:
        print("\n==========arielnet==========")
        print("Silahkan pilih menu di bawah")
        print("[1] Tampilkan daftar paket internet")
        print("[2] Pilih paket internet")
        print("[3] Keluar")

        pilihan = int(input("Masukkan pilihan Anda: "))

        if pilihan == 1:
            tampilkan_daftar_paket()
        elif pilihan == 2:
            paket_terpilih = pilih_paket()
            if paket_terpilih:
                print(f"Anda memilih {paket_terpilih['nama']}. Terima kasih telah membeli paket ini!")
        elif pilihan == 3:
            print("Terima kasih telah setia menggunakan arielnet.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()
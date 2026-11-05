print("<================ Warkop Jalanan ================>")

total = 0
nama = input("Masukkan Nama: ")
print("\nhalo selamat datang",nama)

rincian = ""

while True:
    print("\n<=====MENU MAKANAN=====>")
    print("1. Ifumie          - Rp16.000")
    print("2. Mie Aceh        - Rp15.000")
    print("3. Ayam Pecak      - Rp22.000")
    print("4. Sate Kacang     - Rp25.000")
    print("5. Mie Bangladesh  - Rp13.000")
    print("0. Selesai Memilih")

    pilihan = int(input("Pilih menu (0-5): "))

    if pilihan == 0:
        break

    elif pilihan == 1:
        harga = 16000
        nama_menu = "Ifumie"

    elif pilihan == 2:
        harga = 15000
        nama_menu = "Mie Aceh"

    elif pilihan == 3:
        harga = 22000
        nama_menu = "Ayam Pecak"

    elif pilihan == 4:
        harga = 25000
        nama_menu = "Sate Kacang"

    elif pilihan == 5:
        harga = 13000
        nama_menu = "Mie Bangladesh"

    else:
        print("Pilihan tidak tersedia!")
        continue

    jumlah = int(input("Masukkan jumlah pesanan: "))

    if jumlah <= 0:
        print("Jumlah pesanan harus lebih dari 0!")
        continue

    subtotal = harga * jumlah
    total = total + subtotal

    print("\nPesanan berhasil!")
    print("Menu:", nama_menu)
    print("Harga:", harga)
    print("Jumlah:", jumlah)
    print("Subtotal:", subtotal)
    print("Total sementara:", total)

    rincian = rincian + "\nMenu     : " + nama_menu
    rincian = rincian + "\nHarga    : Rp " + str(harga)
    rincian = rincian + "\nJumlah   : " + str(jumlah)
    rincian = rincian + "\nSubtotal : Rp " + str(subtotal) + "\n"

if total > 200000:
    persen_diskon = 20
    diskon = total * 0.20
else:
    persen_diskon = 0
    diskon = 0
total_bayar = total - diskon

print("\n<================================>")
print("       STRUK PEMBAYARAN")
print("Nama Pelanggan:", nama)

print(rincian)

print("<==============================>")
print("Total Belanja :Rp",total)
print("Diskon        :", str(persen_diskon) + "%")
print("Diskon        :Rp",diskon)
print("<==================================>")
print("Total Bayar   :Rp",total_bayar)

print("<==================================>")
print("             TERIMA KASIH")
print("   selamat menikmati makanannya kak",nama)
print("       Silahkan Datang Kembali 🔄")
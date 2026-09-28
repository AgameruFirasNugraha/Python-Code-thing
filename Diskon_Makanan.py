print("=== PROGRAM KASIR KANTIN ===")

Harga = int(input("Masukkan harga makanan: "))
Jumlah = int(input("Masukkan jumlah porsi: "))

Total_Bayar = Harga * Jumlah

if Total_Bayar > 20000:
    potongan = Total_Bayar * 10/100
    Total_Bayar = Total_Bayar - potongan
    print("Selamat! Anda mendapatkan diskon 10%")
else:
    print("Maaf, belum mencapai batas minimal diskon")

print(f"Total yang harus dibayar: Rp{int(Total_Bayar)}")
Daftar_Barang = []
print("=== PROGRAM PENCATAT BARANG ===")
Jumlah = int(input("Berapa barang yang ingin kamu catat? "))

for i in range(Jumlah):
    Nama_Barang = input(f"Masukkan nama barang ke-{i + 1}: ")
    Daftar_Barang.append(Nama_Barang)

print("\nHASIL CATATAN BARANG:")
for Barang in Daftar_Barang:
    if len(Barang) > 5:
        print(f"- {Barang} (Barang dengan jumlah huruf lebih dari 5)")
    else:
        print(f"- {Barang} (Barang dengan jumlah huruf kurang dari 5)")

print(f"Total: {len(Daftar_Barang)} Barang.")

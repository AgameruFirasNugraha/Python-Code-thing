Nama = input("Masukkan nama mahasiswa: ")
Nilai = int(input("Masukkan nilainya: "))

if(Nilai >= 90):
    print(f"Grade {Nama} adalah A")
elif(Nilai >= 80):
    print(f"Grade {Nama} adalah B")
elif(Nilai >= 70):
    print(f"Grade {Nama} adalah C")
elif(Nilai >= 60):
    print(f"Grade {Nama} adalah D-")
elif(Nilai < 60):
    print(f"Grade {Nama} adalah E")

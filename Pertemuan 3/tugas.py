def hitung_gaji():
    print("Program Python Menghitung Gaji Karyawan")
    print("=======================================")

    nama = input("Nama Karyawan : ")
    golongan = input("Golongan : ").upper()
    jam_kerja = int(input("Jumlah jam kerja per minggu : "))

    if golongan == "A":
        gaji_per_jam = 5000
    elif golongan == "B":
        gaji_per_jam = 7000
    elif golongan == "C":
        gaji_per_jam = 8000
    elif golongan == "D":
        gaji_per_jam = 10000
    else :
        print("Golongan tidak terdaftar")
        return

    jam_normal = 48
    if jam_kerja > jam_normal:
        gaji_lembur = (jam_kerja - 48) * 4000
    else :
        gaji_lembur = 0
    
    total_gaji = (gaji_per_jam * jam_kerja) + gaji_lembur

    print("\n ##Program Python Menghitung Gaji Karyawan##")
    print("==============================================")
    print("Nama : ", nama)
    print("Golongan : ", golongan)
    print("Jumlah jam kerja : ", jam_kerja)
    print("Menerima gaji sebesar : Rp", total_gaji, "per minggu")

hitung_gaji()
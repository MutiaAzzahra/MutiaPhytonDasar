while True:
    nama_siswa = input("Masukkan nama siswa: ")
    nilai = int(input("Masukkan nilai siswa: "))

    if nilai >= 70:
        print("Selamat,", nama_siswa, "lulus!")
    else:
        print("Maaf,", nama_siswa, "tidak lulus.")

    ulang = input("Ulangi input? (ya/tidak): ")
    if ulang.lower() != "ya":
        break
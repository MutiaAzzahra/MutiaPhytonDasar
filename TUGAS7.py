# Input Nama dan Gaji Pokok
nama = input("Masukkan Nama: ")
gaji_pokok = float(input("Masukkan Gaji Pokok: "))

# Menghitung Tunjangan
tunjangan = 0.2 * gaji_pokok

# Menghitung Pajak
pajak = 0.15 * (gaji_pokok + tunjangan)

# Menghitung Gaji Bersih
gaji_bersih = gaji_pokok + tunjangan - pajak

# Output Nama, Gaji Pokok, dan Gaji Bersih
print("Nama:", nama)
print("Gaji Pokok:", gaji_pokok)
print("Gaji Bersih:", gaji_bersih)
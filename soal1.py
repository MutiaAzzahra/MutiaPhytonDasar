# Menghitung luas persegi panjang
def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

# Menghitung luas segitiga
def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

# Menghitung luas trapesium
def luas_trapesium(panjang_atas, panjang_bawah, tinggi):
    return 0.5 * (panjang_atas + panjang_bawah) * tinggi

# Menghitung luas jajargenjang
def luas_jajargenjang(alas, tinggi):
    return alas * tinggi

# Menghitung luas belah ketupat
def luas_belah_ketupat(diagonal1, diagonal2):
    return 0.5 * diagonal1 * diagonal2

# Input nilai-nilai yang diperlukan
panjang_persegi_panjang = float(input("Masukkan panjang persegi panjang: "))
lebar_persegi_panjang = float(input("Masukkan lebar persegi panjang: "))

alas_segitiga = float(input("Masukkan alas segitiga: "))
tinggi_segitiga = float(input("Masukkan tinggi segitiga: "))

panjang_atas_trapesium = float(input("Masukkan panjang atas trapesium: "))
panjang_bawah_trapesium = float(input("Masukkan panjang bawah trapesium: "))
tinggi_trapesium = float(input("Masukkan tinggi trapesium: "))

alas_jajargenjang = float(input("Masukkan alas jajargenjang: "))
tinggi_jajargenjang = float(input("Masukkan tinggi jajargenjang: "))

diagonal1_belah_ketupat = float(input("Masukkan diagonal 1 belah ketupat: "))
diagonal2_belah_ketupat = float(input("Masukkan diagonal 2 belah ketupat: "))

# Menghitung dan mencetak luas masing-masing bangun datar
print("Luas Persegi Panjang: ", luas_persegi_panjang(panjang_persegi_panjang, lebar_persegi_panjang))
print("Luas Segitiga: ", luas_segitiga(alas_segitiga, tinggi_segitiga))
print("Luas Trapesium: ", luas_trapesium(panjang_atas_trapesium, panjang_bawah_trapesium, tinggi_trapesium))
print("Luas Jajargenjang: ", luas_jajargenjang(alas_jajargenjang, tinggi_jajargenjang))
print("Luas Belah Ketupat: ", luas_belah_ketupat(diagonal1_belah_ketupat, diagonal2_belah_ketupat))
print("Mulai")

while True:
    umur = int(input("Masukkan Umur: "))

    if umur <= 10:
        print("Status: Anak-anak")
    elif umur <= 18:
        print("Status: Remaja")
    elif umur <= 35:
        print("Status: Dewasa")
    elif umur <= 65:
        print("Status: Parubaya")
    else:
        print("Status: Tua")

    selesai = input("Selesai? (ya/tidak): ")
    if selesai.lower() == "ya":
        break

print("Selesai")
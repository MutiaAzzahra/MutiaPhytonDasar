n = 10 # Jumlah baris

for i in range(1, n + 1):
    #Membuat spasi sebelum bintang 
    for j in range(n - i):
        print(" ", end="")

    #Membuat bintang
    for k in range (2 * i - 1):
        print("*", end="")

    #Pindah ke baris berikutnya
    print()
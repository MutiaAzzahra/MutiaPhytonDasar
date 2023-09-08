#input jumlah baris
jumlah_baris = 10

#Loop untk menghasilkan segitiga
for i in range(1,jumlah_baris + 1):
    for j in range(i):
        print("*", end="")
    print()
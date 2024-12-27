n = int(input("Masukkan jumlah baris: "))

# Mencetak pola segitiga
for i in range(n):
    print(" " * (n-i-1) + "*" * (2*i+1))
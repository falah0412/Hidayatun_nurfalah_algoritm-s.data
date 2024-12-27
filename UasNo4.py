def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: Pembagian dengan nol!"
    return a / b

# Menu operasi
print("Pilih Operasi:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

# Input dari pengguna
pilihan = input("Masukkan pilihan (1/2/3/4): ")
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# Proses perhitungan
if pilihan == '1':
    hasil = tambah(angka1, angka2)
    operator = '+'
elif pilihan == '2':
    hasil = kurang(angka1, angka2)
    operator = '-'
elif pilihan == '3':
    hasil = kali(angka1, angka2)
    operator = '*'
elif pilihan == '4':
    hasil = bagi(angka1, angka2)
    operator = '/'
else:
    hasil = "Pilihan tidak valid!"
    operator = ''

# Tampilkan hasil
if operator:
    print(f"{angka1} {operator} {angka2} = {hasil}")
else:
    print(hasil)
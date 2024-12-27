# Input usia dari pengguna
usia = int(input("Masukkan usia Anda: "))

# Menentukan kategori usia
if usia < 0:
    kategori = "Usia tidak valid"
elif usia <= 5:
    kategori = "Balita"
elif usia <= 12:
    kategori = "Anak-anak"
elif usia <= 17:
    kategori = "Remaja"
elif usia <= 59:
    kategori = "Dewasa"
else:
    kategori = "Lansia"

# Menampilkan hasil
print(f"Usia {usia} tahun adalah: {kategori}")
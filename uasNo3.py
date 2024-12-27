def hitung_gaji(tarif_per_jam, jam_kerja_per_hari, hari_kerja):
    total_gaji = 0
    
    for hari in range(hari_kerja):
        # Menghitung gaji harian
        if jam_kerja_per_hari <= 8:
            gaji_harian = tarif_per_jam * jam_kerja_per_hari
        else:
            gaji_normal = tarif_per_jam * 8
            gaji_lembur = (jam_kerja_per_hari - 8) * (tarif_per_jam * 1.5)
            gaji_harian = gaji_normal + gaji_lembur
        
        total_gaji += gaji_harian
    
    return total_gaji

# Input dari pengguna
tarif = float(input("Masukkan tarif per jam: Rp "))
jam_kerja = float(input("Masukkan jam kerja per hari: "))
hari = int(input("Masukkan jumlah hari kerja: "))

# Hitung dan tampilkan total gaji
gaji_bulanan = hitung_gaji(tarif, jam_kerja, hari)
print(f"\nTotal gaji bulanan: Rp {gaji_bulanan:,.2f}")
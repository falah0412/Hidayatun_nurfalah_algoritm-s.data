# Program untuk menginput dan menampilkan data diri

def input_data():
    print("\n=== Biodata ===\n")
    
    # Meminta input dari pengguna
    nama = input("Masukkan nama Anda: ")
    usia = input("Masukkan usia Anda: ")
    alamat = input("Masukkan alamat Anda: ")
    hobi = input("Masukkan hobi Anda: ")
    
    # Menampilkan informasi dengan format yang rapi
    print("\n=== informasi biodata ===")
    print("=" * 30)
    print(f"Nama   : {nama}")
    print(f"Usia   : {usia} tahun")
    print(f"Alamat : {alamat}")
    print(f"Hobi   : {hobi}")
    print("=" * 30)

# Menjalankan program
if __name__ == "__main__":
    input_data()
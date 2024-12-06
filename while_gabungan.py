listKota = [
    'jakarta','surabaya','depok','bekasi','solo','jogjakarta','semarang','makassar'
    ]
kotaYangDicari = input('masukan nama kota yang anda cari: ')

i = 0
while i < len(listKota):
    if listKota[i].lower() == kotaYangDicari.lower():
        print('berhasil ditemukan', i)
        break

    print('bukan ', listKota[i])
    i += 1

else:
    print('maaf, kota yang anda cari tidak ditemukan')
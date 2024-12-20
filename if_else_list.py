list_buah = ['jambu','mangga','apel','melon']
list_buah_dicari = input ('masukan nama buah dalam huruf kecil: ')

if (list_buah_dicari in list_buah):
    print('buah ditemukan dalam list')
    
else:
    print('buah tidak ditemukan')
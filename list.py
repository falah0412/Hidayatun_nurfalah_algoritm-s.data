#kumpulan string
list_buah = ['duren', 'jambu','pisang','apel']
print('list_buah:',list_buah)
#menampilkan data sesuai array
list_buah = ['duren', 'jambu','pisang','apel']
print(list_buah[-1])
print(list_buah[-2])
print(list_buah[-3])
print(list_buah[-4])
#jika digunakan untuk memaanggil 2 list (slucing list)
print(list_buah[1:3])
print(list_buah[0:2])
print(list_buah[0:3])
#ubah data
list_buah[0] = ('naga')
list_buah[1] = ('kelapa')
list_buah[2] = ('jeruk')
print(list_buah)
#tambah data di belakang list
list_buah.append('srikaya')
print(list_buah)
#tambah data di depan
list_buah.insert(0,'mangga')
list_buah.insert(1,'salak')
print(list_buah)
#menghapus data di belakang
list_buah.pop()
'srikaya'
print(list_buah)
#menghapus data sesuai nama (remove)
list_buah.remove('kelapa')
print(list_buah)
#menghapus data sesuai array (del)
del list_buah[3]
print(list_buah)

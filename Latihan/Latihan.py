daftar_kontak = {}

#ari
daftar_kontak['Ari'] = '081267888'
daftar_kontak['Dina'] = '087677776'
print("# Nama   | Nomor telepon")
print("# ========================")
for i in daftar_kontak.items():
    print("# {0:6} |".format(i[0]),i[1])
print('+--------------------------+\n')

#dina
daftar_kontak['Dina'] = '087677776'

#riko
daftar_kontak['Riko'] = '087654544'
daftar_kontak['Ari'] = '081267888'
print("# Nama   | Nomor telepon")
print("# ========================")
for i in daftar_kontak.items():
    print("# {0:6} |".format(i[0]),i[1])
print('+--------------------------+\n')

#ubah kontak dina
daftar_kontak['Dina'] = '088999776'
daftar_kontak['Ari'] = '081267888'
print("# Nama   | Nomor telepon")
print("# ========================")
for i in daftar_kontak.items():
    print("# {0:6} |".format(i[0]),i[1])
print('+--------------------------+\n')

#tampilkan semua nama
for nama in daftar_kontak.keys():
    print(nama)
print('+--------------------------+\n')

#tampilkan semua nomor
for nomor in daftar_kontak.values():
    print(nomor)
print('+--------------------------+\n')

#tampilkan daftar nama dan nomor
print("# Nama   | Nomor telepon")
print("# ========================")
for i in daftar_kontak.items():
    print("# {0:6} |".format(i[0]),i[1])
print('+--------------------------+\n')

#hapus kontak dina
del daftar_kontak['Dina']
daftar_kontak['Ari'] = '081267888'
print("# Nama   | Nomor telepon")
print("# ========================")
for i in daftar_kontak.items():
    print("# {0:6} |".format(i[0]),i[1])
print('+--------------------------+\n')

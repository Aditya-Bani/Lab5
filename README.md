# DAFTAR TUGAS

<table border="2" cellpading="10">
  <tr>
    <td><b>Pertemuan 4</b></td>
    <td>Latihan VCS</td>
    <td><a href="https://github.com/Aditya-Bani/LatihanVCS">Klik disini</td>
  </tr>
  <tr>
    <td><b>Pertemuan 5</b></td>
    <td>Program Biodata</td>
    <td><a href="https://github.com/Aditya-Bani/Pertemuan-5">Klik disini</td>
  </tr>
  <tr>
    <td><b>Pertemuan 6</b></td>
    <td>Lab1 dan 2</td>
    <td><a href="https://github.com/Aditya-Bani/ProjectPraktikum">Klik disini</td>
  </tr>
  <tr>
    <td><b>Pertemuan 7</b></td>
    <td>Lab3</td>
    <td><a href="https://github.com/Aditya-Bani/Lab3">Klik disini</td>
  </tr>
  <tr>
    <td></td>
    <td>Labspy02</td>
    <td><a href="https://github.com/Aditya-Bani/Labspy02">Klik disini</td>
  </tr>
  <tr>
    <td></td>
    <td>Labpy03</td>
    <td><a href="https://github.com/Aditya-Bani/Labspy03">Klik disini</td>
  </tr>
  <tr>
    <td><b>Pertemuan 9</b></td>
    <td>Lab 4</td>
    <td><a href="https://github.com/Aditya-Bani/Lab4">Klik disini</td>
  </tr>
  <tr>
    <td></td>
    <td>Lab 5</td>
    <td><a href="https://github.com/Aditya-Bani/Lab5">Klik disini</td>
  </tr>
</table>

# Lab 5
## Latihan 1
![SoalLatihan](Latihan/Gambar/SoalLatihan.jpeg)

* **Untuk Codenya bisa dilihat dibawah ini :**

![Gbr1](Latihan/Gambar/gbr1.PNG)
![gbr2](Latihan/Gambar/gbr2.PNG)


## Hasil Output :

#### Daftar Kontak

*  Output menampilkan daftar kontak

![DaftarKontak](Latihan/Gambar/DaftarKontak.PNG)

#### Menambah Kontak Baru Riko
* Output menambahkan kontak baru Riko

![KontakBaru](Latihan/Gambar/KontakBaru.PNG)

#### Ubah Kontak Dina
* Output mengubah kontak dina dengan nomor baru 088999776

![UbahKontakDina](Latihan/Gambar/UbahKontakDina.PNG)

#### Tampilkan semua Nama
* Output menampilkan semua Nama

![TampilkanNama](Latihan/Gambar/SemuaNama.PNG)

#### Tampilkan semua nomor
* Output menampilkan semua nomor

![SemuaNomor](Latihan/Gambar/SemuaNomor.PNG)

#### Tampilkan daftar nama dan nomor
* Output menampilkan semua nama dan nomornya

![TampilanSemuaNamaDanNomor](Latihan/Gambar/TampilanNamaDanNomor.PNG)

#### Hapus Kontak Dina
* Output menghapus kontak Dina

![HapusKontakDina](Latihan/Gambar/HapusKontakDina.PNG)


# Tugas Praktikum 5

![soal-praktikum-5](TugasPraktikum/Gambar/Soal.png)

**Code:**

![gbr1](TugasPraktikum/Gambar/gbr1.PNG)
![gbr2](TugasPraktikum/Gambar/gbr2.PNG)
![gbr3](TugasPraktikum/Gambar/gbr3.PNG)
![gbr4](TugasPraktikum/Gambar/gbr4.PNG)
![gbr4](TugasPraktikum/Gambar/gbr5.PNG)

**Penjelasan:**

**Header**
* ``data={}`` list dengan format dictionary
* Gunakanlah perulangan ``While`` untuk menampilkan data sebanyak banyaknya
* ``menu = input("(T)ambah, (U)bah, (H)apus, (L)ihat, (C)ari, (K)eluar: ")`` kita tambahkan input Tambah, Ubah, Hapus, Lihat, Cari, Keluar dalam variabel menu
* ``else: print("Upss ada yang salah, silahkan cek kembali.")`` jika kita salah dalam input maka akan tercetak 'Upss ada yang salah, silahkan cek kembali.'
* masukan nama, nim, nilai_tugas, nilai_uts, nilai_uas, dan nilai_akhir yang nanti akan di masukkan kedalam ``data={}``
* Nilai akhir didapat dari = (nilai_tugas)*30/100 + (nilai_uts)*35/100 + (nilai_uas)*35/100

**Keluar**
* ``if menu.lower() == 'k':`` Ambil data 'k' dari ``menu``
* lalu ``break`` untuk menghentikan seluruh proses

**Lihat data**
* ``elif menu.lower() == 'l':`` Kita menggunakan kondisi percabangan if, ambil data dari ``menu`` lalu kita akan mengubah perintah 'l' yang kita input menjadi huruf kecil dengan fungsi ``lower()``
* lalu cetak ``print()``

**Tambah data**
* ``elif menu.lower() == 't':`` Ambil data 't' dari ``menu``
* ``nama = input("Masukan nama: ")`` lalu tambahkan input nama, nim, nilai tugas, uts, uas
* ``nilai_akhir = (nilai_tugas)*30/100 + (nilai_uts)*35/100 + (nilai_uas)*35/100 `` untuk nilai akhir diambil dari perhitungan 3 komponen nilai (nilai_tugas: 30%, nilai_uts: 35%, nilai_uas: 35%)
* ``data[nama] = [nama, nim, nilai_tugas, nilai_uts, nilai_uas, nilai_akhir]`` kita akan masukkan data yang tadi kita input ke dalam `data[nama]'
* lalu cetak ``print()``

**Ubah data**
* ``elif menu.lower() == 'u':`` Ambil data 'u' dari ``menu``
* ``nama = input("Masukan nama untuk mengubah data: ")`` kita akan menginput data yang nanti akan di ubah
* ``if nama in data.keys(): print("Mau mengubah apa?")`` jika 'nama' dari di dalam 'data' maka akan mengembalikan daftar menggunakan fungsi 'keys()' lalu di cetak lah 'print()'
* ``sub_data = input("(Semua), (Nama), (NIM), (Tugas), (UTS), (UAS) : ")`` memmbuat menu ubah di dalam ``sub_data``
* ``if sub_data.lower() == "semua":`` ambil kata kunci 'semua' di dalam ``sub_data`` jika 'semua' maka input ``data[nama][1] = input("Ubah NIM:") data[nama][2] = int(input("Ubah Nilai Tugas: ")) data[nama][3] = int(input("Ubah Nilai UTS: ")) data[nama][4] = int(input("Ubah Nilai UAS: "))``
* ``data[nama][5] = data[nama][2] *30/100 + data[nama][3]*35/100 + data[nama][4] *35/100 `` kita dapatkan nilai akhir dengan diambil dari perhitungan 3 komponen nilai (tugas: 30%, uts: 35%, uas: 35%),

*ket: [5] = nilai_akhir, dimana [0] = nama*

* lalu cetak ``print("\nBerhasil ubah data!")``
* Jika kita ingin mengubah data tertentu maka ``elif sub_data.lower() == "nim": data[nama][1] = input("NIM:")`` dan berlaku juga untuk nilai tugas, UTS dan UAS
* lalu cetak ``print("\nBerhasil ubah data!")``
* ``else: print("'{}' tidak ditemukan.".format(nama))`` jika kita salah dalam memasukkan nama untuk mengubah data maka akan muncul 'nama tidak di temukan'

**Cari data**
* ``elif menu.lower() == 'c':`` Ambil data 'c' dari ``menu``
* ``nama = input("Masukan nama untuk mencari data: ")`` kita akan menginput data yang nanti akan di cari
* ``if nama in data.keys():`` kita mengambil list 'nama' di dalam 'data' menggunakan pengkondisian
* maka cetak ``print("Nama: {0}\nNIM : {1}\nNilai Tugas: {2}\nUTS: {3}\nUAS: {4}\nNilai akhir: {5}"`` untuk menampilkan data yang tersedia
* ``else: print("'{}' tidak ditemukan.".format(nama))`` jika data yang kita input salah/tidak ditemukan maka akan tercetak 'nama tidak di temukan'

**Hapudata**
* ``elif menu.lower() == 'h':`` Ambil data 'h' dari ``menu``
* ``nama = input("Masukan nama untuk menghapus data : ")`` kita akan menginput data yang nanti akan di hapus
* ``if nama in data.keys():`` kita mengambil list 'nama' di dalam 'data' menggunakan pengkondisian
* ``del data[nama]`` hapus semua 'nama'  yang ada di dalam 'data'
* jika sudah maka cetak ``print("sub_data '{}' berhasil dihapus.".format(nama))``
* ``else: print("'{}' tidak ditemukan.".format(nama))`` jika data yang kita input salah/tidak ditemukan maka akan tercetak 'nama tidak di temukan'



**Output:**

#### Lihat Data

![LihatData](TugasPraktikum/Gambar/LihatData.PNG)

#### Tambah Data

![TambahData](TugasPraktikum/Gambar/TambahData.PNG)

#### Ubah data
![UbahData](TugasPraktikum/Gambar/UbahData.PNG)

#### Cari data

![CariData](TugasPraktikum/Gambar/CariData.PNG)

#### Hapus data

![HapusData](TugasPraktikum/Gambar/HapusData.PNG)


**Flowchart:**


![Flowchart](TugasPraktikum/Gambar/flowchart.png)

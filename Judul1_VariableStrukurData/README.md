Judul: Program daftar belanja

Program ini merupakan management daftar belanja yang menyediakan enam fitur utama yang dapat diakses melalui menu, yaitu menentukan jumlah item, memasukan item, menampilkan item, menampilkan daftar belanja, menghapus item, mencari item, dan keluar dari program. Seluruh alur program dikendalikan oleh sebuah loop utama while running yang terus berjalan hingga pengguna memilih opsi keluar, try-except untuk mencegah crash akibat input yang tidak sesuai.

Struktur data yang diterapkan dalam program ini adalah array berbasis list python 1 dimensi. Pendekatan ini mencerminkan konsep array dengan ukuran tetap. Operasi yang dilakukan meliputi insert yaitu mengisi slot dengan nama item, delete yaitu menghapus item yang dihapus menjadi string kosong, tranversal yaitu peluang for untuk menampilkan semua item, dan linear search yaitu pencarian item satu persatu dari indeks 0.

<img width="1735" height="881" alt="Screenshot 2026-04-28 231116" src="https://github.com/user-attachments/assets/7c281960-9d6d-40b6-adf1-0a2e7c97b3ad" />
<img width="1727" height="888" alt="Screenshot 2026-04-28 231144" src="https://github.com/user-attachments/assets/0031f271-c069-443e-81db-681c87a8e2e5" />
<img width="1726" height="888" alt="Screenshot 2026-04-28 231401" src="https://github.com/user-attachments/assets/bf7d5515-da4c-4758-9f71-32b542be8007" />
<img width="1727" height="195" alt="Screenshot 2026-04-28 231429" src="https://github.com/user-attachments/assets/d9b4601f-5be3-4a3b-bd57-cacf29e9a35b" />

Penjelasan kode perbaris:
1.	Mendefinisikan fungsi bernama menu
2.	Mencetak judul "Daftar Belanja" dengan baris baru di depan
3.	Mencetak opsi menu nomor 1
4.	Mencetak opsi menu nomor 2
5.	Mencetak opsi menu nomor 3
6.	Mencetak opsi menu nomor 4
7.	Mencetak opsi menu nomor 5
8.	Mencetak opsi menu nomor 6 atau merupakan opsi keluar
9.  –
10. –
11.	Mendefinisikan fungsi utama main
12.	Menginisialisasi list kosong untuk menyimpan item belanja
13.	Menginisialisasi variabel n (jumlah item) dengan nilai 0
14.	Flag boolean untuk mengontrol loop utama program
15.	-
16.	Loop utama program, berjalan selama running bernilai True
17.	Memanggil fungsi menu() untuk menampilkan pilihan menu
18.	Memulai blok percobaan untuk menangkap error input
19.	Membaca input dari user dan mengubahnya ke integer, disimpan di choice
20.	Menangkap error jika input bukan angka
21.	Mencetak pesan kesalahan jika input bukan angka
22.	Kembali ke awal loop tanpa memproses pilihan lebih lanjut
23.	–
24.	Mengecek apakah pilihan user adalah 1
25.	Meminta user memasukkan jumlah item yang diinginkan
26.	Membuat list berisi n string kosong sebagai slot belanja
27.	Konfirmasi jumlah slot yang telah disiapkan
28.	–
29.	Mengecek apakah pilihan user adalah 2
30. Mengecek apakah jumlah item belum dimasukkan
31.	Mencetak perintah untuk memilih opsi 1 terlebih dahulu
32.	Jika jumlah item sudah diisi masuk ke blok else
33.	Mencetak instruksi memasukkan sebanyak n item
34.	Perulangan untuk setiap slot item dari 0 sampai n-1
35.	Loop tak terbatas untuk validasi input item
36.	Memulai blok percobaan untuk menangkap error input item
37.	Membaca nama item ke-i+1 dan menghapus spasi di awal dan akhir
38.	Mengecek apakah input item kosong
39.	Mencetak pesan error jika item dibiarkan kosong
40.	Jika item tidak kosong masuk ke blok else
41.	Menyimpan item ke dalam list belanja pada posisi ke-i
42.	Keluar dari while loop setelah item berhasil disimpan
43.	Menangkap error jika input tidak valid
44.	Mencetak pesan error input tidak valid
45.	Menampilkan seluruh isi list belanja setelah semua item diisi
46.	–
47.	Mengecek apakah pilihan user adalah 3
48.	Mengecek apakah jumlah item belum dimasukkan
49.	Mencetak perintah untuk memilih opsi 1 terlebih dahulu
50.	Mengecek apakah semua slot belanja masih kosong menggunakan fungsi all
51.	Mencetak info bahwa daftar belum diisi sama sekali
52.	Jika ada item yang sudah terisi masuk ke blok else
53.	Mencetak header daftar belanja
54.	Perulangan untuk menampilkan setiap item dari indeks 0 hingga n-1
55.	Menentukan teks yang ditampilkan isi item atau teks kosong jika slot masih kosong
56.	Mencetak nomor urut dan status setiap item belanja
57.	–
58.	Mengecek apakah pilihan user adalah 4 menu hapus item
59.	Mengecek apakah jumlah item belum ditentukan
60.	Mencetak pesan untuk memilih opsi 1 terlebih dahulu
61.	Mengecek apakah semua slot item masih kosong
62.	Mencetak pesan bahwa tidak ada item yang bisa dihapus
63.	Jika ada item yang bisa dihapus masuk ke blok else
64.	Mencetak header menu hapus item
65.	Perulangan untuk menampilkan daftar item sebelum dipilih
66.	Menentukan teks yang ditampilkan isi item atau kosong
67.	Mencetak nomor dan status setiap item
68.	Loop tak terbatas untuk memvalidasi input nomor item yang akan dihapus
69.	Memulai blok percobaan untuk menangkap error input
70.	Membaca nomor item yang ingin dihapus dari user dan mengubahnya ke integer
71.	Mengecek apakah nomor yang dimasukkan valid yaitu antara 1 dan n
72.	Mengecek apakah item pada slot yang dipilih sudah kosong atau sudah pernah dihapus
73.	Memberitahu user bahwa item tersebut sudah kosong
74.	Jika item masih ada isinya masuk ke blok else
75.	Menampilkan konfirmasi nama item yang berhasil dihapus
76.	Mengosongkan slot item pada posisi idx-1 sebagai tanda item telah dihapus
77.	Keluar dari while loop setelah proses hapus selesai
78.	Jika nomor yang dimasukkan di luar rentang valid masuk ke blok else
79.	Mencetak pesan error bahwa nomor berada di luar rentang yang diperbolehkan
80.	Menangkap error jika input yang dimasukkan bukan angka
81.	Mencetak pesan error input tidak valid
82.	–
83.	Mengecek apakah pilihan user adalah 5 menu cari item
84.	Mengecek apakah jumlah item belum dimasukkan
85.	Mencetak pesan untuk memilih opsi 1 terlebih dahulu
86.	Mengecek apakah semua slot item masih kosong
87.	Mencetak pesan bahwa tidak ada item yang bisa dicari
88.	Jika ada item dalam daftar masuk ke blok else
89.	Membaca input kata kunci pencarian menghapus spasi di awal dan akhir dan mengubah ke huruf kecil
90.	Menginisialisasi flag ditemukan dengan nilai False sebagai penanda awal pencarian
91.	Perulangan melalui setiap item dalam daftar belanja dari indeks 0 hingga n-1
92.	Membandingkan item yang diubah ke huruf kecil dengan kata kunci pencarian
93.	Mencetak pesan bahwa item berhasil ditemukan
94.	Menampilkan nama asli item yang ditemukan
95.	Menampilkan posisi indeks dan nomor urut item dalam list
96.	Menampilkan alamat memori dari string item menggunakan fungsi id
97.	Mengubah flag ditemukan menjadi True setelah item berhasil ditemukan
98.	Menghentikan perulangan pencarian setelah item pertama ditemukan
99.	Mengecek apakah setelah loop selesai item tidak ditemukan sama sekali
100. Mencetak pesan bahwa item yang dicari tidak ada dalam daftar
101. –
102. Mengecek apakah pilihan user adalah 6 menu keluar
103. Mengubah flag running menjadi False untuk menghentikan loop utama program
104. Mencetak pesan perpisahan sebelum program selesai
105. –
106. Jika pilihan user tidak sesuai angka 1 hingga 6 masuk ke blok else
107. Mencetak pesan bahwa pilihan yang dimasukkan tidak dikenali
108. –
109. –
110. Mengecek apakah file dijalankan langsung bukan diimpor sebagai modul
111. Memanggil fungsi main untuk memulai jalannya program

<img width="1830" height="787" alt="Screenshot 2026-04-29 142847" src="https://github.com/user-attachments/assets/4bfc8c10-c32d-4bbb-8fbc-ca144a90162c" />
<img width="1810" height="795" alt="Screenshot 2026-04-29 142908" src="https://github.com/user-attachments/assets/72ec3867-5008-4511-a322-cb226aa9447f" />
<img width="1815" height="252" alt="Screenshot 2026-04-29 143115" src="https://github.com/user-attachments/assets/92fdea88-3b69-406d-9e64-9bcea5d6e182" />

Penjelasan output:
program dijalankan dan langsung menampilkan menu utama berisi 6 pilihan operasi. pada percobaan pertama, saya memilih opsi 1 untuk menentukan jumlah item belanjanya. Kemudian program meminta input jumlah item yang diinginkan dan saya memasukan angka 2, sehingga program menyiapkan dua slot kosong pada list belanja. Setelah itu menu utama kembali ditampilkan yang membuktikan bahwa loop utama while running berjalan dan program tidak berhenti setelah satu operasi.
Pada percobaan kedua, saya memilih opsi 2 untuk mengisi item belanja. program meminta input sebanyak dua kali sesuai jumlah slot yang telah ditentukan sebelumnya, saya memasukan ayam pada slot pertama dan sayur pada slot kedua. setelah kedua slot terisi, program menampilkan konfirmasi list secara keseluruhan yaitu ayam dan sayur yang membuktikan bahwa proses penyimpanan item kedalam array berjalan dengan benar.
Percobaan ketiga dengan memilih opsi 3 menampilkan seluruh isi daftar belanja secara terurut. program mencetak 1. ayam dan 2. sayur sesuai urutan indeks dalam list, berhasil menampilkan semua elemen yang tersimpan dalam array tanpa ada yang terlewat.
Percobaan ke empat dengan memilih opsi 4 menguji fitur penghapusan item. program terlebih dahulu menampilkan ulang daftar belanja serta nomornya, kemudian saya memilih nomor 2 untuk menghapus item sayur, lalu program marespon dengan konfirmasi item sayur berhasil dihapus dan mengosongkan slot tersebut dengan mengganti nilainya dengan sebuah string "kosong". operasi delete dalam program tidak benar benar menghapus slot dari array melaikan mengosongkan isinnya sehingga ukuran list tetap sama.
percobaan kelima dengan memilih opsi 5 yaitu menguji fitur pencarian, saya memasukan kata kunci ayam dan program menalusuri list satu persatu. item ayam ditemukan pda indeks pertama sehingga program menampilkan nama item, posisi, serta alamat memorinya. pencarian berhenti setelah item prtama ditemukan karena adanya perintah break.
Percobaan terakhir dengan memilih opsi 6 yaitu mengakhiri program. running diubah menjadi false sehingga loop utama berhenti dan program mencetak pesan "program selesai. selamat berbelanja" yang merupakan tanda bahwa seluruh program berakhir. percobaan ini membuktikan bahwa program berjalan tanpa error.

Link Youtube:
https://youtu.be/RyIWCqo3F6w?si=gimL8x5_KyCk1BVy

Judul program: Sistem pencatatan pembongkaran candi

Program ini dirancang untuk membantu arkeolog dalam proses pembongkaran batu candi secara lapisan. Setiaplapisan yang diangkat akan dicatat kedalam sistem, dan urutan pengembalian batu mengikuti urutan kebalikan dari pencatatannya. dimana batu yang paling akhir diambil harus menjadi batu pertama yang dipasang agar struktur candi tetap sama.

Struktur data yang digunakan adalah stack array dimana metode penyimpanan data yang bekrja dengan konsep LIFO (last in forst out) yaitu data yang terakhir masuk akan menjadi yang pertama keluar. Terdapat empat operasi yang tersedia, yaitu pencatatan lapisan baru, pengangkatan lapisan teratas, pengecekan lapisan paling atas tanpa mengubah data, serta menampilkan seluruh data tersimpan. Dilengkapi dengan pembatasan kapasitas dan pengecekan kondisi tumpukan agar tidak terjadi kesalahan saat tumpukan dalam kondisi penuh maupun kosong.

Source code:
<img width="1721" height="947" alt="Screenshot 2026-05-16 033902" src="https://github.com/user-attachments/assets/b835c16d-15a0-4d5b-8a4a-ba69ded40b45" />
<img width="1726" height="936" alt="Screenshot 2026-05-16 033936" src="https://github.com/user-attachments/assets/a1fbeb52-c03b-469e-99a9-f1692259246f" />
<img width="1728" height="497" alt="Screenshot 2026-05-16 033950" src="https://github.com/user-attachments/assets/c6dec430-c241-47c0-9fb0-0551ebf5c315" />

1.	Mendefinisikan class bernama StackArray sebagai cetak biru struktur data stack
2.	Method konstruktor yang otomatis dipanggil saat objek dibuat, dengan nilai default kapasitas 10
3.	Menyimpan nilai kapasitas maksimal stack ke dalam atribut MAX
4.	Membuat array berisi None sebanyak MAX slot sebagai wadah penyimpanan stack
5.	Menginisialisasi indeks puncak stack dengan -1, menandakan stack masih kosong
6.	-
7.	Mendefinisikan method untuk mengecek apakah stack kosong
8.	Mengembalikan True jika top_idx bernilai -1, artinya belum ada data yang tersimpan
9.	-
10.	Mendefinisikan method untuk mengecek apakah stack sudah penuh
11.	Mengembalikan True jika indeks puncak sudah mencapai slot terakhir array
12.	-
13.	Mendefinisikan method untuk menambahkan data baru ke puncak stack
14.	Mengecek apakah stack sudah penuh sebelum menambahkan data
15.	Menampilkan pesan peringatan jika stack sudah tidak bisa menampung data baru
16.	Menghentikan eksekusi method jika stack penuh
17.	Menaikkan indeks puncak sebesar satu untuk membuka slot baru
18.	Menyimpan nilai x ke dalam slot puncak yang baru dibuka
19.	Menampilkan konfirmasi bahwa data berhasil dicatat beserta posisinya
20.	-
21.	Mendefinisikan method untuk menghapus data di puncak stack
22.	Mengecek apakah stack kosong sebelum mencoba menghapus data
23.	Menampilkan pesan peringatan jika tidak ada data yang bisa dihapus
24.	Menghentikan eksekusi method jika stack kosong
25.	Menyimpan sementara nilai di puncak stack ke variabel item sebelum dihapus
26.	Menampilkan informasi data mana yang sedang dikeluarkan dari stack
27.	Menurunkan indeks puncak sebesar satu, efektif menghapus data teratas dari stack
28.	-
29.	Mendefinisikan method untuk melihat data puncak tanpa mengubah stack
30.	Mengecek apakah stack kosong sebelum mencoba membaca puncak
31.	Menampilkan pesan peringatan jika stack tidak memiliki data
32.	Menghentikan eksekusi method jika stack kosong
33.	Menampilkan nilai dan posisi data yang berada di puncak stack saat ini
34.	-
35.	Mendefinisikan method untuk menampilkan seluruh isi stack
36.	Mengecek apakah stack kosong sebelum menampilkan isi
37.	Menampilkan pesan peringatan jika tidak ada data untuk ditampilkan
38.	Menghentikan eksekusi method jika stack kosong
39.	Menampilkan judul sebelum daftar isi stack dicetak
40.	Melakukan perulangan dari indeks teratas hingga nol dengan urutan atas ke bawah
41.	Memberikan label teratas hanya pada elemen paling atas stack
42.	Mencetak nomor posisi, nama lapisan, dan penanda teratas untuk setiap elemen
43.	-
44.	Mendefinisikan fungsi utama sebagai titik masuk jalannya program
45.	Menampilkan judul program saat pertama kali dijalankan
46.	-
47.	Membuat objek stack baru dengan kapasitas default 10 lapisan
48.	Menginisialisasi variabel pilihan menu dengan nilai 0 agar loop langsung berjalan
49.	-
50.	Menjalankan loop terus-menerus selama pengguna belum memilih menu keluar
51.	Menampilkan jumlah lapisan yang sudah tercatat dari total kapasitas
52.	Menampilkan pilihan menu pertama untuk operasi push
53.	Menampilkan pilihan menu kedua untuk operasi pop
54.	Menampilkan pilihan menu ketiga untuk operasi peek
55.	Menampilkan pilihan menu keempat untuk operasi display
56.	Menampilkan pilihan menu kelima untuk keluar dari program
57.	-
58.	Memulai blok percobaan untuk menangani kemungkinan input yang tidak valid
59.	Membaca input pengguna dan mengubahnya menjadi bilangan bulat
60.	Menangkap kesalahan jika input tidak bisa dikonversi menjadi bilangan bulat
61.	Menampilkan pesan kesalahan jika pengguna memasukkan karakter selain angka
62.	Kembali ke awal loop tanpa memproses pilihan yang tidak valid
63.	-
64.	Memeriksa apakah pengguna memilih menu Catat Bongkar
65.	Membaca nama lapisan dari pengguna dan menghapus spasi di awal maupun akhir
66.	Memeriksa apakah nama yang dimasukkan kosong atau hanya spasi
67.	Menampilkan peringatan jika pengguna tidak memasukkan nama lapisan
68.	Blok yang dijalankan jika nama lapisan valid dan tidak kosong
69.	Memanggil method push untuk menyimpan nama lapisan ke dalam stack
70.	Memeriksa apakah pengguna memilih menu Restorasi
71.	Memanggil method pop untuk mengeluarkan lapisan teratas dari stack
72.	Memeriksa apakah pengguna memilih menu Lihat Teratas
73.	Memanggil method peek untuk menampilkan lapisan teratas tanpa mengubah stack
74.	Memeriksa apakah pengguna memilih menu Tampilkan Semua
75.	Memanggil method display untuk menampilkan seluruh isi stack
76.	Memeriksa apakah pengguna memilih menu Keluar
77.	Menampilkan pesan penutup sebelum program berhenti
78.	Blok yang dijalankan jika pilihan tidak ada dalam daftar menu
79.	Menampilkan pesan bahwa angka yang dimasukkan bukan pilihan yang tersedia
80.	-
81.	Memastikan fungsi main hanya dijalankan jika file ini dieksekusi langsung, bukan diimpor
82.	Memanggil fungsi main untuk memulai jalannya program

Output program:
<img width="1843" height="947" alt="Screenshot 2026-05-16 184229" src="https://github.com/user-attachments/assets/2712198e-1bc2-4c3e-b24d-1fea0b4f8263" />
<img width="1852" height="953" alt="Screenshot 2026-05-16 184245" src="https://github.com/user-attachments/assets/004eca19-fd84-4eb2-a6c1-2323c63d70a1" />
<img width="1857" height="947" alt="Screenshot 2026-05-16 184258" src="https://github.com/user-attachments/assets/54bb0268-581c-4049-8c00-23c1fac2f63d" />
<img width="1857" height="906" alt="Screenshot 2026-05-16 184308" src="https://github.com/user-attachments/assets/00d8abd0-9bd5-4e1a-9cdc-0c24805cd541" />
<img width="1850" height="411" alt="Screenshot 2026-05-16 184320" src="https://github.com/user-attachments/assets/82d84e3e-ace9-47b2-9a46-eea54032aa30" />

link youtube: https://youtu.be/1d5r2HviGW0

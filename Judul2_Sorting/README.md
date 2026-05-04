Judul: Pengurutan Jarak Tempuh Kendaraan dalam KM

Program ini berfungsi untuk mengurutkan data kendaraan berdasarkan jarak tempuh dari yang terkecil hingga yang terbesar. Pengguna diminta memasukan jumlah kendaraam terlebih dahulu, kemudian secara bergantian mengisi nama dan jarak tempuh setiap kendaraan. Program kemudian akan menampilkan data sebelum dan sesudah diurutkan, dilengkapi dengan validasi input agar program tidak berhenti ketika pengguna salah memasukan data.

Algoritma yang digunakan adalah Exchange Sort, yaitu algoritma pengurutan yang bekerja dengan cara membandingkan setiap pasang elemen lalu menukar posisinya jika urutannya belum benar. Memilih satu elemen sebagai acuan, kemudian membandingkan elemen acuan tersebut dengan semua elemen di sebelah kanannya satu per satu. Jika ditemukan elemen yang lebih kecil dari elemen acuan, maka kedua elemen tersebut langsung ditukar posisinya. Proses ini terus berulang hingga seluruh data tersusun dari jarak terkecil hingga terbesar. Strultur data yang digunakan adalah list dua dimensi di mana setiap elemen dalam list utama berupa sublist berisi dua data yaitu nama pemilik pada indeks 0 dan jarak tempuh pada indeks 1. 

Source Code:
<img width="1722" height="926" alt="Screenshot 2026-05-04 114340" src="https://github.com/user-attachments/assets/6b0b6849-984c-448a-acf9-d13f3d272aa8" />
<img width="1723" height="292" alt="Screenshot 2026-05-04 114400" src="https://github.com/user-attachments/assets/70126b21-4d21-4fd5-bc83-c38800073b85" />

1.	Mendefinisikan fungsi tukar yang menerima tiga parameter yaitu list kendaraan, indeks i, dan indeks j
2.	Menyimpan sementara nilai elemen pada posisi i ke dalam variabel temp sebelum nilainya ditimpa
3.	Mengisi posisi i dengan nilai yang ada di posisi j sehingga posisi i sekarang berisi data yang lama ada di posisi j
4.	Mengisi posisi j dengan nilai yang tersimpan di variabel temp sehingga pertukaran dua elemen berhasil dilakukan
5.	—
6.	Mendefinisikan fungsi exchange_sort yang menerima parameter list kendaraan dan jumlah elemen n untuk menjalankan algoritma pengurutan
7.	Perulangan luar berjalan dari indeks 0 hingga n-2 sebagai elemen acuan yang akan dibandingkan
8.	Perulangan dalam berjalan dari indeks i+1 hingga n-1 untuk membandingkan elemen acuan dengan elemen di sebelah kanannya
9.	Mengecek apakah jarak tempuh elemen ke-i lebih besar dari jarak tempuh elemen ke-j dengan mengakses indeks 1 dari setiap sublist
10.	Jika kondisi terpenuhi maka fungsi tukar dipanggil untuk menukar posisi kedua elemen tersebut
11.	—
12.	Mendefinisikan fungsi utama main sebagai pusat kendali jalannya program
13.	Memulai blok percobaan untuk menangkap error jika input jumlah kendaraan bukan angka
14.	Membaca input jumlah kendaraan dari pengguna dan mengubahnya menjadi integer lalu disimpan ke variabel n
15.	Menangkap error ValueError jika pengguna memasukkan karakter selain angka
16.	Mencetak pesan bahwa input tidak valid
17.	Menghentikan eksekusi fungsi main dan keluar dari program jika input tidak valid
18.	—
19.	Menginisialisasi list kosong bernama kendaraan sebagai wadah penyimpanan data
20.	Mencetak instruksi kepada pengguna untuk memasukkan data nama pemilik dan jarak tempuh kendaraan
21.	—
22.	Memulai perulangan sebanyak n kali untuk mengumpulkan data setiap kendaraan
23.	Membaca input nama pemilik kendaraan ke-i+1 dan menyimpannya ke variabel nama
24.	Memulai loop tak terbatas untuk memvalidasi input jarak tempuh
25.	Memulai blok percobaan untuk menangkap error jika input jarak tempuh bukan angka
26.	Membaca input jarak tempuh dari pengguna dikonversi ke integer dan disimpan ke variabel jarak
27.	Menambahkan data kendaraan berupa sublist berisi nama dan jarak ke dalam list kendaraan menggunakan metode append
28.	Menghentikan loop validasi setelah data berhasil disimpan
29.	Menangkap error ValueError jika pengguna memasukkan karakter bukan angka untuk jarak tempuh
30.	Mencetak pesan error dan meminta pengguna mengulang input jarak tempuh
31.	—
32.	Mencetak header atau judul bahwa data berikut adalah data sebelum diurutkan
33.	Memulai perulangan untuk menampilkan setiap elemen dalam list kendaraan
34.	Mencetak nama pemilik dan jarak tempuh setiap kendaraan sebelum proses pengurutan dalam format nama diikuti jarak KM
35.	—
36.	Memanggil fungsi exchange_sort dengan meneruskan list kendaraan dan nilai n untuk menjalankan proses pengurutan
37.	—
38.	Mencetak header bahwa data berikut adalah hasil setelah diurutkan berdasarkan jarak tempuh dari terkecil ke terbesar
39.	Memulai perulangan untuk menampilkan setiap elemen dalam list kendaraan yang sudah terurut
40.	Mencetak nama pemilik dan jarak tempuh setiap kendaraan setelah proses pengurutan dalam format nama diikuti jarak KM
41.	—
42.	Mengecek apakah file dijalankan langsung oleh interpreter Python bukan diimpor sebagai modul
43.	Memanggil fungsi main untuk memulai jalannya seluruh program

Output:
<img width="1836" height="513" alt="Screenshot 2026-05-04 114828" src="https://github.com/user-attachments/assets/f38963b1-4eb6-423d-a0ad-a77dc28d4f13" />

Pada percobaan ini saya memasukkan jumlah kendaraan sebanyak 3, kemudian program meminta data satu per satu secara berurutan. saya memasukkan nama adel dengan jarak tempuh 11 KM, nama davina dengan jarak tempuh 32 KM, dan nama atta dengan jarak tempuh 27 KM. Proses input berjalan lancar yang membuktikan bahwa bagian try-except bekerja dengan baik karena semua data yang dimasukan sudah sesuai format dari program.

Setelah semua data berhasil dikumpulkan, program menampilkan data sebelum diurutkan sesuai urutan yang saya inputkan sebelumnya, yakni adel 11 KM, davina 32 KM, dan atta 27 KM. Urutan tersebut mencerminkan kondisi asli data di dalam list sebelum proses pengurutan dilakukan.  Ketika fungsi exchange_sort dijalankan, algoritma mulai membandingkan setiap pasang elemen berdasarkan nilai jarak tempuh lalu program menemukan bahwa posisi davina dan atta perlu ditukar, semsntara adeel dengan jarak 11km merupakan jarak terkecil sudah berada pada posisi yang tepat. Hasilnya program berhasil menampilkan data setelah diurutkan yaitu adel 11 KM, atta 27 KM, dan davina 32 KM yang tersusun rapi dari jarak tempuh terkecil hingga terbesar, membuktikan bahwa algoritma Exchange Sort bekerja dengan benar . 

https://youtu.be/rvwXoQ4wmh8

Judul: Sistem manajemen parkir motor

Program sistem pengelolaan parkir kendaraan yang dapat digunakan untuk mencatat kendaraan yang masuk, mencari kendaraan berdasarkan nomor plat, dan menghapus data kendaraan yang sudah keluar dari area parkir. Setiap kendaraan disimpan dengan informasi berupa nomor plat, nama pemilik, dan jam masuk. Untuk mencari kendaraan, cukup memasukkan angka pada nomor plat tanpa perlu mengetik seluruh plat kendaraan.

Program ini menggunakan struktur data Hash Map dengan metode Separate Chaining untuk menyimpan data kendaraan. Nomor plat kendaraan akan diubah menjadi sebuah nilai angka menggunakan fungsi hash berbasis nilai ASCII, kemudian di-modulo 10. Nilai angka tersebut kemudian digunakan untuk menentukan lokasi penyimpanan data di dalam Hash Map. Jika terdapat dua atau lebih kendaraan yang tersimpan pada lokasi yang sama (collision), data kendaraan tidak akan saling menimpa, tetapi disimpan secara berurutan menggunakan Linked List.

Source Code:
<img width="1717" height="902" alt="Screenshot 2026-06-09 193439" src="https://github.com/user-attachments/assets/44c5e5f3-c119-4b4c-87e6-5bd14a84b64f" />
<img width="1724" height="872" alt="Screenshot 2026-06-09 193533" src="https://github.com/user-attachments/assets/5dd4a860-8f20-4cc1-8c61-4ef8a6b076a7" />
<img width="1728" height="893" alt="Screenshot 2026-06-09 193547" src="https://github.com/user-attachments/assets/5ea38688-4453-4091-9692-fadc17947171" />
<img width="1730" height="291" alt="Screenshot 2026-06-09 193601" src="https://github.com/user-attachments/assets/b01b822c-cf8c-4e99-aa4c-acf76eaff4c9" />

1. Membuat class Node yang digunakan sebagai elemen penyimpanan data pada linked list.
2. Membuat constructor init() untuk class Node.
3. Menyimpan nilai key ke dalam atribut node.
4. Menyimpan data kendaraan ke dalam atribut value.
5. Menginisialisasi atribut next dengan nilai None karena belum terhubung ke node lain.
6. -
7. Membuat class HashMapSeparateChaining untuk mengelola data parkir menggunakan struktur Hash Map dengan metode Separate Chaining.
8. Membuat constructor init() untuk class HashMapSeparateChaining.
9. Menyimpan ukuran tabel hash ke dalam atribut SIZE.
10. Membuat tabel hash berupa array dengan seluruh elemen bernilai None.
11. -
12. Membuat fungsi hash_function() untuk menghitung indeks penyimpanan data.
13. Menghasilkan nilai hash berdasarkan operasi modulo agar indeks berada dalam rentang tabel.
14. -
15. Membuat fungsi insert() untuk menambahkan data kendaraan ke Hash Map.
16. Menghitung indeks penyimpanan menggunakan fungsi hash.
17. Mengambil node pertama pada indeks yang diperoleh.
18. Melakukan penelusuran linked list pada indeks tersebut.
19. Memeriksa apakah key yang akan dimasukkan sudah ada.
20. Memperbarui data jika key sudah ditemukan.
21. Menghentikan proses karena data telah diperbarui.
22. Berpindah ke node berikutnya pada linked list.
23. Membuat node baru untuk menyimpan data kendaraan.
24. Menghubungkan node baru ke node pertama yang sudah ada pada indeks tersebut.
25. Menjadikan node baru sebagai node pertama (head) pada linked list.
26. -
27. Membuat fungsi search() untuk mencari data berdasarkan key.
28. Menghitung indeks pencarian menggunakan fungsi hash.
29. Mengambil node pertama pada indeks tersebut.
30. Melakukan penelusuran linked list.
31. Memeriksa apakah key yang dicari sesuai dengan key node saat ini.
32. Mengembalikan node jika data ditemukan.
33. Berpindah ke node berikutnya.
34. Mengembalikan None jika data tidak ditemukan.
35. -
36. Membuat fungsi remove_key() untuk menghapus data berdasarkan key.
37. Menghitung indeks lokasi data yang akan dihapus.
38. Mengambil node pertama pada indeks tersebut.
39. Membuat variabel prev untuk menyimpan node sebelumnya.
40. Melakukan penelusuran linked list.
41. Memeriksa apakah key yang dicari ditemukan.
42. Mengecek apakah node yang dihapus berada di posisi pertama.
43. Mengubah head linked list menjadi node berikutnya.
44. Jika node yang dihapus bukan node pertama.
45. Menghubungkan node sebelumnya dengan node sesudah node yang dihapus.
46. Mengembalikan nilai True sebagai tanda penghapusan berhasil.
47. Menyimpan node saat ini sebagai node sebelumnya.
48. Berpindah ke node berikutnya.
49. Mengembalikan nilai False jika data tidak ditemukan.
50. -
51. Membuat fungsi display() untuk menampilkan seluruh data parkir.
52. Menampilkan judul informasi area parkir.
53. Melakukan perulangan pada seluruh indeks Hash Map.
54. Menampilkan nomor zona parkir.
55. Mengambil node pertama pada zona tersebut.
56. Melakukan penelusuran linked list pada zona.
57. Menampilkan nomor plat dan nama pemilik kendaraan.
58. Berpindah ke node berikutnya.
59. Menampilkan keterangan akhir linked list pada zona tersebut.
60. -
61. Membuat fungsi plat_ke_angka() untuk mengubah nomor plat menjadi nilai numerik.
62. Menginisialisasi variabel total dengan nilai 0.
63. Melakukan perulangan pada setiap karakter nomor plat.
64. Mengubah karakter menjadi kode ASCII dan menjumlahkannya ke total.
65. Mengembalikan hasil konversi sebagai key Hash Map.
66. -
67. Membuat fungsi cari_plat_by_nomor() untuk mencari kendaraan berdasarkan sebagian nomor plat.
68. Melakukan perulangan pada seluruh zona parkir.
69. Mengambil node pertama pada zona yang sedang diperiksa.
70. Melakukan penelusuran linked list.
71. Memeriksa apakah nomor yang dicari terdapat pada plat kendaraan.
72. Mengembalikan node jika kendaraan ditemukan.
73. Berpindah ke node berikutnya.
74. Mengembalikan None jika kendaraan tidak ditemukan.
75. -
76. Membuat fungsi hapus_plat_by_nomor() untuk menghapus kendaraan berdasarkan sebagian nomor plat.
77. Melakukan perulangan pada seluruh zona parkir.
78. Mengambil node pertama pada zona yang sedang diperiksa.
79. Melakukan penelusuran linked list.
80. Memeriksa apakah nomor yang dicari terdapat pada plat kendaraan.
81. Menghapus data kendaraan menggunakan key yang ditemukan.
82. Berpindah ke node berikutnya.
83. Mengembalikan nilai False jika kendaraan tidak ditemukan.
84. -
85. Membuat fungsi main() sebagai fungsi utama program.
86. Membuat objek Hash Map bernama parkir.
87. Menambahkan data kendaraan pertama ke dalam Hash Map.
88. Menambahkan data kendaraan kedua ke dalam Hash Map.
89. Menambahkan data kendaraan ketiga ke dalam Hash Map.
90. Menambahkan data kendaraan keempat ke dalam Hash Map.
91. Menambahkan data kendaraan kelima ke dalam Hash Map.
92. Menampilkan seluruh data kendaraan yang sedang parkir.
93. -
94. Meminta pengguna memasukkan nomor kendaraan yang ingin dicari.
95. Menjalankan proses pencarian kendaraan.
96. Memeriksa apakah kendaraan ditemukan.
97. Menampilkan informasi kendaraan yang ditemukan.
98. Jika kendaraan tidak ditemukan.
99. Menampilkan pesan bahwa kendaraan tidak ditemukan.
100. -
101. Meminta pengguna memasukkan nomor kendaraan yang akan keluar.
102. Melakukan pencarian kendaraan yang akan keluar.
103. Memeriksa apakah kendaraan ditemukan.
104. Mengambil nomor plat lengkap kendaraan.
105. Menghapus data kendaraan dari Hash Map.
106. Menampilkan pesan bahwa kendaraan berhasil keluar.
107. Jika kendaraan tidak ditemukan.
108. Menampilkan pesan bahwa kendaraan tidak ditemukan.
109. -
110. Menampilkan informasi setelah kendaraan keluar.
111. Menampilkan kondisi terbaru area parkir.
112. -
113. Memeriksa apakah file dijalankan sebagai program utama.
114. Menjalankan fungsi main().

Output:
<img width="1853" height="787" alt="Screenshot 2026-06-09 195259" src="https://github.com/user-attachments/assets/83e23c8e-43eb-449b-811b-8d79d01d4e81" />

Ketika program pertama kali dijalankan, sistem menampilkan seluruh isi area parkir yang terdiri dari 10 indeks (indeks 0 sampai indeks 9). Dari 5 kendaraan yang dimasukkan, masing-masing ditempatkan di indeks yang ditentukan oleh hasil fungsi hash. Atta dengan plat BE1234AB ditempatkan di indeks 1, vina dengan plat BE5678CD ditempatkan di indeks 3, dan adel dengan plat BG9012EF ditempatkan di indeks 9. Sementara itu, naila dengan plat BE1314GH dan alin dengan plat BE1516IJ sama-sama menghasilkan nilai hash yang berakhiran 5, sehingga keduanya ditempatkan di indeks 5. Kondisi ini disebut collision. Karena program menggunakan metode separate chaining, kedua kendaraan tersebut tidak saling menimpa melainkan disusun secara berantai menggunakan linked list. Alin berada di posisi depan karena dimasukkan lebih akhir, sedangkan naila berada di posisi belakang.

Setelah tampilan awal muncul, program meminta input nomor angka plat yang ingin dicari. Saya menginputkan angka 5678, kemudian program menelusuri seluruh indeks untuk mencari plat yang mengandung angka tersebut. Program berhasil menemukan kendaraan dengan plat BE5678CD milik vina yang tercatat masuk pada jam 08:42, lalu informasi tersebut ditampilkan.

Selanjutnya program meminta input nomor plat kendaraan yang akan keluar. Saya menginputkan angka 5678, program menemukan BE5678CD dan menghapus data kendaraan tersebut dari hash table menggunakan fungsi remove_key(). Setelah penghapusan berhasil, program menampilkan pesan bahwa BE5678CD berhasil keluar. Indeks 3 yang sebelumnya berisi kendaraan milik vina kini berubah menjadi KOSONG, menandakan data berhasil dihapus.

Link Youtube: https://youtu.be/Oiep_17dx2k


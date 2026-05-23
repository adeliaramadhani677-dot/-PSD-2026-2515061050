Judul: Katalog Anime

Ini merupakan sebuah program sederhana untuk mengelola katalog anime. Dalam program ini terdapat fitur untuk menambahkan anime, menghapus anime, mencari anime berdasarkan judul ataupun genre, menampilkan daftar anime secara urut dari A-Z, serta menghitung jumlah anime yang tersimpan dalam katalog. Seluruh data anime disimpan dalam bentuk node yang memiliki informasi judul dan genre. Program dijalankan melalui menu interaktif di terminal sehingga saya dapat memilih akan menggunakan fitur mana.

Struktur data yang diterapkan pada program ini adalah Binary Search Tree atau BST. Pada BST, data disimpan dalam bentuk tree dengan aturan bahwa data yang lebih kecil ditempatkan di sebelah kiri dan data yang lebih besar ditempatkan di sebelah kanan. Dengan metode ini, proses pencarian, penambahan, dan penghapusan data menjadi lebih terstruktur dan efisien dibandingkan pencarian biasa pada list. Program juga menggunakan algoritma traversal inorder untuk menampilkan data anime secara terurut berdasarkan judul dari A-Z.

Source Code: 
<img width="1731" height="909" alt="Screenshot 2026-05-24 021427" src="https://github.com/user-attachments/assets/ec657328-6676-4f63-af0a-d5e189c0d01a" />
<img width="1729" height="906" alt="Screenshot 2026-05-24 021447" src="https://github.com/user-attachments/assets/c4fbbdd8-86f0-4286-bd5d-a9f0c2753914" />
<img width="1728" height="907" alt="Screenshot 2026-05-24 021512" src="https://github.com/user-attachments/assets/967dd066-2aed-4e7d-88f0-c6d771afb60c" />
<img width="1718" height="903" alt="Screenshot 2026-05-24 021537" src="https://github.com/user-attachments/assets/c61164be-8d0f-4d64-bc9d-25a0348ac283" />
<img width="1727" height="805" alt="Screenshot 2026-05-24 021553" src="https://github.com/user-attachments/assets/4166e375-712c-46f6-8b51-efddf07e0c8e" />

1. Membuat class Node yang digunakan untuk menyimpan data anime di dalam Binary Search Tree (BST).
2. Membuat constructor __init__ pada class Node yang akan dijalankan saat object dibuat.
3. Menyimpan nilai judul anime ke dalam atribut self.judul.
4. Menyimpan nilai genre anime ke dalam atribut self.genre.
5. Membuat pointer left bernilai None sebagai cabang kiri node.
6. Membuat pointer right bernilai None sebagai cabang kanan node.
7. -
8. Membuat class BSTFilm untuk mengelola seluruh data BST anime.
9. Membuat constructor untuk class BSTFilm.
10. Mengatur root bernilai None karena BST masih kosong dan belum memiliki data.
11. -
12. Membuat fungsi insert_node() untuk menambahkan data anime ke BST secara rekursif.
13. Mengecek apakah posisi root masih kosong atau tidak ada node.
14. Jika kosong, maka dibuat node baru berisi judul dan genre anime.
15. Membandingkan judul anime input dengan judul pada root menggunakan huruf kecil agar tidak sensitif huruf besar/kecil.
16. Jika judul input lebih kecil, maka data dimasukkan ke cabang kiri BST.
17. Jika kondisi sebelumnya salah, program mengecek apakah judul lebih besar dari root.
18. Jika judul lebih besar, maka data dimasukkan ke cabang kanan BST.
19. Jika judul sama, berarti anime sudah ada di BST.
20. Menampilkan pesan bahwa anime sudah ada sehingga tidak ditambahkan lagi.
21. Mengembalikan node root setelah proses penambahan selesai.
22. -
23. Membuat fungsi insert() sebagai fungsi utama untuk menambah anime.
24. Memanggil fungsi insert_node() dan memperbarui root BST jika ada perubahan.
25. -
26. Membuat fungsi delete_node() untuk menghapus data anime dari BST.
27. Mengecek apakah node yang dicari kosong.
28. Jika kosong, fungsi mengembalikan None karena data tidak ditemukan.
29. Membandingkan judul input dengan judul pada root.
30. Jika judul lebih kecil, pencarian data yang akan dihapus dilakukan ke subtree kiri.
31. Jika kondisi sebelumnya salah, dicek apakah judul lebih besar.
32. Jika lebih besar, pencarian dilakukan ke subtree kanan.
33. Jika judul sama, berarti node ditemukan dan siap dihapus.
34. Mengecek apakah node tidak memiliki anak kiri.
35. Jika benar, node diganti dengan anak kanan.
36. Mengecek apakah node tidak memiliki anak kanan.
37. Jika benar, node diganti dengan anak kiri.
38. Menentukan node pengganti (successor) dari subtree kanan.
39. Mengambil node paling kiri pada subtree kanan karena nilainya paling kecil.
40. Perulangan dilakukan selama successor masih memiliki anak kiri.
41. Menyalin judul successor ke node yang akan dihapus.
42. Menyalin genre successor ke node yang akan dihapus.
43. Menghapus node successor asli karena datanya sudah dipindahkan.
44. Mengembalikan root setelah proses penghapusan selesai.
45. -
46. Membuat fungsi delete() sebagai fungsi utama untuk menghapus anime.
47. Mengecek terlebih dahulu apakah anime ada di BST atau tidak.
48. Jika anime tidak ditemukan, tampilkan pesan kesalahan.
49. Menghentikan fungsi agar proses hapus tidak dilanjutkan.
50. Memanggil fungsi delete_node() untuk menghapus data anime.
51. Menampilkan pesan bahwa anime berhasil dihapus.
52. -
53. Membuat fungsi search_judul_node() untuk mencari anime berdasarkan judul.
54. Mengecek apakah node saat ini kosong.
55. Jika kosong, berarti data tidak ditemukan dan fungsi mengembalikan None.
56. Membandingkan judul input dengan judul pada root BST.
57. Jika sama, node ditemukan dan dikembalikan.
58. Mengecek apakah judul input lebih kecil dari root.
59. Jika lebih kecil, pencarian dilanjutkan ke subtree kiri.
60. Jika tidak, pencarian dilanjutkan ke subtree kanan.
61. -
62. Membuat fungsi search_judul() sebagai fungsi pencarian utama.
63. Memanggil fungsi pencarian mulai dari root BST.
64. -
65. Membuat fungsi search_genre_node() untuk mencari anime berdasarkan genre.
66. Mengecek apakah node kosong.
67. Jika kosong, fungsi dihentikan karena tidak ada data lagi.
68. Melakukan traversal ke subtree kiri terlebih dahulu.
69. Membandingkan genre anime dengan genre input pengguna.
70. Jika genre sama, node anime dimasukkan ke dalam list hasil.
71. Melanjutkan traversal ke subtree kanan.
72. -
73. Membuat fungsi search_genre() sebagai fungsi utama pencarian genre.
74. Membuat list kosong bernama hasil untuk menyimpan data yang ditemukan.
75. Memanggil fungsi pencarian genre mulai dari root BST.
76. Mengembalikan list hasil pencarian genre.
77. -
78. Membuat fungsi inorder() untuk traversal inorder BST.
79. Mengecek apakah node kosong.
80. Jika kosong, fungsi dihentikan.
81. Traversal dilakukan ke subtree kiri terlebih dahulu.
82. Menambahkan node saat ini ke list hasil.
83. Traversal dilanjutkan ke subtree kanan sehingga data menjadi urut A-Z.
84. -
85. Membuat fungsi count_nodes() untuk menghitung jumlah anime dalam BST.
86. Mengecek apakah node kosong.
87. Jika kosong, fungsi mengembalikan nilai 0.
88. Menghitung total node dengan menjumlahkan node sekarang, subtree kiri, dan subtree kanan.
89. -
90. Membuat fungsi cetak_header_tabel() untuk menampilkan judul kolom tabel.
91. Menampilkan tulisan “JUDUL” dan “GENRE” dengan format rapi.
92. -
93. Membuat fungsi cetak_baris() untuk menampilkan isi data anime per baris.
94. Menampilkan judul dan genre anime dengan format tabel yang rapi.
95. -
96. Membuat fungsi main() sebagai program utama.
97. Membuat object BST bernama bst dari class BSTFilm.
98. -
99. Membuat variabel pilih dengan nilai awal 0.
100. Perulangan menu akan terus berjalan selama user belum memilih menu 7.
101. Menampilkan judul program BST katalog anime.
102. Menampilkan menu untuk menambahkan anime.
103. Menampilkan menu untuk menghapus anime.
104. Menampilkan menu untuk mencari anime berdasarkan judul.
105. Menampilkan menu untuk mencari anime berdasarkan genre.
106. Menampilkan menu untuk menampilkan anime urut A-Z.
107. Menampilkan menu untuk menghitung jumlah anime.
108. Menampilkan menu keluar program.
109. -
110. Memulai blok try agar program tidak error saat input salah.
111. Meminta user memasukkan pilihan menu lalu mengubahnya menjadi integer.
112. Jika input bukan angka maka terjadi ValueError.
113. Menampilkan pesan bahwa input tidak valid.
114. Mengulang kembali ke menu awal menggunakan continue.
115. -
116. Mengecek apakah user memilih menu 1.
117. Memulai blok try untuk input data anime.
118. Meminta user memasukkan judul anime.
119. Meminta user memasukkan genre anime.
120. Menambahkan anime ke BST menggunakan fungsi insert().
121. Menampilkan pesan bahwa anime berhasil ditambahkan.
122. Jika input menyebabkan error ValueError.
123. Menampilkan pesan input tidak valid.
124. -
125. Mengecek apakah user memilih menu 2.
126. Meminta user memasukkan judul anime yang ingin dihapus.
127. Memanggil fungsi delete() untuk menghapus anime.
128. -
129. Mengecek apakah user memilih menu 3.
130. Meminta user memasukkan judul anime yang ingin dicari.
131. Menyimpan hasil pencarian ke variabel hasil.
132. Mengecek apakah anime ditemukan.
133. Menampilkan header tabel hasil pencarian.
134. Menampilkan data anime yang ditemukan.
135. Jika anime tidak ditemukan.
136. Menampilkan pesan bahwa anime tidak ditemukan.
137. -
138. Mengecek apakah user memilih menu 4.
139. Meminta user memasukkan genre anime yang ingin dicari.
140. Menyimpan hasil pencarian genre ke variabel hasil.
141. Mengecek apakah ada anime dengan genre tersebut.
142. Menampilkan jumlah anime yang ditemukan sesuai genre.
143. Menampilkan header tabel hasil pencarian.
144. Melakukan perulangan untuk menampilkan semua anime yang ditemukan.
145. Menampilkan setiap anime hasil pencarian genre.
146. Jika tidak ada anime dengan genre tersebut.
147. Menampilkan pesan bahwa genre tidak ditemukan.
148. -
149. Mengecek apakah user memilih menu 5.
150. Membuat list kosong untuk menyimpan hasil traversal inorder.
151. Menjalankan traversal inorder agar data anime urut A-Z.
152. Mengecek apakah BST memiliki data anime.
153. Menampilkan jumlah anime yang ada dalam katalog.
154. Menampilkan header tabel.
155. Melakukan perulangan untuk menampilkan semua anime.
156. Menampilkan anime satu per satu secara urut A-Z.
157. Jika BST kosong.
158. Menampilkan pesan bahwa katalog kosong.
159. -
160. Mengecek apakah user memilih menu 6.
161. Menampilkan jumlah total anime dalam BST menggunakan fungsi count_nodes().
162. -
163. Mengecek apakah user memilih menu 7.
164. Menampilkan pesan bahwa program selesai dijalankan.
165. -
166. Jika user memasukkan pilihan selain menu yang tersedia.
167. Menampilkan pesan bahwa pilihan tidak valid.
168. -
169. Mengecek apakah file Python dijalankan langsung.
170. Memanggil fungsi main() agar program utama dijalankan.

Output Program:
<img width="1713" height="905" alt="Screenshot 2026-05-24 022913" src="https://github.com/user-attachments/assets/d98a3386-cf16-4d4b-a91b-48e9605dee53" />
<img width="1707" height="905" alt="Screenshot 2026-05-24 022958" src="https://github.com/user-attachments/assets/15f7f57b-ad6a-44c2-96f0-b20206d36b77" />
<img width="1708" height="906" alt="Screenshot 2026-05-24 023023" src="https://github.com/user-attachments/assets/7c02ec62-f4b7-4468-824e-44dadf600cbb" />
<img width="1711" height="905" alt="Screenshot 2026-05-24 023035" src="https://github.com/user-attachments/assets/f2da2848-1f95-4d84-a69c-8ad5b623eea5" />
<img width="1698" height="142" alt="Screenshot 2026-05-24 023115" src="https://github.com/user-attachments/assets/853a7e8a-6c83-48bc-91ba-91e30824c61f" />

Saat program dijalankan, pertama program menampilkan menu utama BST Katalog Anime yang berisi beberapa pilihan fitur seperti menambahkan anime, menghapus anime, mencari anime berdasarkan judul maupun genre, menampilkan daftar anime secara urut A-Z, menghitung jumlah anime, dan keluar dari program. Pada proses pengujian, saya menambahkan beberapa data anime ke dalam katalog, yaitu “mtp”, “86”, “bleach”, “sao”, “prism”, “barbatos gundam”, dan “conan” beserta genre masing-masing. Setiap data yang berhasil dimasukkan akan menampilkan pesan bahwa anime berhasil ditambahkan ke dalam BST. Hal ini menunjukkan bahwa fungsi insert pada Binary Search Tree berjalan dengan baik.

Selanjutnya saya mencoba fitur hapus anime dengan menghapus data “prism”. Program berhasil menemukan data tersebut di dalam BST lalu menghapusnya, kemudian menampilkan pesan bahwa anime berhasil dihapus. Setelah itu saya mencoba fitur pencarian berdasarkan judul dengan memasukkan judul “mtp”. Program berhasil menemukan anime tersebut dan menampilkan data judul serta genre dalam bentuk tabel. Saya juga mencoba pencarian berdasarkan genre “mistery” dan program berhasil menampilkan dua anime yang memiliki genre tersebut, yaitu “conan” dan “mtp”. Hal ini menunjukkan bahwa fitur pencarian data sudah berjalan sesuai dengan yang diharapkan.

Pada fitur urut judul A-Z, program menampilkan seluruh data anime secara terurut yaitu “86”, “barbatos gundam”, “bleach”, “conan”, “mtp”, dan “sao”. Pengurutan ini dilakukan menggunakan traversal inorder pada Binary Search Tree sehingga data dapat tampil secara otomatis sesuai urutan alfabet. Setelah itu saya menjalankan fitur jumlah anime dan program menampilkan total data sebanyak 6 anime karena satu data sebelumnya sudah dihapus. Terakhir saya memilih menu keluar dan program menampilkan pesan “Program selesai”, yang menandakan seluruh proses program telah berjalan dengan baik tanpa error.

link video:

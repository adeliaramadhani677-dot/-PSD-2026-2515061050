Judul program: pengecekan barang pada sebuah toko

Program ini berfungsi untuk mengecek ketersediaan barang pada sebuah stok dengan menggunakan sebuah input dari pengguna. Data disimpan dalam list yang berisi sebuah beberapa nama barang, seperti mie, kopi, the, susu, ataupun yang lainnya. Pada program ini pengguna diminta memasukan nama barang yang ingin dicari, lalu program akan menghitung ada berapa atau berapa kali barang itu muncul dari daftar. Program juga menampilkan posisi indeks terakhir barang yang dicari itu ditemukan pada indeks ke berapa. Jika mencari barang yang tidak ada pada daftar maka program akan merespon dengan mneginformasikan bahwa barang itu tidak ditemukan.

Algoritma yang diterapkan dalam program ini yaitu sequential search dimana algoritma ini bekerja dengan cara menelusuri data satu persatu dari indeks awal hingga akhir untuk mencari data yang sesuai dengan barang atau data yang dicari. Struktur data yang digunakan merupakan array atau list pada pemrograman python, dimana ini untuk menyimpan sekumpulan data barang tersebut, program ini juga menggunakan proses perulangan while dan if untuk melakukan pencarian dan pengecekan datanya.

Source Code:
<img width="1728" height="947" alt="Screenshot 2026-05-09 213754" src="https://github.com/user-attachments/assets/59dc322c-3eaa-46f8-aeb6-8012218068e0" />
<img width="1727" height="466" alt="Screenshot 2026-05-09 213822" src="https://github.com/user-attachments/assets/5c8327f4-c925-43d7-b6f0-04d5820f979f" />

1. Mendefinisikan fungsi sequential_search dengan tiga parameter: data (list barang), n (jumlah elemen), dan target (barang yang dicari)
2. Menginisialisasi variabel i dengan nilai 0 sebagai indeks awal penelusuran
3. Menginisialisasi variabel counter dengan nilai 0 untuk menghitung jumlah kemunculan target
4. Menginisialisasi variabel last_index dengan nilai -1 sebagai penanda bahwa target belum ditemukan
5. Memulai perulangan while yang berjalan selama nilai i masih kurang dari n
6. Mengecek apakah elemen pada posisi i dalam list data sama dengan target
7. Jika kondisi terpenuhi, menambahkan nilai counter sebanyak 1
8. Menyimpan nilai i ke last_index sebagai posisi terakhir target ditemukan
9. Menambahkan nilai i sebanyak 1 untuk berpindah ke elemen berikutnya
10. Mengembalikan dua nilai sekaligus yaitu counter dan last_index sebagai hasil fungsi
11. -
12. Mendefinisikan fungsi main sebagai fungsi utama program
13. Mendefinisikan list data berisi 15 nama barang (baris pertama dari tiga baris)
14. Melanjutkan isi list data (baris kedua dari tiga baris)
15. Melanjutkan dan menutup isi list data (baris ketiga dari tiga baris)
16. -
17. Menghitung jumlah elemen dalam list data menggunakan len() dan menyimpannya ke variabel n
18. Mencetak teks judul stok barang beserta jumlah itemnya
19. Mencetak seluruh isi list data diikuti baris kosong dari \n
20. -
21. Membuat list baru barang_tersedia berisi barang unik dengan mengubah data menjadi set (menghapus duplikat) lalu dikonversi kembali ke list
22. Mencetak teks header daftar barang yang tersedia
23. Melakukan perulangan pada barang_tersedia menggunakan enumerate dengan nomor urut dimulai dari 1
24. Mencetak nomor urut dan nama setiap barang
25. -
26. Mencetak satu baris kosong sebagai pemisah antar bagian output
27. -
28. Memulai perulangan while True yang berjalan terus sampai ada perintah break
29. Menampilkan prompt input kepada pengguna dan menyimpan hasilnya ke target, lalu .strip() menghapus spasi di awal dan akhir teks
30. Mengecek apakah input yang dimasukkan pengguna adalah string kosong
31. Jika kosong, mencetak pesan peringatan bahwa input tidak boleh kosong
32. Jika input tidak kosong, masuk ke blok else
33. Menghentikan perulangan while karena input sudah valid
34. -
35. Memanggil fungsi sequential_search dengan argumen data, n, dan target, lalu menyimpan dua nilai kembaliannya ke counter dan last_index
36. -
37. Mengecek apakah nilai counter lebih dari 0, artinya target berhasil ditemukan
38. Jika ditemukan, mencetak nama target beserta jumlah kemunculannya
39. Masuk ke blok else jika counter bernilai 0
40. Mencetak pesan bahwa target tidak ditemukan dalam data
41. -
42. Mengecek apakah last_index tidak sama dengan -1, artinya target pernah ditemukan
43. Jika ya, mencetak indeks terakhir di mana target ditemukan
44. Masuk ke blok else jika last_index masih bernilai -1
45. Mencetak pesan bahwa target tidak ditemukan
46. -
47. Mengecek apakah file ini dijalankan langsung, bukan diimpor sebagai modul oleh file lain
48. Jika ya, memanggil fungsi main() untuk menjalankan program

Output:
<img width="1830" height="405" alt="Screenshot 2026-05-09 214056" src="https://github.com/user-attachments/assets/42a3a2bc-7910-40a6-af4a-06f1e12b36ea" />

Program ini menerapkan algoritma Sequential Search untuk melakukan pengecekan stok barang pada sebuah toko.
bagian pertama output menampilkan seluruh isi stok barang yang ada yaitu berupa 15 data barang dimana beberapa barang muncul lebiih dari satu kali untuk mempresentasikan jumlah stok yang ada, nilai 15 diperoleh secara otomatis melalui fungsi len(data) kemudian ditampilkan bersama seluruh isi listnya.
bagian kedua menampilkan daftar barang yang tersedia ditoko. program menggunakan set untuk mendeteksi duplikat dari list sehingga hanya tersisa lima jenis barang berbeda berupa susu, teh,kopi,mie, dan roti dimana urutan tampilannya bisa berbeda setiap program dijalankan.
bagian ketiga pengguna menginputkan sebuah barang, pada bagian ini saya menginputkan Teh sebagai barang yang ingin dicari, karena input yang diberikan tidak kosong maka program langsung melanjutkan ke proses pencarian.
bagian keempat program melakukan pencarian dari indeks 0 sampai indeks akhir yaitu 14, setiap ditemukan barang yang dicari misalnya Teh maka counter bertambah satu dan indeks terakhir diperbarui dengan indeks tersebut. berdasarkan pencarian barang Teh ditemukan pada indeks ke 1,5, dan yang terakhir pada indeks ke 12, sehingga nilai counter adalah 3 dan indeks terakhir bernilai 12. Tampilan hasil akhir yaitu program mencetak Teh berhasil ditemukan sebanyak 3 dan terakhir terlihat pada indeks ke 12 dalam. Dapat dibuktikan bahwa kode berjalan lancar tanpa error.

Link YouTube: https://youtu.be/tORhwmN8Zjg

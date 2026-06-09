Judul: Sistem manajemen parkir motor

Program sistem pengelolaan parkir kendaraan yang dapat digunakan untuk mencatat kendaraan yang masuk, mencari kendaraan berdasarkan nomor plat, dan menghapus data kendaraan yang sudah keluar dari area parkir. Setiap kendaraan disimpan dengan informasi berupa nomor plat, nama pemilik, dan jam masuk. Untuk mencari kendaraan, cukup memasukkan angka pada nomor plat tanpa perlu mengetik seluruh plat kendaraan.

Program ini menggunakan struktur data Hash Map dengan metode Separate Chaining untuk menyimpan data kendaraan. Nomor plat kendaraan akan diubah menjadi sebuah nilai angka menggunakan fungsi hash berbasis nilai ASCII, kemudian di-modulo 10. Nilai angka tersebut kemudian digunakan untuk menentukan lokasi penyimpanan data di dalam Hash Map. Jika terdapat dua atau lebih kendaraan yang tersimpan pada lokasi yang sama (collision), data kendaraan tidak akan saling menimpa, tetapi disimpan secara berurutan menggunakan Linked List.

Source Code:
<img width="1717" height="902" alt="Screenshot 2026-06-09 193439" src="https://github.com/user-attachments/assets/44c5e5f3-c119-4b4c-87e6-5bd14a84b64f" />
<img width="1724" height="872" alt="Screenshot 2026-06-09 193533" src="https://github.com/user-attachments/assets/5dd4a860-8f20-4cc1-8c61-4ef8a6b076a7" />
<img width="1728" height="893" alt="Screenshot 2026-06-09 193547" src="https://github.com/user-attachments/assets/5ea38688-4453-4091-9692-fadc17947171" />
<img width="1730" height="291" alt="Screenshot 2026-06-09 193601" src="https://github.com/user-attachments/assets/b01b822c-cf8c-4e99-aa4c-acf76eaff4c9" />


class StackArray:
    def __init__(self, max_size=10):
        self.MAX = max_size
        self.st = [None] * self.MAX
        self.top_idx = -1

    def is_empty(self):
        return self.top_idx == -1

    def is_full(self):
        return self.top_idx == self.MAX - 1

    def push(self, x):
        if self.is_full():
            print("Stack penuh! Kapasitas catatan lapisan candi sudah maksimal.")
            return
        self.top_idx += 1
        self.st[self.top_idx] = x
        print(f"Lapisan '{x}' berhasil dicatat di posisi #{self.top_idx + 1}.")

    def pop(self):
        if self.is_empty():
            print("Stack kosong! Tidak ada lapisan yang bisa direstorasi.")
            return
        item = self.st[self.top_idx]
        print(f"Restorasi: '{item}' diangkat kembali ke posisi semula.")
        self.top_idx -= 1

    def peek(self):
        if self.is_empty():
            print("Stack kosong! Tidak ada lapisan teratas.")
            return
        print(f"Lapisan teratas saat ini: '{self.st[self.top_idx]}' (posisi #{self.top_idx + 1})")

    def display(self):
        if self.is_empty():
            print("Stack kosong! Belum ada lapisan yang dicatat.")
            return
        print("Urutan lapisan:")
        for i in range(self.top_idx, -1, -1):
            penanda = " - teratas" if i == self.top_idx else ""
            print(f"  #{i + 1}  {self.st[i]}{penanda}")

def main():
    print("Pembongkaran Candi")

    candi = StackArray()
    pilih = 0

    while pilih != 5:
        print(f"\nLapisan tercatat: {candi.top_idx + 1}/{candi.MAX}")
        print("1. Catat Bongkar  (Push)")
        print("2. Restorasi      (Pop)")
        print("3. Lihat Teratas  (Peek)")
        print("4. Tampilkan Semua")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            nama = input("Nama lapisan batu: ").strip()
            if not nama:
                print("Nama lapisan tidak boleh kosong.")
            else:
                candi.push(nama)
        elif pilih == 2:
            candi.pop()
        elif pilih == 3:
            candi.peek()
        elif pilih == 4:
            candi.display()
        elif pilih == 5:
            print("Program selesai. Pembongkaran candi tersimpan.")
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()

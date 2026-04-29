def menu():
    print("\nDaftar Belanja")
    print("1. Masukkan jumlah item")
    print("2. Masukkan item belanja")
    print("3. Tampilkan semua item belanja")
    print("4. Hapus item belanja")
    print("5. Cari item belanja")
    print("6. Keluar")


def main():
    belanja = []
    n = 0
    running = True

    while running:
        menu()
        try:
            choice = int(input("Pilihan: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue

        if choice == 1:
            n = int(input("\nBerapa item yang ingin dimasukkan? "))
            belanja = [""] * n
            print(f" Siap menampung {n} item belanja!")

        elif choice == 2:
            if n == 0:
                print("\n  Masukkan jumlah item terlebih dahulu! (Pilihan 1)")
            else:
                print(f"\nMasukkan {n} item belanja:")
                for i in range(n):
                    while True:
                        try:
                            item = input(f"  Item ke-{i+1}: ").strip()
                            if item == "":
                                print("  Item tidak boleh kosong!")
                            else:
                                belanja[i] = item
                                break
                        except ValueError:
                            print("  Input tidak valid!")
                print(f"\n Daftar belanja tersimpan: {belanja}")

        elif choice == 3:
            if n == 0:
                print("\n  Masukkan jumlah item terlebih dahulu! (Pilihan 1)")
            elif all(item == "" for item in belanja):
                print("\n  (Daftar masih kosong)")
            else:
                print("\n Daftar Belanja:")
                for i in range(n):
                    status = belanja[i] if belanja[i] != "" else "(kosong)"
                    print(f"  {i+1}. {status}")

        elif choice == 4:
            if n == 0:
                print("\n  Masukkan jumlah item terlebih dahulu! (Pilihan 1)")
            elif all(item == "" for item in belanja):
                print("\n  Daftar belanja masih kosong!")
            else:
                print("\n  Hapus Item Belanja:")
                for i in range(n):
                    status = belanja[i] if belanja[i] != "" else "(kosong)"
                    print(f"  {i+1}. {status}")
                while True:
                    try:
                        idx = int(input(f"\n  Pilih nomor item yang ingin dihapus (1-{n}): "))
                        if 1 <= idx <= n:
                            if belanja[idx-1] == "":
                                print("  Item sudah kosong!")
                            else:
                                print(f"  Item '{belanja[idx-1]}' berhasil dihapus!")
                                belanja[idx-1] = ""
                            break
                        else:
                            print(f"  Masukkan nomor 1-{n}!")
                    except ValueError:
                        print("  Input tidak valid!")

        elif choice == 5:
            if n == 0:
                print("\n  Masukkan jumlah item terlebih dahulu! (Pilihan 1)")
            elif all(item == "" for item in belanja):
                print("\n  Daftar belanja masih kosong!")
            else:
                cari = input("\n Masukkan nama item yang dicari: ").strip().lower()
                ditemukan = False
                for i in range(n):
                    if belanja[i].lower() == cari:
                        print(f"\n   Ditemukan!")
                        print(f"  Nama item : {belanja[i]}")
                        print(f"  Posisi    : slot {i} (item ke-{i+1})")
                        print(f"  ID memori : {id(belanja[i])}")
                        ditemukan = True
                        break
                if not ditemukan:
                    print(f"\n   Item '{cari}' tidak ditemukan!")

        elif choice == 6:
            running = False
            print("Program selesai. Selamat berbelanja! ")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()

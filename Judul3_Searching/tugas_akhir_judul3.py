def sequential_search(data, n, target):
    i = 0
    counter = 0
    last_index = -1 
    while i < n:
        if data[i] == target:
            counter += 1
            last_index = i 
        i += 1
    return counter, last_index  

def main():
    data = ["Mie", "Teh", "Mie", "Kopi", "Roti",
            "Teh", "Mie", "Susu", "Kopi", "Mie",
            "Roti", "Susu", "Teh", "Kopi", "Mie"]

    n = len(data)
    print(f"Stok barang ({n} item):")
    print(f"   {data}\n")

    barang_tersedia = list(set(data))
    print("Barang yang tersedia di toko:")
    for i, barang in enumerate(barang_tersedia, 1):
        print(f"   {i}. {barang}")

    print()

    while True:
        target = input("Masukkan nama barang yang ingin dicek: ").strip()
        if target == "":
            print("Input tidak boleh kosong")
        else:
            break

    counter, last_index = sequential_search(data, n, target)

    if counter > 0:
        print(f"\n'{target}' ditemukan sebanyak {counter} unit")
    else:
        print(f"\n'{target}' tidak ditemukan")

    if last_index != -1:
        print(f"   Terakhir terlihat pada indeks ke-{last_index}")
    else:
        print("   Tidak ditemukan")

if __name__ == "__main__":
    main()

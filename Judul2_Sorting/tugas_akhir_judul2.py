def tukar(kendaraan, i, j):
    temp = kendaraan[i]
    kendaraan[i] = kendaraan[j]
    kendaraan[j] = temp

def exchange_sort(kendaraan, n):
    for i in range(n - 1):
        for j in range(i + 1, n):
            if kendaraan[i][1] > kendaraan[j][1]:
                tukar(kendaraan, i, j)

def main():
    try:
        n = int(input("Masukkan jumlah kendaraan: "))
    except ValueError:
        print("Input tidak valid!")
        return

    kendaraan = []
    print("Masukkan data kendaraan (nama pemilik dan jarak tempuh KM):")

    for i in range(n):
        nama = input(f"Nama pemilik kendaraan ke-{i+1}: ")
        while True:
            try:
                jarak = int(input(f"Jarak tempuh {nama} (KM): "))
                kendaraan.append([nama, jarak])
                break
            except ValueError:
                print("Input tidak valid, silakan masukkan angka!")

    print("Data sebelum diurutkan:")
    for data in kendaraan:
        print(f"{data[0]} - {data[1]} KM")

    exchange_sort(kendaraan, n)

    print("Data setelah diurutkan (berdasarkan jarak tempuh):")
    for data in kendaraan:
        print(f"{data[0]} - {data[1]} KM")

if __name__ == "__main__":
    main()

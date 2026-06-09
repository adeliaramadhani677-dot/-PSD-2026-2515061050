class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMapSeparateChaining:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next
        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current
            current = current.next
        return None

    def remove_key(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        while current is not None:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                return True
            prev = current
            current = current.next
        return False

    def display(self):
        print("Isi Area Parkir:")
        for i in range(self.SIZE):
            print("Zona " + str(i) + ": ", end="")
            current = self.table[i]
            while current is not None:
                print("(" + current.value["plat"] + ", " + current.value["pemilik"] + ") -> ", end="")
                current = current.next
            print("KOSONG")

def plat_ke_angka(plat):
    total = 0
    for i, c in enumerate(plat.upper()):
        total += ord(c) * (i + 1)
    return total

def cari_plat_by_nomor(parkir, nomor):
    for i in range(parkir.SIZE):
        current = parkir.table[i]
        while current is not None:
            if nomor in current.value["plat"]:
                return current
            current = current.next
    return None

def hapus_plat_by_nomor(parkir, nomor):
    for i in range(parkir.SIZE):
        current = parkir.table[i]
        while current is not None:
            if nomor in current.value["plat"]:
                return parkir.remove_key(current.key)
            current = current.next
    return False

def main():
    parkir = HashMapSeparateChaining()
    parkir.insert(plat_ke_angka("BE1234AB"), {"plat": "BE1234AB", "pemilik": "atta",  "jam_masuk": "08:15"})
    parkir.insert(plat_ke_angka("BE5678CD"), {"plat": "BE5678CD", "pemilik": "vina",  "jam_masuk": "08:42"})
    parkir.insert(plat_ke_angka("BG9012EF"), {"plat": "BG9012EF", "pemilik": "adel",  "jam_masuk": "09:05"})
    parkir.insert(plat_ke_angka("BE1314GH"), {"plat": "BE1314GH", "pemilik": "naila", "jam_masuk": "09:30"})
    parkir.insert(plat_ke_angka("BE1516IJ"), {"plat": "BE1516IJ", "pemilik": "alin",  "jam_masuk": "10:00"})
    parkir.display()

    nomor_cari = input("\nMasukkan nomor BE yang dicari (contoh: 1234): ")
    hasil = cari_plat_by_nomor(parkir, nomor_cari)
    if hasil is not None:
        print("Kendaraan ditemukan: " + hasil.value["plat"] + " milik " + hasil.value["pemilik"] + " masuk pada jam " + hasil.value["jam_masuk"])
    else:
        print("Kendaraan tidak ditemukan")

    nomor_keluar = input("\nMasukkan nomor BE yang keluar (contoh: 1234): ")
    hasil_keluar = cari_plat_by_nomor(parkir, nomor_keluar)
    if hasil_keluar is not None:
        plat_lengkap = hasil_keluar.value["plat"]
        parkir.remove_key(plat_ke_angka(plat_lengkap))
        print(plat_lengkap + " berhasil keluar")
    else:
        print(nomor_keluar + " tidak ditemukan")

    print("\nSetelah kendaraan keluar:")
    parkir.display()

if __name__ == "__main__":
    main()

class Node:
    def __init__(self, judul, genre):
        self.judul = judul
        self.genre = genre
        self.left = None
        self.right = None

class BSTFilm:
    def __init__(self):
        self.root = None

    def insert_node(self, root, judul, genre):
        if root is None:
            return Node(judul, genre)
        if judul.lower() < root.judul.lower():
            root.left = self.insert_node(root.left, judul, genre)
        elif judul.lower() > root.judul.lower():
            root.right = self.insert_node(root.right, judul, genre)
        else:
            print(f"Anime '{judul}' sudah ada di katalog.")
        return root

    def insert(self, judul, genre):
        self.root = self.insert_node(self.root, judul, genre)

    def delete_node(self, root, judul):
        if root is None:
            return None
        if judul.lower() < root.judul.lower():
            root.left = self.delete_node(root.left, judul)
        elif judul.lower() > root.judul.lower():
            root.right = self.delete_node(root.right, judul)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            successor = root.right
            while successor.left is not None:
                successor = successor.left
            root.judul = successor.judul
            root.genre = successor.genre
            root.right = self.delete_node(root.right, successor.judul)
        return root

    def delete(self, judul):
        if self.search_judul(judul) is None:
            print(f"Anime '{judul}' tidak ditemukan.")
            return
        self.root = self.delete_node(self.root, judul)
        print(f"Anime '{judul}' berhasil dihapus.")

    def search_judul_node(self, root, judul):
        if root is None:
            return None
        if judul.lower() == root.judul.lower():
            return root
        if judul.lower() < root.judul.lower():
            return self.search_judul_node(root.left, judul)
        return self.search_judul_node(root.right, judul)

    def search_judul(self, judul):
        return self.search_judul_node(self.root, judul)

    def search_genre_node(self, root, genre, hasil):
        if root is None:
            return
        self.search_genre_node(root.left, genre, hasil)
        if root.genre.lower() == genre.lower():
            hasil.append(root)
        self.search_genre_node(root.right, genre, hasil)

    def search_genre(self, genre):
        hasil = []
        self.search_genre_node(self.root, genre, hasil)
        return hasil

    def inorder(self, root, hasil):
        if root is None:
            return
        self.inorder(root.left, hasil)
        hasil.append(root)
        self.inorder(root.right, hasil)

    def count_nodes(self, root):
        if root is None:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

def cetak_header_tabel():
    print(f"\n {'JUDUL':<25} {'GENRE':<15}")

def cetak_baris(no, node):
    print(f" {node.judul:<25} {node.genre:<15}")

def main():
    bst = BSTFilm()

    pilih = 0
    while pilih != 7:
        print("BST Katalog anime")
        print("1. Masukan anime")
        print("2. Hapus anime")
        print("3. Cari anime berdasarkan judul")
        print("4. Cari anime berdasarkan genre")
        print("5. Urut judul A-Z")
        print("6. Jumlah anime")
        print("7. Keluar")

        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            try:
                judul = input("Judul anime  : ")
                genre = input("Genre       : ")
                bst.insert(judul, genre)
                print(f"Anime '{judul}' berhasil ditambahkan.")
            except ValueError:
                print("Input tidak valid!")

        elif pilih == 2:
            judul = input("Masukkan judul anime yang ingin dihapus: ")
            bst.delete(judul)

        elif pilih == 3:
            judul = input("Masukkan judul anime: ")
            hasil = bst.search_judul(judul)
            if hasil:
                cetak_header_tabel()
                cetak_baris(1, hasil)
            else:
                print(f"Anime '{judul}' tidak ditemukan.")

        elif pilih == 4:
            genre = input("Masukkan genre anime: ")
            hasil = bst.search_genre(genre)
            if hasil:
                print(f"\n  Ditemukan {len(hasil)} anime dengan genre '{genre}':")
                cetak_header_tabel()
                for i, node in enumerate(hasil, 1):
                    cetak_baris(i, node)
            else:
                print(f"Tidak ada anime dengan genre '{genre}'.")

        elif pilih == 5:
            hasil = []
            bst.inorder(bst.root, hasil)
            if hasil:
                print(f"\n  Daftar anime urut A-Z ({len(hasil)} anime):")
                cetak_header_tabel()
                for i, node in enumerate(hasil, 1):
                    cetak_baris(i, node)
            else:
                print("Katalog kosong.")

        elif pilih == 6:
            print(f"Jumlah anime dalam katalog: {bst.count_nodes(bst.root)}")

        elif pilih == 7:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()

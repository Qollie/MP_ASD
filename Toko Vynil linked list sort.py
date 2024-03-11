class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class VinylRecord:
    def __init__(self, id, judul, artis, genre, tahunRilis, harga):
        self.id = id
        self.judul = judul
        self.artis = artis
        self.genre = genre
        self.tahunRilis = tahunRilis
        self.harga = harga

class VinylStore:
    def __init__(self):
        self.head = None

    def create(self, vinyl_record):
        new_node = Node(vinyl_record)
        new_node.next = self.head
        self.head = new_node

    def createAtEnd(self, vinyl_record):
        new_node = Node(vinyl_record)
        if not self.head:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def createAtIndex(self, index, vinyl_record):
        new_node = Node(vinyl_record)
        if index == 0:
            self.create(vinyl_record)
            return
        current_node = self.head
        for _ in range(index - 1):
            if not current_node:
                print("Indeks", index, "melebihi batas linked list")
                return
            current_node = current_node.next
        if not current_node:
            print("Indeks", index, "melebihi batas linked list")
            return
        new_node.next = current_node.next
        current_node.next = new_node

    def read(self):
        current_node = self.head
        while current_node:
            print(f"ID: {current_node.data.id}")
            print(f"Judul: {current_node.data.judul}")
            print(f"Artis: {current_node.data.artis}")
            print(f"Genre: {current_node.data.genre}")
            print(f"Tahun Rilis: {current_node.data.tahunRilis}")
            print(f"Harga: Rp{current_node.data.harga}\n")
            current_node = current_node.next

    def delete(self):
        if not self.head:
            print("Linked list kosong")
            return

        self.head = self.head.next

    def deleteAtEnd(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        current_node.next = None

    def deleteAtIndex(self, index):
        if index == 0:
            if self.head:
                self.head = self.head.next
            else:
                print("Linked list kosong")
            return

        current_node = self.head
        prev_node = None
        for _ in range(index):
            if not current_node:
                print("Indeks", index, "melebihi batas linked list")
                return
            prev_node = current_node
            current_node = current_node.next
        if not current_node:
            print("Indeks", index, "melebihi batas linked list")
            return
        prev_node.next = current_node.next

    def quickSort(self, arr, key):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        less = [x for x in arr if getattr(x.data, key) < getattr(pivot.data, key)]
        equal = [x for x in arr if getattr(x.data, key) == getattr(pivot.data, key)]
        greater = [x for x in arr if getattr(x.data, key) > getattr(pivot.data, key)]
        return self.quickSort(less, key) + equal + self.quickSort(greater, key)

    def getList(self):
        current_node = self.head
        arr = []
        while current_node:
            arr.append(current_node)
            current_node = current_node.next
        return arr

    def sortIdAscend(self):
        arr = self.getList()
        arr = self.quickSort(arr, 'id')
        self.head = arr[0]
        for i in range(len(arr)-1):
            arr[i].next = arr[i+1]
        arr[-1].next = None

    def sortTitleAscend(self):
        arr = self.getList()
        arr = self.quickSort(arr, 'judul')
        self.head = arr[0]
        for i in range(len(arr)-1):
            arr[i].next = arr[i+1]
        arr[-1].next = None

store = VinylStore()
while True:
    print("\nMenu:")
    print("1. Tambah Vinyl")
    print("2. Lihat Daftar Vinyl")
    print("3. Hapus Vinyl")
    print("4. Menu Sort Vinyl")
    print("5. Keluar")
    pilih = int(input("Pilih operasi yang ingin Anda lakukan: "))

    if pilih == 1:
        print("1. Tambah Vynil di Awal")
        print("2. Tambah Vinyl di Akhir")
        print("3. Tambah Vinyl di Indeks Tertentu")
        pilihCreate = int(input("Pilih operasi yang ingin Anda lakukan: "))

        if pilihCreate == 1:
            id = int(input("Masukkan ID Vinyl: "))
            judul = input("Masukkan Judul: ")
            artis = input("Masukkan Artis: ")
            genre = input("Masukkan Genre: ")
            tahunRilis = int(input("Masukkan Tahun Rilis: "))
            harga = int(input("Masukkan Harga: "))
            vinylBaru = VinylRecord(id, judul, artis, genre, tahunRilis, harga)
            store.create(vinylBaru)

        elif pilihCreate == 2:
            id = int(input("Masukkan ID Vinyl: "))
            judul = input("Masukkan Judul: ")
            artis = input("Masukkan Artis: ")
            genre = input("Masukkan Genre: ")
            tahunRilis = int(input("Masukkan Tahun Rilis: "))
            harga = int(input("Masukkan Harga: "))
            vinylBaru = VinylRecord(id, judul, artis, genre, tahunRilis, harga)
            store.createAtEnd(vinylBaru)

        elif pilihCreate == 3:
            index = int(input("Masukkan indeks: "))
            id = int(input("Masukkan ID Vinyl: "))
            judul = input("Masukkan Judul: ")
            artis = input("Masukkan Artis: ")
            genre = input("Masukkan Genre: ")
            tahunRilis = int(input("Masukkan Tahun Rilis: "))
            harga = int(input("Masukkan Harga: "))
            vinylBaru = VinylRecord(id, judul, artis, genre, tahunRilis, harga)
            store.createAtIndex(index, vinylBaru)

    elif pilih == 2:
        print("\nDaftar Vinyl:")
        store.read()

    elif pilih == 3:
        print("1. Hapus Vynil di Awal")
        print("2. Hapus Vinyl di Akhir")
        print("3. Hapus Vinyl di Indeks Tertentu")
        pilihDelete = int(input("Pilih operasi yang ingin Anda lakukan: "))
        
        if pilihDelete == 1:
            store.delete()

        elif pilih == 2:
            store.deleteAtEnd()

        elif pilih == 3:
            index = int(input("Masukkan indeks: "))
            store.deleteAtIndex(index)

    elif pilih == 4:
        print("1. Urutkan berdasarkan ID (Ascending)")
        print("2. Urutkan berdasarkan Judul (Ascending)")
        sort_choice = int(input("Pilih jenis sorting: "))

        if sort_choice == 1:
            store.sortIdAscend()
            print("Data telah diurutkan berdasarkan ID secara ascending.")

        elif sort_choice == 2:
            store.sortTitleAscend()
            print("Data telah diurutkan berdasarkan Judul secara ascending.")

    elif pilih == 5:
        break

    else:
        print("Pilihan tidak ada, silahkan pilih antara 1-8.")

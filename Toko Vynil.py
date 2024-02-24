class VinylRecord:
    def __init__(self, Id, Judul, Artis, Genre, TahunRilis, Harga):
        self.Id = Id
        self.Judul = Judul
        self.Artis = Artis
        self.Genre = Genre
        self.TahunRilis = TahunRilis
        self.Harga = Harga



class VinylStore:
    def __init__(self):
        self.Records = []

        vinyl1 = VinylRecord(1, "Thriller", "Michael Jackson", "Pop", "1982", 47000000)
        vinyl2 = VinylRecord(2, "Kind of blue", "Miles Davis", "Jazz", "2011", 600000)
        vinyl3 = VinylRecord(3, "The Dark Side of the Moon", "Pink Floyd", "Rock", "2016", 650000)

        self.Records.append(vinyl1)
        self.Records.append(vinyl2)
        self.Records.append(vinyl3)

    def Create(self, vinyl_record):
        for vinyl in self.Records:
            if vinyl.Id == vinyl_record.Id:
                print("ID yang baru sudah ada, penambahan gagal.")
                return
        self.Records.append(vinyl_record)
        print("Vinyl berhasil ditambahkan!")

    def Read(self):
        for vinyl in self.Records:
            print(f"ID: {vinyl.Id}")
            print(f"Judul: {vinyl.Judul}")
            print(f"Artis: {vinyl.Artis}")
            print(f"Genre: {vinyl.Genre}")
            print(f"Tahun Rilis: {vinyl.TahunRilis}")
            print(f"Harga: Rp{vinyl.Harga}\n")

    def Update(self, Id, vinyl_record):
        for i, vinyl in enumerate(self.Records):
            if vinyl.Id == Id:
                self.Records[i] = vinyl_record
                break

    def Delete(self, Id):
        for i, vinyl in enumerate(self.Records):
            if vinyl.Id == Id:
                del self.Records[i]
                break



store = VinylStore()
while True:
    print("\nMenu:")
    print("1. Tambah Vinyl")
    print("2. Lihat Daftar Vinyl")
    print("3. Update Vinyl")
    print("4. Hapus Vinyl")
    print("5. Keluar")
    pilih = int(input("Pilih operasi yang ingin Anda lakukan: "))

    if pilih == 1:
        Id = int(input("Masukkan ID Vinyl: "))
        Judul = input("Masukkan Judul: ")
        Artis = input("Masukkan Artis: ")
        Genre = input("Masukkan Genre: ")
        TahunRilis = int(input("Masukkan Tahun Rilis: "))
        Harga = int(input("Masukkan Harga: "))
        vinylBaru = VinylRecord(Id, Judul, Artis, Genre, TahunRilis, Harga)
        store.Create(vinylBaru)

    elif pilih == 2:
        print("\nDaftar Vinyl:")
        store.Read()

    elif pilih == 3:
        Id = input("Masukkan ID Vinyl yang ingin diupdate: ")
        Judul = input("Masukkan Judul baru: ")
        Artis = input("Masukkan Artis baru: ")
        Genre = input("Masukkan Genre baru: ")
        TahunRilis = int(input("Masukkan Tahun Rilis baru: "))
        Harga = int(input("Masukkan Harga baru: "))
        updateVinyl = VinylRecord(Id, Judul, Artis, Genre, TahunRilis, Harga)
        store.Update(Id, updateVinyl)
        print("\nVinyl berhasil diupdate")

    elif pilih == 4:
        Id = int(input("Masukkan ID Vinyl yang ingin dihapus: "))
        store.Delete(Id)
        print("Vinyl berhasil dihapus")

    elif pilih == 5:
        break

    else:
        print("Pilihan tidak ada, silahkan pilih antara 1-5.")

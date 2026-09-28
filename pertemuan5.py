class Kendaraan:
    def __init__(self, merk, nomor, jenis, harga):
        self.merk = merk
        self.nomor = nomor
        self.jenis = jenis
        self.harga = harga

    def hitung_sewa(self, hari):
        return self.harga * hari

    def tampilkan_data(self, hari):
        total = self.hitung_sewa(hari)

        print("Merk       :", self.merk)
        print("Nomor      :", self.nomor)
        print("Jenis      :", self.jenis)
        print("Harga/Hari :", self.harga)
        print("Lama Sewa  :", hari, "hari")
        print("Total Sewa :", total)
        print("-" * 30)


# Membuat objek kendaraan
kendaraan1 = Kendaraan("Toyota Avanza", "S 1111 BM", "Mobil", 300000)
kendaraan2 = Kendaraan("Honda Brio", "S 5678 CD", "Mobil", 250000)
kendaraan3 = Kendaraan("Honda Vario", "S 9012 EF", "Motor", 100000)

# Menampilkan data rental
kendaraan1.tampilkan_data(2)
kendaraan2.tampilkan_data(3)
kendaraan3.tampilkan_data(4)
# Membuat kelas Mahasiswa yang memiliki atribut nama, npm, dan jurusan. 
class Mahasiswa:
    def __init__(self, nama, npm, jurusan):
        self.nama = nama
        self.npm = npm
        self.jurusan = jurusan

# Metode __init__ digunakan untuk menginisialisasi atribut-atribut ini saat objek Mahasiswa dibuat.

    def tampilkan_info(self):
        print("Nama Mahasiswa:", self.nama)
        print("NPM:", self.npm)
        print("Jurusan:", self.jurusan.NamaJurusan)
 
# Metode tampilkan_info digunakan untuk menampilkan informasi lengkap tentang seorang mahasiswa.

# Membuat kelas Jurusan yang memiliki atribut NamaJurusan dan DaftarMahasiswa.
class Jurusan:
    def __init__(self, nama_jurusan):
        self.NamaJurusan = nama_jurusan
        self.DaftarMahasiswa = []

# Metode __init__ digunakan untuk menginisialisasi atribut-atribut ini saat objek Jurusan dibuat. 
    
    def tambah_mahasiswa(self, mahasiswa):
        self.DaftarMahasiswa.append(mahasiswa)

# Metode tambah_mahasiswa digunakan untuk menambahkan objek Mahasiswa ke dalam DaftarMahasiswa jurusan.

    def tampilkan_daftar_mahasiswa(self):
        print("Daftar Mahasiswa di Jurusan", self.NamaJurusan, " :")
        print("")
        for mahasiswa in self.DaftarMahasiswa:
            print("Nama :", mahasiswa.nama)
            print("NPM  :", mahasiswa.npm)
            print("")

# Metode tampilkan_daftar_mahasiswa digunakan untuk menampilkan daftar mahasiswa yang terdaftar 
# dalam jurusan beserta informasi nama dan NIM mereka.

# Membuat kelas Universitas yang memiliki atribut NamaUniversitas dan DaftarJurusan.
class Universitas:
    def __init__(self, nama_universitas):
        self.NamaUniversitas = nama_universitas
        self.DaftarJurusan = []

# Metode __init__ digunakan untuk menginisialisasi atribut-atribut ini saat objek Universitas dibuat. 

    def tambah_jurusan(self, jurusan):
        self.DaftarJurusan.append(jurusan)

# Metode tambah_jurusan digunakan untuk menambahkan objek Jurusan ke dalam DaftarJurusan universitas. 

    def tampilkan_daftar_jurusan(self):
        print("Daftar Jurusan di Universitas", self.NamaUniversitas, " :")
        for jurusan in self.DaftarJurusan:
            print(jurusan.NamaJurusan)
        print("")

# Metode tampilkan_daftar_jurusan digunakan untuk menampilkan daftar jurusan yang ada di universitas.

# Membuat objek Universitas dengan nama "XYZ University"
universitas_xyz = Universitas("XYZ University")

# Membuat objek Jurusan dengan nama "Teknik Informatika" dan menambahkannya ke dalam Universitas XYZ
jurusan_1 = Jurusan("Informatika")
universitas_xyz.tambah_jurusan(jurusan_1)

# Membuat objek Mahasiswa dengan nama, NPM
mahasiswa_1 = Mahasiswa("Zahrah Hafizah Fakhri", "G1A022046", jurusan_1)
mahasiswa_2 = Mahasiswa("Riolan Pratama", "G1A022047", jurusan_1)
mahasiswa_3 = Mahasiswa("Neli Agustin", "G1A022048", jurusan_1)
mahasiswa_4 = Mahasiswa("M Febri Ardiansyah", "G1A022049", jurusan_1)

# Memasukkannya ke dalam Jurusan Teknik Informatika di Universitas XYZ
jurusan_1.tambah_mahasiswa(mahasiswa_1)
jurusan_1.tambah_mahasiswa(mahasiswa_2)
jurusan_1.tambah_mahasiswa(mahasiswa_3)
jurusan_1.tambah_mahasiswa(mahasiswa_4)

# Menampilkan daftar jurusan yang ada di Universitas XYZ
universitas_xyz.tampilkan_daftar_jurusan()

# Menampilkan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Informatika di Universitas XYZ
jurusan_1.tampilkan_daftar_mahasiswa()
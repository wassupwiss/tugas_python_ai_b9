"""
list-akses dan manipulasi
"""
#membuat list dengan elemen campuran
data = ["puppy", 1, "cat", 2, "bird", 3, 4, "tiger"]

print("list awal:", data)

#akses elemen
print("\nselemen pertama:", data[0])
print("elemen terakhir:", data[7])

#slicing (start:stop:step)
print("slicing data(::2):", data[::2])   #start di indeks 0, stop di indeks terakhir, lompat 2
print("slicing data(::2):", data[0:8:2])   #start di indeks 0, stop di indeks terakhir, lompat 2
print("slicing data(1:7:1):", data[1:7:1])   #start di indeks 1, stop di indeks sebelum 7, lompat 1

#manipulasi list
print("\nsebelum manipulasi:", data)

#menambahkan elemen di akhir list
data.append("moth")
print("setelah append 'moth':", data)

#menyisipkan elemen di indeks ke-2
data.insert(2, "8")
print("setelah insert(2, '8'):", data)

#menambahkan banyak elemen sekaligus
data.extend([100, "snake", "bunny"])
print("setelah extend([100, 'snake', 'bunny']):", data)

#menghapus elemen terakhir dengan pop()
data.pop()
print("setelah pop():", data)

#menghapus elemen tertentu dengan remove()
data.remove(3)
print("setelah remove('3'):", data)

"""
tuple-immutability dan unpacking
"""
#membuat tuple dengan 5 elemen atau lebih
data = ("book", "pen", 12, "mouse", 6, 15, "ruler")
print("\ntuple:", data)

#panjang tuple
print("\npanjang tuple:", len(data))

#akses elemen berdasarkan indeks
print("elemen pertama:", data[0])
print("elemen terakhir:", data[6])
print("elemen ke-3:", data[2])

#unpacking tuple ke dalam variabel
data1, data2, *sisanya = data
print("pertama:", data1)
print("kedua:", data2)
print("sisanya:", sisanya)

#contoh unpacking 3 variabel saja
a, b, c, *rest = data
print("a:", a)
print("b:", b)
print("c:", c)
print("rest:", rest)

"""
Set-keunikan & operasi himpunan
"""
#membuat dua set dengan elemen yang tumpang tindih
set_a = {1, 2, 3, 4, 5, 5, 3, 2, 6}
set_b = {4, 5, 6, 7, 8, 8, 6, 10, 9, 2}
print("\nset A:", set_a)
print("set B:", set_b)

#union (gabungan)
print("\nunion (A | B):", set_a | set_b)

#intersection (irisan)
print("intersection (A & B):", set_a & set_b)

#difference (A - B)
print("difference (A - B):", set_a - set_b)
print("difference (B - A):", set_b - set_a)

#symmetric difference (elemen yang berbeda di A dan B)
print("symmetric difference (A ^ B):", set_a ^ set_b)

"""
dictionary-key/value dasar
"""
#membuat dictionary mahasiswa
mahasiswa = {
    "nama": "Louis Angelica",
    "nim": "2321038",
    "angkatan": 2023,
    "kota": "Bintan"
}

print("\ndata mahasiswa baru:", mahasiswa)

#tambah key baru
mahasiswa["program studi"] = "sistem informasi"
print("\nsetelah tambah key 'prodi':", mahasiswa)

#ubah nilai key
mahasiswa["kota"] = "Batam"
print("setelah ubah key 'kota':", mahasiswa)

#hapus key
del mahasiswa["angkatan"]
print("setelah hapus key 'angkatan':", mahasiswa)

#menampilkan keys(), values(), items()
print("\nkeys:", mahasiswa.keys())
print("values:", mahasiswa.values())
print("items:", mahasiswa.items())

#iterasi menampilkan key: value
print("iterasi dictionary:")
for key, value in mahasiswa.items():
    print(f"{key}: {value}")

"""
nested structures
"""
#list berisi dictionary (nested structure)
mahasiswa_list = [
    {"nama mahasiswa": "Louis Angelica", "NIM": 232323, "prodi": "SI"},
    {"nama mahasiswa": "Ayudya putri Arini", "NIM": 232424, "prodi": "SI"},
    {"nama mahasiswa": "Fathimah Nurnailah Mahira", "NIM": 232525, "prodi": "SI"},
    {"nama mahasiswa": "Yoon Jeonghan", "NIM": 232626, "prodi": "TK"},
    {"nama mahasiswa": "Deardo", "NIM": 232727, "prodi": "TK"},
    {"nama mahasiswa": "Zulkifli", "NIM": 232828, "prodi": "SI"}
]

#cetak semua nama mahasiswa dengan loop
print("\ndaftar nama mahasiswa:")
for mahasiswa in mahasiswa_list:
    print("-", mahasiswa["nama mahasiswa"])

#filter prodi mahasiswa >= prodi tertentu
prodi = "TK"
prodi_teknik = [mahasiswa for mahasiswa in mahasiswa_list if mahasiswa["prodi"] == prodi]

print(f"\nmahasiswa prodi= {prodi}:")
for mahasiswa in prodi_teknik:
    print(f"- {mahasiswa['nama mahasiswa']} ({mahasiswa['prodi']})")

prodi = "SI"
prodi_teknik = [mahasiswa for mahasiswa in mahasiswa_list if mahasiswa["prodi"] == prodi]

print(f"\nmahasiswa prodi= {prodi}:")
for mahasiswa in prodi_teknik:
    print(f"- {mahasiswa['nama mahasiswa']} ({mahasiswa['prodi']})")

"""
# List berisi dictionary (nested structure)
buku_list = [
    {"judul": "Python untuk Pemula", "penulis": "Andi", "tahun": 2019},
    {"judul": "Algoritma dan Struktur Data", "penulis": "Budi", "tahun": 2021},
    {"judul": "Kecerdasan Buatan", "penulis": "Citra", "tahun": 2023},
    {"judul": "Basis Data Modern", "penulis": "Dewi", "tahun": 2020}
]

# Cetak semua judul dengan loop
print("Daftar Judul Buku:")
for buku in buku_list:
    print("-", buku["judul"])

# Filter buku terbit >= tahun tertentu
tahun_min = 2021
buku_modern = [buku for buku in buku_list if buku["tahun"] >= tahun_min]

print(f"\nBuku terbit >= {tahun_min}:")
for buku in buku_modern:
    print(f"{buku['judul']} ({buku['tahun']})")
"""

"""
comprehension & utilitas
"""
#list comprehension
angka = list(range(1, 21))
print("\ndaftar angka:", angka)
list_genap = [x for x in angka if x % 2 == 0]
list_kuadrat = [x**2 for x in angka]
list_kuadrat_antara_1_sampai_20 = [x for x in angka if int(x**0.5)**2 == x]

print("list genap:", list_genap)
print("list kuadrat:", list_kuadrat)
print("list kuadrat antara 1–20:", list_kuadrat_antara_1_sampai_20)

#dict comprehension
dict_paritas = {x: ("genap" if x % 2 == 0 else "ganjil") for x in range(1, 11)}

print("\nmapping genap/ganjil:", dict_paritas)
# user input
n = int(input("masukkan angka antara 1-10: "))

# dict comprehension untuk buat mapping angka -> "genap"/"ganjil"
status = {x: ("genap" if x % 2 == 0 else "ganjil") for x in range(1, 11)}

# cek hasil berdasarkan input user
print(f"{n} adalah bilangan {status[n]}")

# set comprehension
kalimat = "STUDI INDEPENDEN SERU!"
huruf_unik = {ch.lower() for ch in kalimat if ch.isalpha()}

print("Huruf unik:", huruf_unik)

"""
keanggotaan & pencarian sederhana
"""
#cek keanggotaan
data = ["uang", "harimau", 6, "kancil", 12, "dompet"]
print("\ndata", data)
print("uang" in data)
print("boneka" in data)
#indeks
buah = ["apel", "mangga", "jeruk", "anggur"]
posisi = buah.index("jeruk")
print("Posisi 'jeruk':", posisi)
#in dan indeks
item = "rambutan"

if item in buah:
    print(f"{item} ada di posisi {buah.index(item)}")
else:
    print(f"{item} tidak ditemukan")


"""
no 1
"""
#string (variabel/characters)
nama = "Louis Angelica"
print(nama)
umur = "umur gak ada yang tau"
print(umur)
hobi = "tidur"
print(hobi)

#integer (bilangan bulat)
tahun_lahir = 2003
print(tahun_lahir)
ukuran_sepatu = 37
print(ukuran_sepatu)

#float (bilangan desimal)
nilai_pi = 3.14159
print(nilai_pi)

#boolean (true or false)
do_louis_admire_dodo = True
print(do_louis_admire_dodo)

#list (array)
hal_yang_disuka = ["biru", "dodo", "jeonghan", "roblox"]
print(hal_yang_disuka[0])
print(hal_yang_disuka[1])

"""
no 2
"""
#menggabungkan string
first_name = "Louis"
last_name = "Angelica"
full_name = first_name + " " + last_name
print("Hallo, saya ", full_name)

#menghitung panjang string
panjang = len(full_name)
print("Jumlah karakter dalam nama lengkap:", panjang)

#mengubah huruf menjadi besar
print("CAPITAL: ", full_name.upper())

#mengubah huruf menjadi kecil
print("lowercase", full_name.lower())

#menggabungkan string dengan angka (harus diubah ke string dulu)
umur = 20
print("Umur saya " + str(umur) + " tahun")

"""
no 3
"""
#operasi matematika sederhana
#variabel
x = 8
y = 2

#penjumlahan
print("Penjumlahan:", x + y)

#pengurangan
print("Pengurangan:", x - y)

#perkalian dan perpangkatan
print("Perkalian:", x * y)
print("Pangkat:", x ** y)

#pembagian (hasil float)
print("Pembagian:", x / y)

#pembagian bulat (floor division)
print("Pembagian bulat:", x // y)

#sisa bagi (modulus)
print("Sisa bagi:", x % y)

"""
no 4
"""
#membuat list dengan 5 item
fav_things = ["sleep", "roblox", "mangga", "Dodo", "Jeonghan"]

#menampilkan list
print("List of Louis's favorite things:", fav_things)

#mengakses elemen tertentu (indeks mulai dari 0)
print("Favorite thing pertama:", fav_things[0])
print("Favorite thing kedua:", fav_things[1])
print("Favorite thing terakhir:", fav_things[4]) #indeks positif
print("Favorite thing terakhir:", fav_things[-1]) #indeks negatif


#menambahkan item baru ke list
fav_things.append("blue")
print("Setelah menambahkan blue:", fav_things)

#menghapus item dengan remove()
fav_things.remove("Dodo")
print("Setelah menghapus Dodo:", fav_things)

#menghapus item dengan pop() (hapus berdasarkan indeks)
fav_things.pop(1)  # menghapus item pada indeks ke-1
print("Setelah menghapus indeks ke-1:", fav_things)

"""
no 5
"""
#meminta input dari user
nama = input("Insert your name: ")
umur = input("Insert your age: ")

# Menampilkan kalimat perkenalan
print("Halo, nama saya " + nama + " dan umur saya " + umur + " tahun.")

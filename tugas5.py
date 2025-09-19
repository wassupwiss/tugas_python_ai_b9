"""
function
"""
#fungsi sapaan
def greet(nama: str) -> str:
    return f"Halo, {nama}! How's everything?"

#fungsi penjumlahan
def tambah(a: float, b: float = 0.0) -> float:
    return a + b

#fungsi rata-rata
def rata_rata(angka: list[float]) -> float:
    if not angka:   #kalau list kosong
        return 0.0
    return round(sum(angka) / len(angka), 2)  #dibulatkan 2 angka di belakang koma

# 1. Sapaan
nama_user = input("Masukkan nama Anda: ")
print(greet(nama_user))

# 2. Penjumlahan
a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua (boleh kosong, tekan Enter): ") or 0)
print("Hasil penjumlahan:", tambah(a, b))

# 3. Rata-rata
n = int(input("Mau masukin berapa angka untuk dihitung rata-rata? "))
daftar_angka = []
for i in range(n):
    nilai = float(input(f"Masukkan angka ke-{i+1}: "))
    daftar_angka.append(nilai)

print("Rata-rata:", rata_rata(daftar_angka))

"""
class
"""
def rata_rata(angka: list[float]) -> float:
    if not angka:
        return 0.0
    return round(sum(angka) / len(angka), 2)

class Student:
    def __init__(self, nama: str, nim: str):
        self.nama = nama
        self.nim = nim
        self.nilai: list[float] = []  # list kosong awalnya

    def tambah_nilai(self, skor: float) -> None:
        self.nilai.append(skor)

    def rata_nilai(self) -> float:
        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0) -> str:
        return "LULUS" if self.rata_nilai() >= threshold else "TIDAK LULUS"

    def __str__(self) -> str:
        return f"Student(nama='{self.nama}', nim='{self.nim}', rata={self.rata_nilai()}, status={self.status()})"

# --- Contoh Pemakaian ---
#mhs = Student("Budi", "A123")
#mhs.tambah_nilai(80)
#mhs.tambah_nilai(85)
#mhs.tambah_nilai(83)
#print(mhs)

nama = input("Masukkan nama mahasiswa: ")
nim = input("Masukkan NIM mahasiswa: ")

mhs = Student(nama, nim)

jumlah_nilai = int(input("Mau masukkan berapa nilai? "))
for i in range(jumlah_nilai):
    skor = float(input(f"Masukkan nilai ke-{i+1}: "))
    mhs.tambah_nilai(skor)

print("\n--- Data Mahasiswa ---")
print(mhs)

"""
demo
"""
def greet(nama: str) -> str:
    return f"Halo, {nama}!"

def tambah(a: float, b: float = 0.0) -> float:
    return a + b

def rata_rata(angka: list[float]) -> float:
    if not angka:
        return 0.0
    return round(sum(angka) / len(angka), 2)


class Student:
    def __init__(self, nama: str, nim: str):
        self.nama = nama
        self.nim = nim
        self.nilai: list[float] = []

    def tambah_nilai(self, skor: float) -> None:
        self.nilai.append(skor)

    def rata_nilai(self) -> float:
        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0) -> str:
        return "LULUS" if self.rata_nilai() >= threshold else "TIDAK LULUS"

    def __str__(self) -> str:
        return f"Student(nama='{self.nama}', nim='{self.nim}', rata-rata={self.rata_nilai()}, status={self.status()})"


# demo program
if __name__ == "__main__":
    print("=== FUNCTIONS ===")
    print(greet("Arifian"))
    print("tambah(5, 7) =", tambah(5, 7))
    print("tambah(10) =", tambah(10))
    print("rata_rata([80, 90, 100]) =", rata_rata([80, 90, 100]))
    print("rata_rata([]) =", rata_rata([]))

    print("\n=== CLASS STUDENT ===")
    mhs1 = Student("Wiss", "SI23")
    mhs1.tambah_nilai(100)
    mhs1.tambah_nilai(100)
    mhs1.tambah_nilai(100)

    mhs2 = Student("Lara", "TI23")
    mhs2.tambah_nilai(60)
    mhs2.tambah_nilai(65)
    mhs2.tambah_nilai(70)

    print(mhs1)
    print("Rata-rata:", mhs1.rata_nilai(), "Status:", mhs1.status())

    print(mhs2)
    print("Rata-rata:", mhs2.rata_nilai(), "Status:", mhs2.status())

"""
import & setup
"""
import numpy as np
import pandas as pd
import os
np.random.seed(42)

"""
numpy- data & statistik
"""
# buat array berisi 10 nilai ujian acak (rentang 50–100)
nilai_ujian = np.random.randint(50, 101, size=10)
print("Array Nilai Ujian:", nilai_ujian)

print("Rata-rata :", np.mean(nilai_ujian))
print("Median    :", np.median(nilai_ujian))
print("Std Dev   :", np.std(nilai_ujian))
print("Nilai Min :", np.min(nilai_ujian))
print("Nilai Max :", np.max(nilai_ujian))

"""
pandas - dataframe
"""
# contoh data mahasiswa
data = {
    "nama": ["Louis", "Ayu", "Nailah", "Jeonghan", "Dino", "Vernon", "Woozi"],
    "nim": ["A001", "A002", "A003", "A004", "A005", "A006", "A007"],
    # ambil 7 nilai pertama dari array numpy
    "nilai": nilai_ujian[:7],
    "angkatan": [2023,2023,2023,2024,2024,2024,2024],
    "prodi": ["SI", "SI", "SI", "TI", "TK", "TI", "TK"]
}

df = pd.DataFrame(data)

# tambah kolom status
df["status"] = df["nilai"].apply(lambda x: "LULUS" if x >= 70 else "TIDAK LULUS")

print("\nDataFrame Mahasiswa:")
print(df.head())

"""
file input/output ringkasan
"""
with open("ringkasan_tugas6.txt", "w", encoding="utf-8") as f:
    f.write("=== RINGKASAN STATISTIK (NumPy) ===\n")
    f.write(f"Rata-rata : {np.mean(nilai_ujian):.2f}\n")
    f.write(f"Median    : {np.median(nilai_ujian):.2f}\n")
    f.write(f"Std Dev   : {np.std(nilai_ujian):.2f}\n")
    f.write(f"Nilai Min : {np.min(nilai_ujian)}\n")
    f.write(f"Nilai Max : {np.max(nilai_ujian)}\n\n")

    f.write("=== RINGKASAN DATAFRAME (pandas) ===\n")
    f.write(f"Jumlah Baris   : {len(df)}\n")
    f.write(f"Jumlah Lulus   : {(df['status'] == 'LULUS').sum()}\n")
    f.write(f"Jumlah Tidak   : {(df['status'] == 'TIDAK LULUS').sum()}\n")

"""
oop sederhana
"""
class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def average(self) -> float:
        """Hitung rata-rata kolom nilai"""
        return self.df["nilai"].mean()

    def pass_rate(self, threshold: float = 70.0) -> float:
        """Hitung persentase mahasiswa yang lulus"""
        total = len(self.df)
        if total == 0:
            return 0.0
        lulus = (self.df["nilai"] >= threshold).sum()
        return (lulus / total) * 100

    def save_summary(self, path: str):
        """Simpan ringkasan statistik ke file txt"""
        with open(path, "a", encoding="utf-8") as f:
            f.write("=== RINGKASAN GRADEBOOK ===\n")
            f.write(f"Jumlah Data   : {len(self.df)}\n")
            f.write(f"Rata-rata     : {self.average():.2f}\n")
            f.write(f"Pass Rate (%) : {self.pass_rate():.2f}%\n\n")

    def __str__(self) -> str:
        return f"GradeBook dengan {len(self.df)} data, Rata-rata Nilai = {self.average():.2f}"
    
"""
demo
"""
if __name__ == "__main__":
    print("=== NUMPY ===")
    print("Array Nilai Ujian:", nilai_ujian)
    print("Rata-rata :", np.mean(nilai_ujian))
    print("Median    :", np.median(nilai_ujian))
    print("Std Dev   :", np.std(nilai_ujian))
    print("Nilai Min :", np.min(nilai_ujian))
    print("Nilai Max :", np.max(nilai_ujian))

    print("\n=== PANDAS ===")
    print(df.head())

    print("\n=== OOP: GRADEBOOK ===")
    gb = GradeBook(df)
    print(gb)  # panggil __str__
    print("Average Nilai :", gb.average())
    print("Pass Rate (%) :", gb.pass_rate())
    gb.save_summary("ringkasan_tugas6.txt")
    print("Ringkasan sudah ditulis ke ringkasan_tugas6.txt")

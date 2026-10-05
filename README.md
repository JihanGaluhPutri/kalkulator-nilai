# Kalkulator Nilai Mahasiswa

Memenuhi Tugas Pertemuan 3 Mata Kuliah Analisis dan Pengujian Sistem.

Mini program Python untuk menghitung nilai akhir mahasiswa dan mengubahnya menjadi grade huruf. Program ini diuji untuk menemukan fault (defect), lalu dianalisis akar penyebabnya (Root Cause Analysis).

## Aturan Program

- Nilai akhir = 30% rata-rata tugas + 30% UTS + 40% UAS
- Grade: A (>= 80), B (>= 70), C (>= 60), D (>= 50), E (< 50)
- Setiap nilai harus berada pada rentang 0 - 100

## Struktur Repository

| File | Isi |
|------|-----|
| `nilai.py` | Program utama (hitung rata-rata tugas, nilai akhir, dan grade) |
| `test_nilai.py` | 7 test case menggunakan `unittest` |
| `defect-log.md` | Daftar fault yang ditemukan beserta RCA-nya |

## Cara Menjalankan

Pastikan Python sudah terpasang, lalu jalankan:

```
python -m unittest -v test_nilai
```

Contoh memakai fungsi secara langsung:

```
python -c "from nilai import hitung_nilai_akhir, tentukan_grade; n = hitung_nilai_akhir([80], 80, 80); print(n, tentukan_grade(n))"
```

Hasil: `80.0 A`

## Ringkasan Hasil Pengujian

Ditemukan **3 fault**:

1. Daftar tugas kosong menyebabkan `ZeroDivisionError` (`rata_rata_tugas`)
2. Nilai 80 mendapat grade B, seharusnya A (`tentukan_grade`)
3. Nilai di luar rentang 0 - 100 diterima (`hitung_nilai_akhir`)

| Kondisi | Hasil test |
|---------|------------|
| Sebelum perbaikan | FAILED (failures=3, errors=1) |
| Sesudah perbaikan | OK (7 dari 7 lulus) |

Detail bukti, Root Cause Analysis, dan perbaikan setiap fault ada di [defect-log.md](defect-log.md).
# Defect Log - Kalkulator Nilai Mahasiswa

Aturan program:
- Nilai akhir = 30% rata-rata tugas + 30% UTS + 40% UAS
- Grade: A (>= 80), B (>= 70), C (>= 60), D (>= 50), E (< 50)
- Setiap nilai harus berada pada rentang 0 - 100

Cara pengujian: `python -m unittest -v test_nilai` (7 test case, library unittest)

- Versi sebelum perbaikan : folder `versi-awal/`
- Versi sesudah perbaikan : folder utama (`nilai.py`)

## Hasil Pengujian

| Test | Skenario | Teknik | Sebelum perbaikan | Sesudah perbaikan |
|------|----------|--------|-------------------|-------------------|
| TC01 | Rata-rata tugas normal | Equivalence partitioning | Lulus | Lulus |
| TC02 | Grade A untuk nilai 90 | Equivalence partitioning | Lulus | Lulus |
| TC03 | Grade A tepat di batas (nilai 80) | Boundary value analysis | FAIL | Lulus |
| TC04 | Daftar tugas kosong | Input tidak valid | ERROR | Lulus |
| TC05 | Nilai negatif | Input tidak valid | FAIL | Lulus |
| TC06 | Nilai lebih dari 100 | Input tidak valid | FAIL | Lulus |
| TC07 | Nilai akhir normal | Equivalence partitioning | Lulus | Lulus |

- Sebelum perbaikan: Ran 7 tests, FAILED (failures=3, errors=1)
- Sesudah perbaikan : Ran 7 tests, OK

---

## Fault 1: Daftar tugas kosong menyebabkan crash

- Fungsi           : rata_rata_tugas
- Test case        : TC04
- Input            : daftar_tugas = []
- Harapan          : pesan error yang jelas (ValueError)
- Hasil aktual     : ZeroDivisionError: division by zero

### RCA (5 Whys)
1. Kenapa program crash? Terjadi pembagian dengan nol.
2. Kenapa dibagi nol? len(daftar_tugas) bernilai 0.
3. Kenapa list kosong bisa masuk? Tidak ada pengecekan sebelum menghitung.
4. Kenapa tidak dicek? Kode mengasumsikan pengguna selalu memberi minimal satu nilai tugas.

- Penyebab langsung : len(daftar_tugas) bernilai 0 sehingga terjadi pembagian dengan nol
- Akar penyebab     : asumsi input tidak dituliskan dan tidak diuji (kasus input kosong
                      tidak dipikirkan)
- Perbaikan         : cek daftar kosong di awal fungsi, lempar ValueError
                      ("Daftar tugas tidak boleh kosong")
- Pencegahan        : validasi input di awal fungsi dan test case untuk input kosong
- Bukti perbaikan   : TC04 berubah dari ERROR menjadi Lulus

---

## Fault 2: Nilai 80 mendapat grade B, seharusnya A

- Fungsi           : tentukan_grade
- Test case        : TC03
- Input            : nilai = 80
- Harapan          : Grade A (aturan: A jika nilai >= 80)
- Hasil aktual     : Grade B ('B' != 'A')

### RCA (5 Whys)
1. Kenapa nilai 80 mendapat B? Kondisi "nilai > 80" bernilai salah untuk 80.
2. Kenapa memakai ">"? Salah memilih operator, aturan meminta ">=".
3. Kenapa tidak ketahuan? Pengujian awal hanya memakai nilai aman seperti 90.

- Penyebab langsung : baris "if nilai > 80" di tentukan_grade
- Akar penyebab     : salah memilih operator pembanding (> bukan >=) dan tidak ada
                      pengujian pada nilai tepat di batas
- Perbaikan         : ubah menjadi "if nilai >= 80"
- Pencegahan        : boundary value analysis (uji 79, 80, 81) dan review kode terhadap aturan
- Bukti perbaikan   : TC03 berubah dari FAIL menjadi Lulus

---

## Fault 3: Nilai di luar rentang 0 - 100 diterima

- Fungsi           : hitung_nilai_akhir
- Test case        : TC05 dan TC06
- Input            : (a) tugas [-10], UTS 70, UAS 80
                     (b) tugas [80], UTS 150, UAS 80
- Harapan          : input di luar rentang 0 - 100 ditolak dengan ValueError
- Hasil aktual     : (a) diterima, keluar 50.0 (D)
                     (b) diterima, keluar 101.0 (A)

### RCA (5 Whys)
1. Kenapa nilai tidak valid diproses? Tidak ada kode yang mengecek rentangnya.
2. Kenapa tidak ada pengecekan? Validasi tidak menjadi tanggung jawab fungsi mana pun.
3. Kenapa itu terjadi? Aturan "0 - 100" hanya tertulis di dokumen, tidak diterapkan ke kode.

- Penyebab langsung : tidak ada kode yang memeriksa rentang nilai sebelum perhitungan
- Akar penyebab     : persyaratan "nilai 0 - 100" hanya tertulis di dokumen, tidak
                      diterapkan ke dalam kode, dan tidak ada bagian yang bertanggung jawab
                      atas validasi
- Perbaikan         : tambah fungsi validasi_nilai yang melempar ValueError jika nilai di luar
                      rentang, dipanggil sebelum perhitungan
- Pencegahan        : validasi di satu tempat yang jelas dan test case untuk nilai negatif,
                      0, 100, dan di atas 100
- Bukti perbaikan   : TC05 dan TC06 berubah dari FAIL menjadi Lulus

---

## Ringkasan

| Fault | Akar penyebab | Kategori | Pencegahan |
|-------|---------------|----------|------------|
| 1 | Asumsi input tidak dituliskan | Kasus tepi tidak ditangani | Validasi input dan test input kosong |
| 2 | Operator > seharusnya >= | Kesalahan logika | Boundary value analysis dan code review |
| 3 | Tidak ada validasi rentang nilai | Persyaratan tidak diterapkan | Validasi terpusat dan test nilai ekstrem |

Kesimpulan: dua dari tiga fault muncul karena kasus tepi (edge case) tidak diuji.
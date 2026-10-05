import unittest

from nilai import hitung_nilai_akhir, rata_rata_tugas, tentukan_grade


class TestKalkulatorNilai(unittest.TestCase):
    def test_TC01_rata_rata_normal(self):
        self.assertEqual(rata_rata_tugas([80, 90, 70]), 80)

    def test_TC02_grade_A_normal(self):
        self.assertEqual(tentukan_grade(90), "A")

    def test_TC03_grade_A_di_batas_80(self):
        self.assertEqual(tentukan_grade(80), "A")

    def test_TC04_daftar_tugas_kosong(self):
        with self.assertRaises(ValueError):
            rata_rata_tugas([])

    def test_TC05_nilai_negatif(self):
        with self.assertRaises(ValueError):
            hitung_nilai_akhir([-10], 70, 80)

    def test_TC06_nilai_lebih_dari_100(self):
        with self.assertRaises(ValueError):
            hitung_nilai_akhir([80], 150, 80)

    def test_TC07_nilai_akhir_normal(self):
        self.assertAlmostEqual(hitung_nilai_akhir([80], 80, 80), 80)


if __name__ == "__main__":
    unittest.main(verbosity=2)
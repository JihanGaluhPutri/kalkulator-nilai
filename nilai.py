BOBOT_TUGAS = 0.3
BOBOT_UTS = 0.3
BOBOT_UAS = 0.4

def validasi_nilai(nilai, nama):
    if nilai < 0 or nilai > 100:
        raise ValueError(f"{nama} harus 0 - 100, bukan {nilai}")

def rata_rata_tugas(daftar_tugas):
    if len(daftar_tugas) == 0:
        raise ValueError("Daftar tugas tidak boleh kosong")
    return sum(daftar_tugas) / len(daftar_tugas)

def hitung_nilai_akhir(daftar_tugas, uts, uas):
    for nilai in daftar_tugas:
        validasi_nilai(nilai, "Nilai tugas")
    validasi_nilai(uts, "Nilai UTS")
    validasi_nilai(uas, "Nilai UAS")
    return (
        rata_rata_tugas(daftar_tugas) * BOBOT_TUGAS
        + uts * BOBOT_UTS
        + uas * BOBOT_UAS
    )

def tentukan_grade(nilai):
    if nilai >= 80:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai >= 60:
        return "C"
    elif nilai >= 50:
        return "D"
    return "E"
BOBOT_TUGAS = 0.3
BOBOT_UTS = 0.3
BOBOT_UAS = 0.4


def rata_rata_tugas(daftar_tugas):
    return sum(daftar_tugas) / len(daftar_tugas)


def hitung_nilai_akhir(daftar_tugas, uts, uas):
    return (
        rata_rata_tugas(daftar_tugas) * BOBOT_TUGAS
        + uts * BOBOT_UTS
        + uas * BOBOT_UAS
    )


def tentukan_grade(nilai):
    if nilai > 80:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai >= 60:
        return "C"
    elif nilai >= 50:
        return "D"
    return "E"
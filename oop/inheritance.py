import classs


class KalkulatorKali(classs.Kalkulator):
    """contoh mewarisi kelas kalkulator sederhana"""

    def kali_angka(self, angka1, angka2):
        self.nilai = angka1 * angka2
        return self.nilai

    # override method
    def tambah_angka(self, angka1, angka2):
        self.nilai = angka1 + angka2
        return self.nilai


kk = KalkulatorKali()
# sesuai dengan definisi class memiliki fitur kali_angka
a = kk.kali_angka(2, 3)
print(a)

# memiliki fitur tambah_angka karena mewarisi dari Kalkulator
b = kk.tambah_angka(5, 6)
print(b)


class KalkulatorTambah(classs.Kalkulator):
    """contoh mewarisi kelas kalkulator sederhana"""

    def tambah_angka(self, angka1, angka2):
        if angka1 + angka2 <= 9:  # fitur ini sudah oke di kelas dasar, gunakan yang ada saja
            # panggil fungsi dari Kalkulator lalu isi nilai
            super().tambah_angka(angka1, angka2)
        else:  # ini adalah fitur baru yang ingin diperbaiki dari keterbatasan kelas dasar
            self.nilai = angka1 + angka2
        return self.nilai


class Employee:
    pass  # definisi calss kosong


aEmployee = Employee()
aEmployee.name = "Bay"
aEmployee.tribe = "Digital"
aEmployee.age = 23

print(aEmployee.name)

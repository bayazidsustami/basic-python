class Kalkulator:
    """contoh kelas kalkulator sederhana"""

    def __init__(self, i=12345):
        self.i = i

    def f(self):
        return 'hello world'

    @classmethod
    def tambah_angka(self, angka1, angka2):
        return "{} + {} = {}".format(angka1, angka2, angka1+angka2)

    @staticmethod
    def kali_angka(angka1, angka2):
        return '{} x {} = {}'.format(angka1, angka2, angka1 * angka2)


# create instance
calc = Kalkulator(i=1024)
print(calc.i)
print(calc.f())
print(calc.tambah_angka(1, 2))
print(Kalkulator.kali_angka(1, 2))

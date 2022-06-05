from audioop import mul
from tkinter.messagebox import NO


def cetak(param1):
    print(param1)
    return


def multiplication(arg1, arg2):
    result = arg1 * arg2
    return result


def ubah(list_saya):
    list_saya.append([1, 2, 3, 4])
    print('Nilai di dalam fungsi: {}'.format(list_saya))


def sebuah_fungsi(a, b, c):
    print("%s, %s, %s" % (a, b, c))
    return None


def daftar(tanggal, bulan, tahun):
    print("Tanggal Lahir {}".format(tanggal, bulan, tahun))
    return


cetak(10)
cetak(20)
print(multiplication(20, 10))

# Panggil fungsi ubah
# pass by reference akan mengubah nilai list baik diluar maupun didalam func
# tetapi jika dilakukan assignment tidak berlaku
new_list = [10, 20, 30]
ubah(new_list)
print('Nilai di luar fungsi: {}'.format(new_list))

# can used named argument
sebuah_fungsi(a=2, b=3, c="oke")

# keyword argument
daftar(tanggal=10, bulan=12, tahun=1999)
daftar(**{'tanggal': 1, 'bulan': 'Januari', 'tahun': 2020})

# positional argument
daftar(1, 'Januari', 2020)
daftar(*(1, 'Januari', 2020))

# positional-or-keyword
# def kali(nilai1, nilai2=None): ...

# positional-only
# def (nilai1, nilai2, /, nilai3): ...

# keyword-only
# def func(arg, *, kw_only1, kw_only2): ...

# var-positional dan var-keyword
# def func(*args, **kwargs): ...


def printinfo(*args, **kwargs):
    for a in args:
        print("argument posisi {}".format(a))
    for key, value in kwargs.items():
        print('argumen kata kunci {}:{}'.format(key, value))


# Panggil printinfo
printinfo()
printinfo(1, 2, 3)
printinfo(i=7, j=8, k=9)
printinfo(1, 2, j=8, k=9)
printinfo(*(2, 3), **{'i': 7, 'j': 8})

# anonymous func
# lambda [arg1 [,arg2,.....argn]]:expression


def add(arg1, arg2): return arg1 + arg2


print("Result : ", add(1, 2))

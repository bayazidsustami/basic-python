# syntax error
# while True print('Hello world')
# File "<stdin>", line 1
#   while True print('Hello world')

z = 0
try:
    x = 1 / z
    print(x)
except ZeroDivisionError:
    print('tidak bisa membagi angka dengan nilai nol')

try:
    with open('contoh_tidak_ada.py') as file:
        print(file.read())
except (FileNotFoundError, ):
    print('file tidak ditemukan')

d = {'ratarata': '10.0'}
try:
    print('rata-rata: {}'.format(d['rata_rata']))
except KeyError:
    print('kunci tidak ditemukan di dictionary')
except ValueError:
    print('nilai tidak sesuai')

try:
    print('rata-rata: {}'.format(d['ratarata']/3))
except KeyError:
    print('kunci tidak ditemukan di dictionary')
except (ValueError, TypeError):
    print('nilai atau tipe tidak sesuai')

try:
    print('pembulatan rata-rata: {}'.format(int(d['ratarata'])))
except (ValueError, TypeError) as e:
    print('penangan kesalahan: {}'.format(e))

d = {'ratarata': '10.0'}
if 'total' not in d:
    raise KeyError('harus memiliki total')

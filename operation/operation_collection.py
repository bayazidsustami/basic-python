from operator import truediv


contoh_list = [1, 3, 3, 5, 5, 5, 7, 7, 9]
print(contoh_list)
print(len(contoh_list))

contoh_set = set([1, 3, 3, 5, 5, 5, 7, 7, 9])
print(contoh_set)
print(len(contoh_set))

contoh_string = "Belajar Python"
print(contoh_string)
print(len(contoh_string))

angka = [13, 7, 24, 5, 96, 84, 71, 11, 38]
print(min(angka))
print(max(angka))

genap = [2, 4, 4, 6, 6, 6, 6, 8, 10, 10]
print(genap.count(6))  # menghitung berapa kali angka 6 muncul
string = "Belajar Python di Dicoding sangat menyenangkan"
substring = "a"
print(string.count(substring))

# gabung
angka = [2, 4, 6, 8]
huruf = ['P', 'Y', 'T', 'H', 'O', 'N']
gabung = angka + huruf
print(gabung)

# replikasi
learn = ['P', 'Y', 'T', 'H', 'O', 'N']
replikasi = learn * 2
print(replikasi)

tujuh = [7]*5
print(len(tujuh))
print(tujuh)

# range
for i in range(5):
    print(i)

print("\n")
# Range dengan 2 parameter n,p: membuat deret bilangan yang dimulai dari n, hingga sebelum p (bilangan p tidak ikut). Sering disebut sebagai inklusif n (deret dimulai bilangan n) dan eksklusif p (deret tidak menyertakan bilangan p).
for i in range(1, 11):
    print(i)

print([_ for _ in range(0, 20, 5)])
# range(n,p,q)
for i in range(1, 11, 2):
    print(i)

# for check if a collection is contains or not
kalimat = "Belajar Python di Dicoding sangat menyenangkan"
print('Dicoding' in kalimat)
print('tidak' in kalimat)
print('Dicoding' not in kalimat)
print('tidak' not in kalimat)

# giving value to variable
data = ['shirt', 'white', 'L']
apparel = data[0]
color = data[1]
size = data[2]

# or
data = ['shirt', 'white', 'L']  # From List
apparel, color, size = data
data = ('shirt', 'white', 'L')  # From Tuple
apparel, color, size = data

# apparel, color, size, price = data #it will be produce error bcs variable count is not same with the list

# switch the value
apparel, color = 'shirt', 'white'
apparel, color = color, apparel
print(apparel)
print(color)

# sorting
angka = [100, 1000, 500, 200, 5]
angka.sort()
print(angka)
angka.sort(reverse=True)
print(angka)

kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort()
print(kendaraan)

# can't do sorting if not spesific type
#urutan = ['Dicoding', 1, 2, 'Indonesia', 3]
# urutan.sort()

# the uppercase will be priorities
kendaraan = ['motor', 'mobil', 'helikopter', 'Pesawat']
kendaraan.sort()
print(kendaraan)
kendaraan.sort(key=str.lower)  # ignore uppercase
print(kendaraan)

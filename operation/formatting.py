# Contoh 1: Penggunaan zfill 5 pada angka satuan
angka = 5
print(str(angka).zfill(5))
# Contoh 2: Penggunaan zfill 5 pada angka ratusan
angka = 300
print(str(angka).zfill(5))
# Contoh 3: Penggunaan zfill 5 pada angka desimal negatif (memiliki koma)
angka = -0.45  # nilai koma dan negatif dihitung
print(str(angka).zfill(5))
# Contoh 4: Penggunaan zfill 7 pada angka desimal negatif (memiliki koma)
angka = -0.45
print(str(angka).zfill(7))

# Contoh 1
kata = 'aku'
print(kata.zfill(5))
# Contoh 2
kata = 'kamu'
print(kata.zfill(5))
# Contoh 3
kata = 'dirinya'
print(kata.zfill(5))

# adjust to right
print('Dicoding'.rjust(20, "*"))
print('Dicoding'.rjust(20))
print('Dicoding'.ljust(20, "*"))
print('Dicoding'.ljust(20))
print('Dicoding'.center(20))
print('Dicoding'.center(20, "-"))

# String literals
# print('jum'at') #it will be produce error
print('jum\'at')  # escape character
print("jum'at")

# list of escape character
# \' Single quote
# \" Double quote
# \t Tab
# \n Newline (line break)
# \\ Backslash

print("Halo!\nKapan terakhir kali kita bertemu?\nKita bertemu hari Jum\'at yang lalu.")

# raw string
print(r'Dicoding\tIndonesia')

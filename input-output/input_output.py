x = 11
print("nilai x adalah", x)

# use string format
print("nilai x adalah {}".format(x))
# or
name = "boys"
print("namanya adalah %s, umur %d" % (name, x))
print("namanya adalah %s" % name)

angka = [7, 9, 11, 13]
print("Angka saya: %s" % angka)

# list of specifier
# %s - String
# %d - Integers
# %f - Bilangan Desimal
# %.<digit>f - Bilangan desimal dengan sejumlah digit angka dibelakang koma.
# %x/%X - Bilangan bulat dalam representasi Hexa (huruf kecil/huruf besar)

# print hexa
a, b = 10, 11
print('10: %x and 11: %X' % (a, b))

# input
inputValue = input("masukkan angka : ")
# if you expect receive int/float, you should convert it to spesific type what you want
print(inputValue)

# input with mathematic expression
mathExpression = input("masukkan ekspressi matematika : ")  # e.g '90+19'
print(eval(mathExpression))

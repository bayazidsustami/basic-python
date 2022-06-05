import sys
for huruf in 'Dicoding':  # Contoh pertama
    print('Huruf: {}'.format(huruf))

flowers = ['mawar', 'melati', 'anggrek']
for flower in flowers:  # Contoh kedua
    print('Flower: {}'.format(flower))

flowers = ['mawar', 'melati', 'anggrek']
for index in range(len(flowers)):  # accessing with index
    print('Flowers: {}'.format(flowers[index]))

count = 0
while (count < 7):
    print('Hitungannya adalah: {}'.format(count))
    count += 1

# produce infinite loop if more than 1
var = 1
while var >= 1:  # This constructs an infinite loop
    num = input('Masukkan angka: ')
    var = int(num)
    print('Anda memasukkan angka: {}'.format(num))


# while True:  # This constructs an infinite loop
#    num = input('Masukkan angka: ')
#    print('Anda memasukkan angka: {}'.format(num))

# nested loop
for i in range(0, 6):
    for j in range(0, 6 - i):
        print('*', end='')
    print()

# handling loop
for huruf in 'Dico ding':
    if huruf == ' ':
        break
    print('Huruf saat ini: {}'.format(huruf))

for i in range(0, 6):
    for j in range(0, 6):
        if j > i:
            print()
            break
        else:
            print("*", end="")
print()
for huruf in 'Dico ding':
    if huruf == ' ':
        continue
    print('Huruf saat ini: {}'.format(huruf))

jumlahbaris = 10
baris = 0
bintang = 0
while baris < jumlahbaris:
    if (bintang) >= (baris+1):
        print()
        baris += 1
        bintang = 0
        continue  # saat masuk ke if, maka bagian print * diluar if tidak akan dijalankan, langsung ulang ke while
    print("*", end="")
    bintang += 1

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n/x)
            break
    else:
        # loop fell through without finding a factor
        print(n, ' adalah bilangan prima')

print()
n = 10
while n > 0:
    n = n - 1
    if n == 7:
        break
    print(n)
else:
    print("Loop selesai")


# pass used to passing the func execution
def aFunction():
    pass


# print("----------------")
#var1 = ""
# while(var1 != "exit"):
#    var1 = input("Please enter an integer (type exit to exit): ")
#    print(int(var1))
print("-----------------")
data = ''
while(data != 'exit'):
    try:
        data = input('Please enter an integer (type exit to exit): ')
        print('got integer: {}'.format(int(data)))
    except:
        if data == 'exit':
            pass  # exit gracefully without prompt any error
        else:
            print('error: {}'.format(sys.exc_info()[0]))

print("--------------")
# Cara 1
angka = [1, 2, 3, 4]
pangkat = []
for n in angka:
    pangkat.append(n**2)
print(pangkat)


# new_list = [expression for_loop_one_or_more conditions]
# Cara 2 List Comprehension
angka = [1, 2, 3, 4]
pangkat = [n**2 for n in angka]
print(pangkat)

# Contoh3 menemukan item yang ada di kedua list
list1 = ['d', 'i', 'c', 'o']
list2 = ['d', 'i', 'n', 'g']
duplikat = []
for a in list1:
    for b in list2:
        if a == b:
            duplikat.append(a)

print(duplikat)  # Output ['d','i']

# Contoh4 Implementasi dengan list comprehension
list1 = ['d', 'i', 'c', 'o']
list2 = ['d', 'i', 'n', 'g']
duplikat = [a for a in list1 for b in list2 if a == b]
print(duplikat)  # Output: ['d','i']

# Contoh 5 kecilkan semua huruf
list_a = ["Hello", "World", "In", "Python"]
small_list_a = [_.lower() for _ in list_a]
print(small_list_a)

list_a = range(1, 10, 2)
x = [[a**2, a**3] for a in list_a]
print(x)

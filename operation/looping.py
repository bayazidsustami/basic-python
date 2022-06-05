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

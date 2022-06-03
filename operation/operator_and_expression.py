from operator import *


print(2 + 3)
print(3 * 5)
print('a'+'b')
print(2**4)
print(4/2)
print(13//2)
print(13 % 2)
print("-----------------")
print(2 << 2)
print(11 >> 1)
print(5 & 3)
print(5 | 3)
print(5 ^ 3)
print(~5)

print(5 < 3)  # lt
print(5 > 3)  # gt
print(5 <= 3)  # le
print(5 >= 3)  # ge
print(5 == 3)  # eq
print(5 != 3)  # ne

print("------------------")

hijau = 5
kuning = 10
print('Kelereng Hijau = {}'.format(hijau))
print('Kelereng Kuning = {}'.format(kuning))
listFunc = [lt, le, eq, ne, ge, gt]
for func in listFunc:
    print('{}(hijau, kuning): {}'.format(func.__name__, func(hijau, kuning)))

a = 2
a = a * 3
print(a)
a = 2
a *= 3  # simply way
print(a)

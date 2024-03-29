from re import A


a = [1, 1.1, 'python']
print(a)
print(a[2])

x = [5, 10, 15, 20, 25, 30, 35, 40]
print(x[5])
print(x[-1])
print(x[3:5])
print(x[:5])
print(x[-3:])
print(x[1:7:2])

x1 = [1, 2, 3]
x1[2] = 4
print(x1)
x1.append(7)
print(x1)

binatang = ['kucing', 'rusa', 'badak', 'gajah']
del binatang[2]
print(binatang)

s = "Hello World!"
print(s[4])  # ambil karakter kelima dari string s
print(s[6:11])  # ambil karakter ketujuh hingga sebelas dari string s
# s[5] = "d"  # ubah karakter keenam dari string s menjadi "d", seharusnya gagal karena immutable
# ubah isi string s menjadi "Halo Dunia!", seharusnya berhasil karena mutable
s = "Halo Dunia!"
print(s)


# tuple
print("------------------tuple-------------")
t = (5, 'program', 1+3j)
print(t[0])
print(t[1])
print(t[2])


# set
print("-------------------set-------------")
aSet = {1, 1, 1, 2, 2, 2, 3, 3, 3}
print(aSet)
# print(aSet[0]) we can't slicing if we use set because is unordered

# dictionary
print("---------------dictionary----------")
aDict = {1: "value", "key": 2}
print(type(aDict))
print(aDict)
print(aDict[1])
print(aDict["key"])

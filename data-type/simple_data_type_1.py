from re import S


x = [0]*10005  # inisialisasi array 0 sebanyak 10005; x[0]=0
x[1] = 1  # x[1]=1

for j in range(2, 10001):
    x[j] = x[j-1]+x[j-2]  # fibbonacci
print(x[10000])

# string
s = "ini adalah string baris tunggal"
ss = '''ini adalah string 
yang memiliki baris pertama
dan selanjutnya baris kedua'''
print(S)
print(ss)

isBool = False
print(isBool)
isBool1 = 0
isBool2 = 0.0
isBool3 = 1
isBool4 = 1.0
print(bool(isBool1))
print(bool(isBool2))
print(bool(isBool3))
print(bool(isBool4))

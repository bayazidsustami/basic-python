kelerengku = 10
if kelerengku:
    print("cetak ini benar")
    print(kelerengku)

tinggi_badan = int(input("Masukkan tinggi badan Anda : "))
if tinggi_badan >= 160:
    print("Silakan, Anda boleh masuk")
else:
    print("Maaf, Anda belum boleh masuk")

bilangan = int(input("masukkan bilangan :"))
if bilangan % 2 == 0:
    print('Bilangan {} adalah genap'.format(bilangan))
else:
    print('Bilangan {} adalah ganjil'.format(bilangan))

nilai = int(input("Masukkan nilai tugas Anda : "))
if nilai > 80:
    print("Selamat! Anda mendapat nilai A")
    print("Pertahankan!")
elif nilai > 70:
    print("Hore! Anda mendapat nilai B")
    print("Tingkatkan!")
elif nilai > 60:
    print("Hmm.. Anda mendapat nilai C")
    print("Ayo semangat!")
else:
    print("Waduh, Anda mendapat nilai D")
    print("Yuk belajar lebih giat lagi!")

bilangan = -3
if bilangan > 0:
    print('Bilangan {} adalah positif'.format(bilangan))
elif bilangan < 0:
    print('Bilangan {} adalah negatif'.format(bilangan))
else:
    print('Bilangan {} adalah nol'.format(bilangan))

# ternary operators
nilai = True
print("oke") if nilai else print("no")

# ternary tuples
#(condition_if_false, condition_if_true)[condition]
kata = (("false", "true"), [nilai])
print(kata)

# shorthand ternary
hasil = None
pesan = hasil or "Tidak ada data"
print(pesan)

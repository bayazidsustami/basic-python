while True:
    print('Masukkan apapun:')
    value = input()
    if value.isalpha():
        print("Halo", value)
        break
    elif value.isdecimal():
        print("angka yang ada masukkan", value)
        break
    elif value.isalnum():
        print("alphanumeric yang ada masukkan", value)
        break
    print('Masukkan nama Anda dengan benar.')

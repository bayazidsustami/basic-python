# upper()
aWord = "indonesia"
aWordWithUpper = aWord.upper()
print(aWordWithUpper)

# lower()
aWord1 = "INDONESIA"
aWordWithLower = aWord1.lower()
print(aWordWithLower)

# remove whitespace at end of string
print('Dicoding    '.rstrip())
# remove whitespace at first of string
print('    Dicoding'.lstrip())
# remove white space at first and end of string
print('    Dicoding    '.strip())

# remove a word that we don't want to use
kata = 'CodeCodeDicodingCodeCode'
print(kata.strip('Code'))

# give a boolean value if find first word that we want
print('Dicoding Indonesia'.startswith('Dicoding'))

# opposite of startswith()
print('Dicoding Indonesia'.endswith('Indonesia'))

# merge strings
print(' '.join(['Dicoding', 'Indonesia', '!']))
print('123'.join(['Dicoding', 'Indonesia', '!']))

# separate string by delimeter
print('Dicoding Indonesia !'.split())
print('Dicoding123Indonesia123!'.split('123'))  # split by '123' as delimeter
# split multiline string
print('''Halo,
aku ikan,
aku suka sekali menyelam
aku tinggal di perairan.
Badanku licin dan renangku cepat.
Senang berkenalan denganmu.'''.split('\n'))

# replace a string to new string
string = "Ayo belajar Coding di Dicoding"
print(string.replace("Coding", "Pemrograman"))

# just replace 1 word by adding at third params
string = "Ayo belajar Coding di Dicoding karena Coding adalah bahasa masa depan"
print(string.replace("Coding", "Pemrograman", 1))

# string check
kata = 'DICODING'
print(kata.isupper())
kata = 'dicoding'
print(kata.islower())

print('Dicoding'.upper().lower())
print('Dicoding'.lower().upper())
print('DICODING'.upper().lower().islower())
print('DICODING'.upper().lower().isupper())

# check if string is alphabet
print("dicoding".isalpha())
print("dicoding1".isalpha())

# check if string is alfanumeric
print("dicoding123".isalnum())
print("123".isalnum())
print("dicoding".isalnum())

# check if string is numeric
print("123".isdecimal())
print("dicoding123".isdecimal())

# check if string is just whitespace
print("     ".isspace())
print("   ds  ".isspace())

# check if string is capitalize
print('Dicoding Indonesia'.istitle())
print('Dicoding indonesia'.istitle())

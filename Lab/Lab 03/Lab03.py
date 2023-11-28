# lab03.py
# Nama : Rifqi Farel Muhammad
# NPM : 2106650310
# Mengkonversi bilangan bulat desimal ke string binary, begitu pula sebaliknya.

# The Beginning of Program
print('Lab 03 -- 2021\n')

# Konversi dari bilangan integer desimal ke string binary
print('From decimal to binary')
print('----------------------')

# Meminta user untuk menginput nilai bilangan integer desimal yang ingin diubah menjadi string binary
myInt = int(input('Give a positive integer in decimal representation: '))

# Mengkonversi bilangan integer desimal di dalam myInt menjadi string binary
binstr = ''    #Untuk menjadi akumulator di string binary
temp = myInt
while temp != 0 :
    bindigit = temp % 2
    binstr = str(bindigit) + binstr
    temp = temp // 2

# Mencetak hasil konversi bilangan integer desimal ke string binary
print('The binary representation of', myInt, 'is', '0b' + binstr)

# Konversi dari string binary ke bilangan integer desimal
print()
print('From binary to decimal')
print('----------------------')

# Meminta user untuk menginput nilai string binary ke bilangan integer desimal
binstr = input('Give a positive integer in binary representation: ')

# Mengkonversi binary digits di dalam binstr menjadi bilangan integer desimal
temp = binstr[2:]    #Menghilangkan '0b'
newInt = 0           #Untuk menjadi akumulator di bilangan integer desimal
length = len(temp)
for power in range(length) :
    bindigitstr = temp[-1]                      #Untuk mendapatkan digit paling kanan dari string binary
    bindigit = int(bindigitstr) * 2**power    
    newInt = newInt + bindigit                
    temp = temp[0:-1]                           #Menghilangkan digit paling kanan dari string binary

# Mencetak hasil konversi string binary ke bilangan integer desimal
print('The decimal representation of', binstr, 'is', newInt)

# Akhir dari program
print()
print('Thanks for using this program.')
print()
input('Press Enter to continue ...')

# Program Selesai
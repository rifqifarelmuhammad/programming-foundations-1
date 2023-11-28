# Beginning of Program
# Student name: Rifqi Farel Muhammad
# NPM: 2106650310

print('Lab 04')
print("Decimal & 2's Complement Converter")

# Meminta user untuk menginput jumlah bit yang ingin digunakan dalam sistem 2's complement
noBits = int(input("\nHow many bits to use in the 2's complement representation? "))

# Meminta user untuk menginput mode konversi yang ingin dilakukan dan menyimpannya dalam variabel mode
mode= int(input("\nPlease select the desired conversion mode : " +
                "\n1. Decimal -> 2's Complement" +
                "\n2. 2's Complement -> Decimal\n\n"))

# Memisahkan 2 mode yang akan dijalankan menggunakan if & else
if mode == 1 :     # Mode konversi integer decimal ke 2's complement

    # Menjalankan program konversi integer decimal ke 2's complement
    print()
    print("From decimal to 2's complement representation")
    print("---------------------------------------------")

    # Meminta user untuk menginput nilai integer decimal yang ingin dikonversikan
    myInt = int(input('\nGive an integer in decimal representation: '))
    
    binstr = ''    # Untuk menjadi akumulator di bilangan 2's complement
    
    # Menetapkan nilai awal yang benar dari nilai yang diinput oleh user
    if myInt >= 0 :     # Jika nilai yang diinput >= 0
        temp = myInt
    else :              # Jika nilai yang diinput <0
        temp = 2**noBits + (myInt)
    
    while temp > 0 :     # Mengkonversi integer decimal ke 2's complement
        bindigit = temp % 2                
        binstr = str(bindigit) + binstr
        temp = temp // 2
    
    binstr = binstr.zfill(noBits)     # Mengisi bits yang tersisa dengan 0 agar jumlah bit sesuai dengan yang diminta user

    # Mencetak hasil konversi
    print("\nThe 2's complement representation [" + str(noBits) + " bits] of", str(myInt), "is", str(binstr))

elif mode == 2 :     # Mode konversi 2's complement ke integer decimal

    # Menjalankan program konversi 2's complement ke integer decimal
    print()
    print("From 2's complement to decimal representation")
    print("---------------------------------------------")

    #Meminta user untuk menginput nilai 2's complement yang ingin dikonversikan
    binstr = input("\nGive an integer in 2's complement representation [" + str(noBits) + ' bits]: ')

    binstr = temp = binstr.zfill(noBits)     # Mengisi bits yang tersisa dengan 0 agar jumlah bit sesuai dengan yang diminta user

    # newInt merupakan akumulator di bilangan integer decimal
    # newInt merupakan bobot MSB dari bilangan 2's complement yang diinput oleh user
    newInt = int(temp[0]) * (-1) * 2**(noBits-1)
    length = len(temp)

    for power in range(length - 1) :     # Mengkonversi 2's complement ke integer decimal
        bindigitstr = temp[-1]
        bindigit = int(bindigitstr)
        newInt = newInt + (bindigit * (2**power))
        temp = temp[:-1]
    
    # Mencetak hasil konversi
    print('\nThe decimal representation of', binstr, 'is', str(newInt))

# Akhir dari program
print()
print('Thank you for using this program.')
input('Press Enter to continue ...')

# Program Selesai.
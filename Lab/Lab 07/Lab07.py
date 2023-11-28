# DASAR-DASAR PEMROGRAMAN 1 -- CSGE601020
# Lab 07 -- Vigenère cipher
# Name : Rifqi Farel Muhammad
# NPM  : 2106650310

# Mengimport module string untuk mendapatkan huruf lowercase dan uppercase
import string

lowerupper = string.ascii_letters     # String dari semua huruf lowercase dan uppercase

def main() :     # Sebagai fungsi utama program
    # Meminta user untuk menginput keyword, file input, file output, dan operation
    keyword = input('Enter the secret keyword: ')
    in_name = input('Enter the input file name: ')
    out_name = input('Enter the output file name: ')
    operation = input('(E)ncrypt or (D)ecrypt? ')

    # Membaca setiap huruf yang ada di dalam file sebagai sebuah string
    inf = open(in_name, 'r')
    text = inf.read()
    inf.close()

    keylen = len(keyword)     # Untuk dijadikan patokan pola keyword yang diinput oleh user
    dictioEnc = []     # Sebagai tempat untuk menjadi list of dictionaries dari encryption
    dictioDec = []     # Sebagai tempat untuk menjadi list of dictionaries dari decryption
    for i in range(0, keylen) :
        d = lowerupper.find(keyword[i])     # Mencari indeks tiap huruf keyword di lowerupper
        dictioEnc.append(dict(zip(lowerupper, lowerupper[d:] + lowerupper[:d])))     # list of dictionaries dari encryption
        dictioDec.append(dict(zip(lowerupper[d:] + lowerupper[:d], lowerupper)))     # list of dictionaries dari decryption
    
    result = ""     # Sebagai akumulator hasil output nanti
    for i in range(0, len(text)) :
        if operation == 'E' :     # Encryption
            result += dictioEnc[i % keylen].get(text[i], text[i])
        elif operation == 'D' :     # Decryption
            result += dictioDec[i % keylen].get(text[i], text[i])
    
    # Menyimpan hasil outputnya di dalam sebuah file txt
    outf = open(out_name, 'w')
    outf.write(result)
    outf.close()

# Menjalankan fungsi main()
if __name__ == '__main__' :
    main()
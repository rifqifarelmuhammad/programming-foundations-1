# DASAR-DASAR PEMROGRAMAN 1 -- CSGE601020
# Lab 05 -- Palindrophilia
# Name : Rifqi Farel Muhammad
# NPM  : 2106650310

# Mempersiapkan kalimat jika kata merupakan palindrome atau bukan untuk dimasukkan ke dalam format print
PALINDROME_TXT = 'palindrome'
NOT_PALINDROME_TXT = 'not palindrome'

# Judul Program
print("""
▒█▀▀█ █▀▀█ █░░ ░▀░ █▀▀▄ █▀▀▄ █▀▀█ █▀▀█ █▀▄▀█ █▀▀
▒█▄▄█ █▄▄█ █░░ ▀█▀ █░░█ █░░█ █▄▄▀ █░░█ █░▀░█ █▀▀
▒█░░░ ▀░░▀ ▀▀▀ ▀▀▀ ▀░░▀ ▀▀▀░ ▀░▀▀ ▀▀▀▀ ▀░░░▀ ▀▀▀""")
print(48 * "~")
print("Program ini akan mengecek apakah setiap string pada file yang diberikan merupakan palindrom. ")

# Memastikan apakah file yang diinput oleh user untuk dijadikan sebagai file input ada keberadaannya
try :
    # Meminta user untuk menginput file yang ingin dijadikan sebagai file input dan file output
    input_txt = input('Masukkan File Input: ')
    output_txt = input('Masukkan File Output: ')

    # Membuka file input dan file output
    input_file = open(input_txt, 'r+')    # 'r+' karena file input ingin diedit/ditambahkan saja
    output_file = open(output_txt, 'w')     # 'w' karena ingin menambahkan hasil program ke dalam file output
    
    line_counter = 0     # Sebagai akumulator penomoran di format string

    for line in input_file :     # Memeriksa tiap baris yang ada di file input
        word = line.lower().strip()     # Mengubah semua huruf dalam baris menjadi huruf kecil & menghilangkan whitespace
        temp = word     # Variabel temp dijadikan sebagai tempat untuk kita otak-atik agar kata yang ada di variabel word tidak berubah sama sekali
        line_counter += 1     # Sebagai nomor di tiap kata di format string
        
        is_palindrome = True     # Sebagai indikator apakah kata tersebut adalah palindrome atau bukan
        
        while is_palindrome and len(temp)>0 :     # Memeriksa apakah suatu kata termasuk ke dalam palindrome atau bukan
            first_letter = temp[0]
            last_letter = temp[-1]
            
            if first_letter != last_letter :     # Jika kata tidak termasuk ke dalam palindrome
                is_palindrome = False
            
            temp = temp[1:-1]
            
        if word == '' :     # Menghandle jika terdapat baris yang berupa string kosong
            word = '""'
        
        if is_palindrome :
            print_palindrome_string = f"{line_counter:<4d} {word:<20s} {PALINDROME_TXT:>14s}"    # Untuk mencetak kata yang palindrome
        else :
            print_palindrome_string = f"{line_counter:<4d} {word:<20s} {NOT_PALINDROME_TXT:>14s}"    # Untuk mencetak kata yang bukan palindrome
        
        print(print_palindrome_string, file = output_file)     # Mencetak hasil ke dalam file output
    
    # Memberitahu kepada user bahwa output dari program telah disimpan kepada file output
    print('output dari program telah disimpan di file output. Terima kasih telah menggunakan program ini')
        
    # Menutup file input dan file output
    input_file.close()
    output_file.close()
    
except IOError :     #Jika file input yang diinput oleh user tidak ditemukan
    print('Maaf, program tidak bisa mencari file yang diinginkan.')

# Akhir dari program
input('Tekan Enter untuk melanjutkan...')

# PROGRAM SELESAI.
# TP02.py
# Nama : Rifqi Farel Muhammad
# NPM : 2106650310
# Word Clouds
# Berkonsulatasi dengan Mayfa Shadrina Siddi

# Mengimport module yang dibutuhkan
import string
import random

# Membuat function untuk HTML nya
def make_HTML_word(word,cnt,high,low):
    htmlBig = 96
    htmlLittle = 14
    if high != low:
        ratio = (cnt-low)/float(high-low)
    else:
        ratio = 0
    fontsize = htmlBig*ratio + (1-ratio)*htmlLittle
    fontsize = int(fontsize)
    rgb = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    word_str = '<span style=\"color: rgb{}; font-size:{:s}px;\">{:s}</span>'
    return word_str.format(rgb,str(fontsize), word)

def make_HTML_box(body):
    box_str = """<div style=\"
    width: 560px;
    background-color: rgb(250,250,250);
    border: 1px grey solid;
    text-align: center\" >{:s}</div>
    """
    return box_str.format(body)

def print_HTML_file(body,title):
    fd = open(title+'.html','w')
    the_str="""
    <html> <head>
    <title>"""+title+"""</title>
    </head>

    <body>
    <h1>"""+title+'</h1>'+'\n'+body+'\n'+"""<hr>
    </body> </html>
    """
    fd.write(the_str)
    fd.close()

# The Beginning of Program
print('Program to create word cloud from a text file')
print('---------------------------------------------')
print('The result is stored as an HTML file,')
print('which can be displayed in a web browser.')

FileStopWords = open('stopwords.txt', 'r')     # Membuka dan membaca file stopWords.txt
stopWords = FileStopWords.read().split('\n')     # Membuat list dari anggota kata stopWords.txt

# Membuat function untuk membersihkan file dari tanda baca & anggota dari stopWords
def bersihinIsiFile(file) :
    word = file.lower().split()     # Membuat list dari anggota kata file & semua hurufnya menjadi kecil
    
    for i in range(len(word)) :
        word[i] = word[i].strip(string.punctuation)     # Menghilangkan tanda baca (punctuation) dari anggota kata file
    
    for kata in word[:] :
        if kata in stopWords :
            word.remove(kata)     # Menghilangkan anggota kata stopWords.txt dari anggota file

    return word

# Meminta user untuk menginput file dan memastikan file yang diinput oleh user ada keberadaannya
while True :
    try :
        inputFile = input("Please enter the file name: ")
        file_input = open(inputFile, 'r')     #Membuka & membaca file yang diinput oleh user
        fileInput = file_input.read()
        if fileInput == '' :     # Jika file yang diinput ada keberadaannya tetapi terdiri dari string kosong
            input('File yang diinput ada tetapi berisi string kosong, tekan Enter untuk keluar dari program....')
            FileStopWords.close()
            file_input.close()
            exit()
        break
    
    except IOError :     # Jika file yang diinput tidak ada keberadaannya
        print('File tidak ditemukan, mohon input file yang benar')

# Mencetak kalimat lanjutan program
print()
print(inputFile, ':')
print('56 words in frequency order as (count:word) pairs\n')

File = bersihinIsiFile(fileInput)     # Membuka dan membersihkan file yang diinput oleh user dari tanda baca dan anggota kata stopWords.txt

# Menghitung tiap kata yang terdapat di dalam file yang diinput oleh user & telah dibersihkan
kuantitasKata = {}     # Sebagai akumulator untuk jumlah tiap kata
for kata in File :
    if kata not in kuantitasKata :
        kuantitasKata[kata] = 1
    else :
        kuantitasKata[kata] += 1

# Mengurutkan variabel kuantitasKata dari jumlah kata terbanyak dan nilai karakter dari terbesar hingga terkecil
# Referensi : https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
kuantitasKata = dict(sorted(kuantitasKata.items(), key = lambda item : item[0], reverse=True))
kuantitasKata = dict(sorted(kuantitasKata.items(), key = lambda item : item[1], reverse=True))
kata = list(kuantitasKata.keys())
jumlah = list(kuantitasKata.values())

# Mencari jumlah huruf terpanjang di tiap kata untuk dijadikan patokan di dalam string formatting
terpanjang = 0     # Sebagai akumulator untuk mencari jumlah huruf di kata terpanjang
for i in range(len(kata)) :
    if len(kata[i]) > terpanjang :
        terpanjang = len(kata[i])

# Mencetak 56 angka dengan kuantitas terbanyak berdasarkan nilai karakter dari terkecil hingga terbesar
indeks = 0     # Sebagai akumulator indeks list
if len(kuantitasKata) >= 56 :     # Jika angka yang terdapat di dalam file yang telah dibersihkan >= 56
    for i in range(56) :
        if indeks == 3 :
            print(f"{jumlah[i]:>2d}:{kata[i]:<{terpanjang}}")
            indeks = 0
        else :
            print(f"{jumlah[i]:>2d}:{kata[i]:<{terpanjang}}", end = '')
            indeks += 1
else :     # Jika angka yang terdapat di dalam file yang telah dibersihkan < 56
    for i in range(len(kuantitasKata)) :
        if indeks == 3 :
            print(f"{jumlah[i]:>2d}:{kata[i]:<{terpanjang}}")
            indeks = 0
        else :
            print(f"{jumlah[i]:>2d}:{kata[i]:<{terpanjang}}", end = '')
            indeks += 1

# Untuk dijadikan patokan oleh HTML dalam mencetak kata dan ukuran kata di Word Clouds
hasil = []     # Sebagai akumulator untuk patokan HTML
if len(kuantitasKata) >= 56 :     # Jika angka yang terdapat di dalam file yang telah dibersihkan >= 56
    for isi in range(56) :
        a = (kata[isi], jumlah[isi])
        hasil.append(a)
else :     # Jika angka yang terdapat di dalam file yang telah dibersihkan < 56
    for isi in range(len(kuantitasKata)) :
        a = (kata[isi], jumlah[isi])
        hasil.append(a)
hasil.sort(key=lambda x : x[0])     # Mengurutkan kata berdasarkan nilai karakter dari terkecil hingga terbesar

# Untuk dijadikan patokan dalam mencari nilai hight_count dan low_count
angka = []     # Sebagai akumulator list kuantitas kata yang telah diurutkan
if len(kuantitasKata) >= 56 :      # Jika angka yang terdapat di dalam file yang telah dibersihkan >= 56
    for i in range(56) :
        angka.append(jumlah[i])
else :     # Jika angka yang terdapat di dalam file yang telah dibersihkan < 56
    for i in range(len(kuantitasKata)) :
        angka.append(jumlah[i])

# Mencari nilai hight_count dan low_count
high = 0     # Sebagai akumulator nilai hight_count
low = angka[0]     # Sebagai akumulator nilai low_count
for i in range(len(angka)) :
    if angka[i] >= high :
        high = angka[i]
    elif angka[i] <= low :
        low = angka[i]
    else :
        continue

# Membuat function untuk HTML dalam mencetak kata dan ukuran kata
def main():
    pairs = hasil
    high_count=high
    low_count=low
    body=''
    for word,cnt in pairs:
        body = body + " " + make_HTML_word(word,cnt,high_count,low_count)
    box = make_HTML_box(body)
    print_HTML_file(box,'A Word Cloud of ' + inputFile)

# Menjalankan function main() untuk menciptakan file HTML yang isinya Word Clouds dari file yang diinput oleh user
main()

# Menutup semua file yang telah kita buka sebelumnya
FileStopWords.close()
file_input.close()

# Akhir dari program
print()
input('Please type Enter to exit ...')

# Program Selesai.
# TP03.py
# Nama : Rifqi Farel Muhammad
# NPM : 2106650310
# Sorting One Million Numbers Using Merge Sort

# Membuat fungsi yang mengurutkan 2 list (left & right)
def merge(left, right):
    result = []     # Sebagai akumulator pengurutan list
    i, j = 0, 0     # Sebagai indexing untuk membandingkan 2 list

    while i < len(left) and j < len(right):
        if left[i] <= right[j] :     # Menambahkan index 0 list left ke result jika <= index 0 list right
            result.append(left[i])     # Menambahkan index 0 ke result & menghilangkannya dari list left
            i += 1
        else:     # Menambahkan index 0 list right ke result jika < index 0 list left
            result.append(right[j])     # Menambahkan index 0 ke result & menghilangkannya dari list right
            j += 1

    # result = result + left + right     # Menyatukan seluruh anggota list left & right yang tersisa ke list result

    return result + right[j:] + left[i:]     # Mereturn nilai result

# Membuat fungsi recursive yang memisahkan sebuah list menjadi 2 list (left & right) dan mengurutkannya menggunakan fungsi Merge
def mergeSort(L):
    if len(L) == 0 or len(L) == 1 :     # Jika panjang list adalah 0 atau 1, maka akan mereturn anggota list tersebut
        return L[:]
    else:     # Jika panjang list adalah lebih dari 1
        middle = len(L)//2     # Patokan untuk membagi list menjadi 2 bagian (left & right)
        left = mergeSort(L[:middle])     # Menggunakan fungsi mergeSort kembali untuk memisahkan list left menjadi 2 list (left & right)
        right = mergeSort(L[middle:])     # Menggunakan fungsi mergeSort kembali untuk memisahkan list right menjadi 2 list (left & right)
        return merge(left, right)     # Mengurutkan list left & right menggunakan fungsi merge
 
# Mengimport module time untuk menentukan berapa waktu yang digunakan untuk mengurutkan angka yang ada di dalam file yang diinput oleh user
import time

# Membuat fungsi utama program
def main():
    # Awalan program
    print('TP 03 DDP1 -- 2021')
    print('Implementation of Merge Sort')
    print('============================\n')

    try :     # Memastikan bahwa file yang diinput oleh user ada keberadaannya dalam storage PC
        FileInputName = input('Input file name: ')     # Meminta user untuk menginput file yang datanya ingin diurutkan
        ifile = open(FileInputName, 'r')     # Membuka dan membaca file yang telah diinput oleh user
        
    except IOError :     # Jika file yang diinput oleh user tidak ada keberadaannya dalam storage PC
        print('Input file not found.')
        exit()

    try:     # Memastikan bahwa semua data file yang diinput oleh user merupakan angka
        ListOfNumbers = [int(line.strip()) for line in ifile]

    except ValueError:     # Jika terdapat data dari file yang diinput oleh user bukan merupakan angka
        print('Data dari file yang diinput harus berupa angka')
        exit()
    
    # Meminta, membuka, dan menulis file yang ingin dijadikan sebagai tempat output oleh user
    FileOutputName = input('\nOutput file name: ')
    ofile = open(FileOutputName, 'w')
    
    # Sebagai patokan waktu sebelum program mengurutkan data yang diinput oleh user
    t1 = time.time()
    t = time.process_time()

    print('\nSorting in progress ...')
    sortedNumbers = mergeSort(ListOfNumbers)     # Program mengurutkan data file yang diinput oleh user

    # Waktu yang dibutuhkan oleh CPU serta durasi yang dibutuhkan untuk mengurutkan file yang diinput oleh user
    cpu_time = time.process_time() - t
    duration = time.time() - t1
    
    # Mencetak hasil pengurutan data ke dalam file output
    for i in range(len(sortedNumbers)) :
        printOutput = f"{sortedNumbers[i]}"
        print(printOutput, file = ofile)

    ifile.close()     # Menutup file input
    ofile.close()     # Menutup file output
    print('CPU time of the Merge-sort: ', cpu_time)     # Mencetak waktu yang dibutuhkan oleh CPU untuk mengurutkan file yang diinput oleh user
    print('Clock time of the Merge-sort: ', duration)     # Mencetak durasi yang dibutuhkan mengurutkan file yang diinput oleh user

# Menjalankan program main()
if __name__ == '__main__':
    main()
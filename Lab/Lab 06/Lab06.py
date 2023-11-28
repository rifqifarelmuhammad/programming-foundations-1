# DASAR-DASAR PEMROGRAMAN 1 -- CSGE601020
# Lab 06 -- Powers of a Power Set
# Name : Rifqi Farel Muhammad
# NPM  : 2106650310

def main() :     # Sebagai fungsi utama program
    # Meminta user untuk menginput sebuah set bilangan bulat
    inputSet = input("Please give a set of integers (e.g. {1,2,3}):\n")

    # Menghilangkan tanda '{}' dan memisahkan anggotanya berdasarkan tanda ','
    dataList = inputSet.strip('{}').split(',')

    # Mengubah tipe data anggota dataList menjadi integer
    dataListCleaned = [ int(data) for data in dataList if dataList != [''] ]

    result = recursivePowerSet(dataListCleaned)     # Membuat power setnya menggunakan fungsi recursivePowerSet

    # Mencetak power setnya menggunakan fungsi printing
    result = [{} if a == [] else set(a) for a in result]
    printing(result, inputSet)

def recursivePowerSet(inputList) :     # Untuk membuat power setnya
    if inputList == [] :     # Jika inputListnya berupa list kosong
        return [[]]
    
    else :     # Jika inputListnya bukan merupakan list kosong
        currentElement = [inputList[0]]
        powerset_without_first_element = recursivePowerSet(inputList[1:])
        return powerset_without_first_element + [(currentElement + i) for i in powerset_without_first_element]

def printing(outputList, inputSet) :     # Untuk mencetak power setnya
    print("The power set of " + inputSet + " is: ")
    print("{")

    for subset in outputList[:-1] :
        print("\t" + str(subset), end=",\n")

    print("\t" + str(outputList[-1]))
    print("}")

if __name__ == '__main__' :     # menjalankan fungsi main
    main()
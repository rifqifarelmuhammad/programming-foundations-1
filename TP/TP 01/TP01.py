# TP01.py
# Nama : Rifqi Farel Muhammad
# NPM : 2106650310
# MathBot untuk anak SD kelas 1

# Mengimport module random
import random

# The Beginning of Program
print('Hai! Selamat datang di Mathbot')

# Membuat tampilan halaman utama menggunakan while True
while True : 
    print('Pilihan Mode:\n1. Penjumlahan\n2. Pengurangan\n3. Campur\n4. Akhiri program\n')   # Halaman utama
    mode = input('Masukkan nomor mode yang ingin kamu mainkan: ')     # Meminta user untuk menginput mode yang ingin dimainkan

    # Memisahkan antara input untuk mode yang benar dan yang tidak benar
    if mode == '1' or mode == '2' or mode == '3' or mode == '4' :

        # Membuat tampilan halaman pilihan mode penjumlahan menggunakan while True
        if mode == '1' :
            while True :
                print('\nKamu berada di dalam mode penjumlahan\nPilihan kuis:\n1. Kuis lepas\n2. Kuis 5\n3. Ganti mode\n4. Akhiri program\n')   # Halaman mode penjumlahan
                jenisKuis = input('Masukkan nomor jenis kuis yang ingin kamu mainkan: ')     # Meminta user untuk menginput jenis kuis yang ingin dimainkan

                # Memisahkan antara input untuk jenis kuis yang benar dan yang tidak benar
                if jenisKuis == '1' or jenisKuis == '2' or jenisKuis == '3' or jenisKuis == '4' :

                    # Membuat program permainan kuis lepas dalam mode penjumlahan menggunakan while True
                    if jenisKuis == '1' :
                        while True :
                            angka1 = random.randint(0,10)
                            angka2 = random.randint(0,10)

                            print('\nBerapa', str(angka1), '+', str(angka2) + '? (Ketik "akhiri kuis" untuk keluar dari jenis kuis ini)')
                            jawaban = input('Jawab: ')     # Meminta user untuk menginput jawaban

                            if jawaban == 'akhiri kuis' :     # Untuk mengakhiri jenis kuis lepas
                                break

                            # Memisahkan antara input jawaban yang benar dan yang tidak benar
                            while True :
                                try :
                                    jawabanint = int(jawaban)
                                    if jawabanint == (angka1 + angka2) :     # Memisahkan jawaban yang benar dan yang salah
                                        print('Hore kamu benar!')
                                        break
                                    else :
                                        print('Jawaban kamu masih kurang tepat, jawaban yang benar adalah', (angka1 + angka2))
                                        break
                                except ValueError :     # Jika memasukkan input yang salah
                                    print('Jawaban tidak valid, hanya menerima jawaban berupa bilangan bulat')
                                    break

                    # Membuat program permainan kuis 5 dalam mode penjumlahan menggunakan for loop
                    elif jenisKuis == '2' :
                        score = 0     # Akumulator score akhir
                        for i in range(5) :
                            angka1 = random.randint(0,10)
                            angka2 = random.randint(0,10)

                            print('\nPertanyaan', str(i+1) + ': Berapakah', angka1, '+', angka2, '?')
                            jawaban = input('Jawab: ')     # Meminta user untuk menginput jawaban

                            # Memisahkan antara input jawaban yang benar dan yang tidak benar
                            while True :
                                try :
                                    jawabanint = int(jawaban)
                                    if jawabanint == (angka1 + angka2) :     # Memisahkan jawaban yang benar dan yang salah
                                        print('Hore kamu benar!')
                                        score += 20     # Score bertambah 20 jika benar
                                        break
                                    else :
                                        print('Jawaban kamu masih kurang tepat, jawaban yang benar adalah', (angka1 + angka2),'')
                                        break
                                except ValueError :     # Jika memasukkan input yang salah
                                    print('Jawaban tidak valid, hanya menerima jawaban berupa bilangan bulat')
                                    break

                        print('\nScore akhir kamu:', str(score))     # Mencetak score akhir

                    # Membuat program ganti mode dalam mode penjumlahan
                    elif jenisKuis == '3' :
                        print()
                        break     # Keluar dari while loop jenis kuis sehingga masuk ke while loop mode permainan

                    # Membuat program untuk mengakhiri semua program
                    else :
                        print('\nTerima kasih telah bermain kuis ini. Sampai jumpa lagi!')
                        exit()     # Program berakhir
                
                else :
                    print('\nProgram tidak mengenali perintah yang dimasukkan. Silahkan memilih dari perintah yang tersedia')

        # Membuat tampilan halaman pilihan mode pengurangan menggunakan while True
        elif mode == '2' :
            while True :
                print('\nKamu berada di dalam mode pengurangan\nPilih kuis:\n1. Kuis lepas\n2. Kuis 5\n3. Ganti mode\n4. Akhiri program\n')   # Halaman mode pengurangan
                jenisKuis = input('Masukkan nomor jenis kuis yang ingin kamu mainkan: ')     # Meminta user untuk menginput jenis kuis yang ingin dimainkan

                # Memisahkan antara input untuk jenis kuis yang benar dan yang tidak benar
                if jenisKuis == '1' or jenisKuis == '2' or jenisKuis == '3' or jenisKuis == '4' :
                    
                    # Membuat program permainan kuis lepas dalam mode pengurangan menggunakan while True
                    if jenisKuis == '1' :
                        while True :
                            angka1 = random.randint(0,10)
                            angka2 = random.randint(0,10)

                            # Memisahkan program jika angka1 >= angka2 atau sebaliknya
                            if angka1 >= angka2 :
                                print('\nBerapa', str(angka1), '-', str(angka2) + '? (Ketik "akhiri kuis" untuk keluar dari jenis kuis ini)')
                                jawaban = input('Jawab: ')     # Meminta user untuk menginput jawaban ketika angka1 >= angka2

                                if jawaban == 'akhiri kuis' :     # Untuk mengakhiri jenis kuis lepas
                                    break

                                # Memisahkan antara input jawaban yang benar dan yang tidak benar
                                while True:
                                    try :
                                        jawabanint = int(jawaban)
                                        if jawabanint == (angka1 - angka2) :     # Memisahkan jawaban yang benar dan yang salah
                                            print('Hore kamu benar!')
                                            break
                                        else :
                                            print('Jawaban kamu masih kurang tepat, jawaban yang benar adalah', (angka1 - angka2))
                                            break
                                    except ValueError :     # Jika memasukkan input yang salah
                                        print('Jawaban tidak valid, hanya menerima jawaban berupa bilangan bulat')
                                        break
                            
                            else :
                                print('\nBerapa', str(angka2), '-', str(angka1) + '? (Ketik "akhiri kuis" untuk keluar dari jenis kuis ini)')
                                jawaban = input('Jawab: ')     # Meminta user untuk menginput jawaban ketika angka2 > angka1

                                if jawaban == 'akhiri kuis' :     # Untuk mengakhiri jenis kuis lepas
                                    break

                                # Memisahkan antara input jawaban yang benar dan yang tidak benar
                                while True :
                                    try :
                                        jawabanint = int(jawaban)
                                        if jawabanint == (angka2 - angka1) :     # Memisahkan jawaban yang benar dan yang salah
                                            print('Hore kamu benar!')
                                            break
                                        else :
                                            print('Jawaban kamu masih kurang tepat, jawaban yang benar adalah', (angka2 - angka1))
                                            break
                                    except ValueError :     # Jika memasukkan input yang salah
                                        print('Jawaban tidak valid, hanya menerima jawaban berupa bilangan bulat')
                                        break

                    # Membuat program permainan kuis 5 dalam mode pengurangan menggunakan for loop
                    elif jenisKuis == '2' :
                        while True :
                            score = 0     # Akumulator score akhir
                            for i in range(5) :
                                angka1 = random.randint(0,10)
                                angka2 = random.randint(0,10)

                                # Memisahkan bentuk pertanyaan jika angka1 >= angka2 atau sebaliknya
                                if angka1 >= angka2 :
                                    print('\nPertanyaan', str(i+1) + ': Berapakah', angka1, '-', angka2, '?')
                                else :
                                    print('\nPertanyaan', str(i+1) + ': Berapakah', angka2, '-', angka1, '?')

                                jawaban = input('Jawab: ')     # Meminta user untuk menginput jawaban

                                # Memisahkan antara input jawaban yang benar dan yang tidak benar
                                while True :
                                    try :
                                        jawabanint = int(jawaban)
                                        if angka1 >= angka2 :
                                            if jawabanint == (angka1 - angka2) :   # Memisahkan jawaban yang benar dan yang salah jika angka1 >= angka2
                                                print('Hore kamu benar!')
                                                score += 20     # Score bertambah 20 jika benar
                                                break
                                            else :
                                                print('Jawaban kamu masih kurang tepat, jawaban yang benar adalah', (angka1 - angka2))
                                                break
                                        else :
                                            if jawabanint == (angka2 - angka1) :   # Memisahkan jawaban yang benar dan yang salah jika angka2 < angka 1
                                                print('Hore kamu benar!')
                                                score += 20     # Score bertambah 20 jika benar
                                                break
                                            else :
                                                print('Jawaban kamu masih kurang tepat, jawaban yang benar adalah', (angka2 - angka1))
                                                break
                                    except ValueError :     # Jika memasukkan input yang salah
                                        print('Jawaban tidak valid, hanya menerima jawaban berupa bilangan bulat')
                                        break
                            
                            print('\nScore akhir kamu:', score)     # Mencetak score akhir
                            break
                    
                    # Membuat program ganti mode dalam mode pengurangan
                    elif jenisKuis == '3' :
                        print()
                        break     # Keluar dari while loop jenis kuis sehingga masuk ke while loop mode permainan

                    # Membuat program untuk mengakhiri semua program
                    else :
                        print('\nTerima kasih telah bermain kuis ini. Sampai jumpa lagi!')
                        exit()     # Program berakhir
                
                else :
                    print('\nProgram tidak mengenali perintah yang dimasukkan. Silahkan memilih dari perintah yang tersedia')
                
        # Membuat tampilan halaman pilihan mode campur menggunakan while True
        elif mode == '3' :
            while True :
                print('\nKamu berada di dalam mode campur\nPilih kuis:\n1. Kuis lepas\n2. Kuis 5\n3. Ganti mode\n4. Akhiri program\n')   # Halaman mode campur
                jenisKuis = input('Masukkan nomor jenis kuis yang ingin kamu mainkan: ')     # Meminta user untuk menginput jenis kuis yang ingin dimainkan

                # Memisahkan antara input untuk jenis kuis yang benar dan yang tidak benar
                if jenisKuis == '1' or jenisKuis == '2' or jenisKuis == '3' or jenisKuis == '4' :
                    
                    # Membuat program permainan kuis lepas dalam mode campur menggunakan while True
                    if jenisKuis == '1' :
                        while True :
                            angka1 = random.randint(0,10)
                            angka2 = random.randint(0,10)
                            operasi = random.randint(0,1)

                            # Jika operasi = 0, maka operasi yang akan terjadi adalah operasi pertambahan
                            if operasi == 0 :
                                print('\nBerapa', str(angka1), '+', str(angka2) + '? (Ketik "akhiri kuis" untuk keluar dari jenis kuis ini)')
                                jawaban = input('Jawab: ')     # Meminta user untuk menginput jawaban

                                if jawaban == 'akhiri kuis' :     # Untuk mengakhiri jenis kuis lepas
                                    break

                                # Memisahkan antara input jawaban yang benar dan yang tidak benar
                                while True :
                                    try :
                                        jawabanint = int(jawaban)
                                        if jawabanint == (angka1 + angka2) :     # Memisahkan jawaban yang benar dan yang salah
                                            print('Hore kamu benar!')
                                            break
                                        else :
                                            print('Jawaban kamu masih kurang tepat, jawaban yang benar adalah', (angka1 + angka2))
                                            break
                                    except ValueError :     # Jika memasukkan input yang salah
                                        print('Jawaban tidak valid, hanya menerima jawaban berupa bilangan bulat')
                                        break
                            
                            # Jika operasi = 1, maka operasi yang akan terjadi adalah operasi pengurangan
                            elif operasi == 1 :
                                
                                # Memisahkan program jika angka1 >= angka2 atau sebaliknya
                                if angka1 >= angka2 :
                                    print('\nBerapa', str(angka1), '-', str(angka2) + '? (Ketik "akhiri kuis" untuk keluar dari jenis kuis ini)')
                                    jawaban = input('Jawab: ')     # Meminta user untuk menginput jawaban ketika angka1 >= angka2

                                    if jawaban == 'akhiri kuis' :     # Untuk mengakhiri jenis kuis lepas
                                        break

                                    # Memisahkan antara input jawaban yang benar dan yang tidak benar
                                    while True:
                                        try :
                                            jawabanint = int(jawaban)
                                            if jawabanint == (angka1 - angka2) :     # Memisahkan jawaban yang benar dan yang salah
                                                print('Hore kamu benar!')
                                                break
                                            else :
                                                print('Jawaban kamu masih kurang tepat, jawaban yang benar adalah', (angka1 - angka2))
                                                break
                                        except ValueError :     # Jika memasukkan input yang salah
                                            print('Jawaban tidak valid, hanya menerima jawaban berupa bilangan bulat')
                                            break
                                                    
                                else :
                                    print('\nBerapa', str(angka2), '-', str(angka1) + '? (Ketik "akhiri kuis" untuk keluar dari jenis kuis ini)')
                                    jawaban = input('Jawab: ')     # Meminta user untuk menginput jawaban ketika angka2 > angka1

                                    if jawaban == 'akhiri kuis' :     # Untuk mengakhiri jenis kuis lepas
                                        break

                                    # Memisahkan antara input jawaban yang benar dan yang tidak benar
                                    while True :
                                        try :
                                            jawabanint = int(jawaban)
                                            if jawabanint == (angka2 - angka1) :     # Memisahkan jawaban yang benar dan yang salah
                                                print('Hore kamu benar!')
                                                break
                                            else :
                                                print('Jawaban kamu masih kurang tepat, jawaban yang benar adalah', (angka2 - angka1))
                                                break
                                        except ValueError :     # Jika memasukkan input yang salah
                                            print('Jawaban tidak valid, hanya menerima jawaban berupa bilangan bulat')
                                            break

                    # Membuat program permainan kuis 5 dalam mode campur menggunakan for loop
                    elif jenisKuis == '2' :
                        while True :
                            score = 0     # Akumulator score akhir
                            for i in range(5) :
                                angka1 = random.randint(0,10)
                                angka2 = random.randint(0,10)
                                operasi = random.randint(0,1)
                                
                                # Jika operasi = 0, maka operasi yang akan terjadi adalah operasi pertambahan
                                if operasi == 0 :
                                    print('\nPertanyaan', str(i+1) + ': Berapakah', angka1, '+', angka2, '?')
                                    jawaban = input('Jawab: ')     # Meminta user untuk menginput jawaban

                                    # Memisahkan antara input jawaban yang benar dan yang tidak benar
                                    while True :
                                        try :
                                            jawabanint = int(jawaban)
                                            if jawabanint == (angka1 + angka2) :     # Memisahkan jawaban yang benar dan yang salah
                                                print('Hore kamu benar!')
                                                score += 20    # Score bertambah 20 jika benar
                                                break
                                            else :
                                                print('Jawaban kamu masih kurang tepat, jawaban yang benar adalah', (angka1 + angka2),'')
                                                break
                                        except ValueError :     # Jika memasukkan input yang salah
                                            print('Jawaban tidak valid, hanya menerima jawaban berupa bilangan bulat')
                                            break
                                
                                # Jika operasi = 1, maka operasi yang akan terjadi adalah operasi pengurangan
                                elif operasi == 1 :
                                    if angka1 >= angka2 :
                                        print('\nPertanyaan', str(i+1) + ': Berapakah', angka1, '-', angka2, '?')
                                    else :
                                        print('\nPertanyaan', str(i+1) + ': Berapakah', angka2, '-', angka1, '?')

                                    jawaban = input('Jawab: ')     # Meminta user untuk menginput jawaban

                                    # Memisahkan antara input jawaban yang benar dan yang tidak benar
                                    while True :
                                        try :
                                            jawabanint = int(jawaban)
                                            if angka1 >= angka2 :
                                                if jawabanint == (angka1 - angka2) :   # Memisahkan jawaban yang benar dan yang salah jika angka1 >= angka2
                                                    print('Hore kamu benar!')
                                                    score += 20     # Score bertambah 20 jika benar
                                                    break
                                                else :
                                                    print('Jawaban kamu masih kurang tepat, jawaban yang benar adalah', (angka1 - angka2))
                                                    break
                                            else :
                                                if jawabanint == (angka2 - angka1) :   # Memisahkan jawaban yang benar dan yang salah jika angka2 < angka 1
                                                    print('Hore kamu benar!')
                                                    score += 20     # Score bertambah 20 jika benar
                                                    break
                                                else :
                                                    print('Jawaban kamu masih kurang tepat, jawaban yang benar adalah', (angka2 - angka1))
                                                    break
                                        except ValueError :     # Jika memasukkan input yang salah
                                            print('Jawaban tidak valid, hanya menerima jawaban berupa bilangan bulat')
                                            break
                            
                            print('\nScore akhir kamu:', score)     # Mencetak score akhir
                            break
                    
                    # Membuat program ganti mode dalam mode campur
                    elif jenisKuis == '3' :
                        print()
                        break     # Keluar dari while loop jenis kuis sehingga masuk ke while loop mode permainan

                    # Membuat program untuk mengakhiri semua program
                    else :
                        print('\nTerima kasih telah bermain kuis ini. Sampai jumpa lagi!')
                        exit()     # Program berakhir
                                           
                else :
                    print('\nProgram tidak mengenali perintah yang dimasukkan. Silahkan memilih dari perintah yang tersedia')

        else : 
            print('\nTerima kasih telah bermain kuis ini. Sampai jumpa lagi!')
            exit()     # Program berakhir
    
    else :
        print('\nProgram tidak mengenali perintah yang dimasukkan. Silahkan memilih dari perintah yang tersedia\n')
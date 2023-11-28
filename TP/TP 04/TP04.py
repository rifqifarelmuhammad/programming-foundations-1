# TP03.py
# Nama : Rifqi Farel Muhammad
# NPM : 2106650310
# EAN-13 Barcode Generator

# Mengimport module yang dibutuhkan untuk menjalankan program
from tkinter import *
from tkinter.messagebox import showerror, showinfo

class BarcodeMaker(object):     # Membuat suatu class baru untuk menjalankan program
    # Membuat fungsi inisiasi atau fungsi utama untuk menjalankan operasi yang harus dilakukan oleh program
    def __init__(self):     
        window = Tk()     # Membuat sebuah window
        window.title('EAN-13 [by Rifqi]')     # Judul windownya
        window.geometry('270x370')     # Ukuran windownya
        window.resizable(False, False)     # Agar ukuran window tidak dapat diubah-ubah oleh user

        # Membuat sebuah frame sebagai tempat tulisan, entry dan canvas program
        frame1 = Frame(window, borderwidth=5)
        frame1.pack()

        # Membuat Tulisan serta entry untuk meminta & menyimpan nama file yang diinput oleh user
        labelFileName = Label(frame1, text = 'Save barcode to PS file [eg: EAN13.eps]:', font = 'Melvetica 10 bold')
        labelFileName.pack()
        self.fileName = StringVar()     # Tempat untuk menyimpan input user
        entryFile = Entry(frame1, textvariable = self.fileName)
        entryFile.pack()
        entryFile.bind('<Return>', self.getTheFileName)     # Menjadikan tombol 'Enter' sebagai keybind untuk menjalankan fungsi getTheFileName

        # Membuat Tulisan serta entry untuk meminta & menyimpan code barcode yang diinput oleh user
        labelCode = Label(frame1, text = 'Enter code (first 12 decimal digits):', font = 'Melvetica 10 bold')
        labelCode.pack()
        self.Code = StringVar()     # Tempat untuk menyimpan input user
        entryCode = Entry(frame1, textvariable = self.Code)
        entryCode.pack()
        entryCode.bind('<Return>', self.getTheInputCode)      # Menjadikan tombol 'Enter' sebagai keybind untuk menjalankan fungsi getTheInputCode

        # Membuat sebuah canvas untuk tempat memunculkan barcode
        self.canvas = Canvas(window, width = 220, height = 250, bg = 'white')
        self.canvas.pack()

        # Membuat tulisan bahwa 'Ctrl + \' adalah keybind untuk memunculkan informasi keybind program
        Help = Label(window, text = 'Press Ctrl + \ for help', font = 'Melvetica 10 bold')
        Help.pack()
        window.bind('<Control-backslash>', self.help)     # 'Ctrl + \' adalah keybind untuk menjalankan fungsi help
        window.bind('<Control-slash>', self.delete)     # 'Ctrl + /' adalah keybind untuk menjalankan fungsi delete
        
        window.mainloop()     # Menjalankan event loop
    
    def getTheFileName(self, event) :     # Fungsi yang akan memeriksa nama file output yang telah diminta oleh user
        filename = self.fileName.get()     # Mengambil nama file yang diinput user
        fileName = filename.strip()

        '''
        Memeriksa apakah nama file yang diinput oleh user diizinkan untuk dijadikan file output program menggunakan try except.
        Jika tidak boleh, maka akan muncul pop up error
        '''
        try:
            file_name = open(fileName, 'w')
            
            if (len(fileName) > 4 and '.eps' in fileName[-4:]) or (len(fileName) > 3 and '.ps' in fileName[-3:]) :
                file_name.close()
            
            elif ('.eps' in fileName[-4:] and fileName[:-4] == '') or ('.ps' in fileName[-3:] and fileName[:-3] =='') :
                showerror(title = 'Filename error!', message = 'Please input the correct filename!')
                file_name.close()

            else:
                showerror(title = 'Filename error!', message = 'Please input the correct filename!')
                file_name.close()
        
        except OSError :
            showerror(title = 'Filename error!', message = 'Please input the correct filename!')

    '''
    Fungsi yang akan memerika apakah nama file & code barcode yang diinput oleh user sudah benar atau belum.
    Jika sudah benar, maka akan dibuat barcodenya. Jika tidak benar, maka akan muncul pop up error
    '''
    def getTheInputCode(self,event) :
        filename = self.fileName.get()
        fileName = filename.strip()

        try:     # Memeriksa nama file yang diinput oleh user menggunakan try except
            file_name = open(fileName, 'w')
            if (len(fileName) > 4 and '.eps' in fileName[-4:]) or (len(fileName) > 3 and '.ps' in fileName[-3:]) :
                if self.fileName.get() == '' :
                    showerror(title = 'Filename error!', message = 'Please input the filename!')
                
                else:
                    try:     # Memeriksa code barcode yang diinput oleh user menggunakan try except
                        input_code = self.Code.get()
                        inputCode = int(input_code)
                        
                        if len(input_code) == 12 :     # Jika sudah sesuai, maka akan dibuat barcodenya
                            Structure = self.structure(input_code)
                            check_digit = self.checkDigit(input_code)

                            # Membuat tulisan awalan di canvas
                            self.canvas.create_text(110,35, text = 'EAN-13 Barcode:', font = 'Melvetica 13 bold', fill = 'black')
                            
                            # Mencetak first digit di bawah kiri barcodenya
                            self.canvas.create_text(10, 200, text = f"{Structure[0]}", font = 'Melvetica 12 bold', fill = 'black')

                            # Pola barcodde : SXXXXXXMRRRRRRE

                            # Membuat garis S (Start) nya
                            firstX = 19
                            y1 = 50
                            y2 = 195
                            y3 = 185
                            self.canvas.create_line(firstX,y1,firstX,y2, width=2, fill = 'red')
                            self.canvas.create_line(firstX + 2,y1,firstX + 2,y2, width=2, fill = 'white')
                            self.canvas.create_line(firstX + 4,y1,firstX + 4,y2, width=2, fill = 'red')

                            # Membuat garis XXXXXX dan nomor barcodenya
                            x1 = firstX + 4
                            x2 = 32
                            for i in range(len(Structure[3][0])):
                                self.canvas.create_text(x2, 200, text = f"{Structure[1][i]}", font = 'Melvetica 12 bold', fill = 'black')
                                for j in range(len(Structure[3][0][i])):
                                    if Structure[3][0][i][j] == '1':
                                        x1 += 2
                                        self.canvas.create_line(x1,y1,x1,y3, width=2, fill = 'blue')
                                    else :
                                        x1 += 2
                                        self.canvas.create_line(x1,y1,x1,y3, width=2, fill = 'white')
                                x2 += 14
                            
                            # Membuat garis M (Middle) nya
                            M = '01010'
                            for i in range(len(M)):
                                if M[i] == '1':
                                    x1 += 2
                                    self.canvas.create_line(x1,y1,x1,y2, width=2, fill = 'red')
                                else:
                                    x1 += 2
                                    self.canvas.create_line(x1,y1,x1,y2, width=2, fill = 'white')

                            # Mencetak nomor barcode dari susunan pola RRRRR
                            x2 += 8
                            for i in range(5):
                                self.canvas.create_text(x2, 200, text = f"{Structure[2][i]}", font = 'Melvetica 12 bold', fill = 'black')
                                x2 += 14

                            for i in range(len(Structure[3][1])):
                                # Mencetak nomor barcode dari susunan pola R terakhir (check digit)
                                self.canvas.create_text(x2, 200, text = f"{check_digit}", font = 'Melvetica 12 bold', fill = 'black')
                                
                                # Membuat garis RRRRRR nya
                                for j in range(len(Structure[3][1][i])):
                                    if Structure[3][1][i][j] == '1':
                                        x1 += 2
                                        self.canvas.create_line(x1,y1,x1,y3, width=2, fill = 'blue')
                                    else :
                                        x1 += 2
                                        self.canvas.create_line(x1,y1,x1,y3, width=2, fill = 'white')

                            # Membuat garis E (End) nya
                            self.canvas.create_line(x1+2,y1,x1+2,y2, width=2, fill = 'red')  
                            self.canvas.create_line(x1+4,y1,x1+4,y2, width=2, fill = 'white')  
                            self.canvas.create_line(x1+6,y1,x1+6,y2, width=2, fill = 'red')

                            # Mencetak Check Digit dari nomor barcode yang diinput
                            self.canvas.create_text(110,220, text = f"Check Digit: {check_digit}", font = 'Melvetica 12 bold', fill = 'orange')

                            # Mempostscript canvas
                            self.canvas.postscript(file = self.fileName.get(), colormode = 'color')

                        else :
                            showerror(title = 'Wrong Input!', message = 'Please input the correct code!')
                
                    except ValueError :
                        showerror(title = 'Wrong Input!', message = 'Please input the correct code!')

                    file_name.close()     # Menutup file yang berisi barcode
            
            elif ('.eps' in fileName[-4:] and fileName[:-4] == '') or ('.ps' in fileName[-3:] and fileName[:-3] =='') :
                showerror(title = 'Filename error!', message = 'Please input the correct filename!')
                file_name.close()

            else:
                showerror(title = 'Filename error!', message = 'Please input the correct filename!')
                file_name.close()
        
        except OSError :
            showerror(title = 'Filename error!', message = 'Please input the correct filename!')
        

    # Fungsi yang akan menghitung check digit dari code barcode yang telah diinput oleh user
    def checkDigit(self, code) :
        odd = int(code[0]) + int(code[2]) + int(code[4]) + int(code[6]) + int(code[8]) + int(code[10])
        even = int(code[1]) + int(code[3]) + int(code[5]) + int(code[7]) + int(code[9]) + int(code[11])
        checkDigit = (odd + even * 3) % 10
        
        if checkDigit != 0 :
            return (10 - checkDigit)
        else :
            return checkDigit

    # Fungsi yang akan mencari tahu first digit, first group, last group, dan struktur atau pola dari barcode yang diinput oleh user
    def structure(self, code):
        R = ['1110010', '1100110', '1101100', '1000010', '1011100', '1001110', '1010000', '1000100', '1001000', '1110100']     # Data R-Code

        G = []     # Tempat menaruh Data G-Code
        for i in range(len(R)) :
            G.append(R[i][::-1])

        L = []     # Tempat menaruh Data L-Code
        for i in range(len(R)) :
            temp = ''
            for j in range(len(R[i])) :
                if R[i][j] == '0' :
                    temp += '1'
                else :
                    temp += '0'
            L.append(temp)

        firstDigit = code[0]     # First Digit dari code barcode yang diinput user
        firstGroup = code[1:7]     # First Group dari code barcode yang diinput user
        lastGroup = code[7:]     # Last Group dari code barcode yang diinput user

        structureFirstLast = []     # Tempat menaruh structure / pola dari code barcode yang diinput user

        # Data Structure / pola yang akan dipakai tergantung first digit cede barcode 
        structurelistFirst = ['LLLLLL', 'LLGLGG', 'LLGGLG', 'LLGGGL', 'LGLLGG', 'LGGLLG', 'LGGGLL', 'LGLGLG', 'LGLGGL', 'LGGLGL']
        
        structure = structurelistFirst[int(firstDigit)]     # Mencari tahu structure / pola apa yang dipakai berdasarkan digit pertama code
        
        structureFirst = []     # Tempat menaruh structure / pola first group dari code barcode yang diinput user
        for i in range(len(firstGroup)):     # Mencari structure / pola First Group dari code barcode yang diinput user
            if structure[i] == 'L':
                structureFirst.append(L[int(firstGroup[i])])
            else :
                structureFirst.append(G[int(firstGroup[i])])
        structureFirstLast.append(structureFirst)
        
        structureLast = []     # Tempat menaruh structure / pola last group dari code barcode yang diinput user
        for i in range(len(lastGroup)) :     # Mencari structure / pola Last Group dari code barcode yang diinput user
            a = int(lastGroup[i])
            structureLast.append(R[a])
        structureLast.append(R[int(self.checkDigit(self.Code.get()))])
        structureFirstLast.append(structureLast)

        return [firstDigit, firstGroup, lastGroup, structureFirstLast]     # Mereturn semua data yang dibutuhkan

    # Fungsi yang akan menampilkan pop up info tentang informasi keybind dalam program ini
    def help(self,event) :
        showinfo(title = 'Keyboard Commands', message = 'Enter    = Input file / code\n' 'Ctrl + / = Delete barcode\n' 'Ctrl + \ = Help')
    
    # Fungsi yang akan menghapus semua hal dalam canvas
    def delete(self, event) :
        self.canvas.delete('all')

# Membuat fungsi yang akan langsung menjalankan class BarcodeMaker jika tidak diimport
def main():
    BarcodeMaker()

# Menjalankan fungsi main()
if __name__ == '__main__':
    main()
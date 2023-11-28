# DASAR-DASAR PEMROGRAMAN 1 -- CSGE601020
# Lab 08 -- Scribble
# Name : Rifqi Farel Muhammad
# NPM  : 2106650310
# Referensi : https://stackoverflow.com/questions/47996285/how-to-draw-a-line-following-your-mouse-coordinates-with-tkinter

# Mengimport module yang dibutuhkan oleh program
from tkinter import Tk, Canvas, Frame, Button, Label, TOP, BOTTOM, BOTH, LEFT
from tkinter.colorchooser import askcolor

class Scribble(object):     # Membuat class baru untuk program
    # Membuat fungsi inisiasi atau fungsi utama untuk menjalankan operasi yang harus dilakukan oleh program
    def __init__(self):
        master = Tk()     # Membuat sebuah window
        master.title('Simple Pen (Finger) Scribble')     # Judul windownya

        self.oldx, self.oldy = 0, 0     # Koordinat mouse awal / default
        self.color = 'green'     # Warna pen awal / default

        # Membuat canvas utama dengan ukuran 400 x 250 dan menjalankan function begin dan draw
        self.canvas = Canvas(master, width = 400, height = 250)
        self.canvas.bind("<Button-1>", self.begin)
        self.canvas.bind('<Button1-Motion>', self.draw)

        # Menampilkan canvas di layar
        self.canvas.pack(expand=True, fill=BOTH)

        # Membuat sebuah frame sebagai tempat tombol clear dan color
        frame1 = Frame(master)
        frame1.pack(side=TOP)

        # Membuat dan menampilkan tombol clear yang berfungsi untuk menghapus semua garis yang telah dibuat sebelumnya
        self.bt_clear = Button(master=frame1, text = 'Clear', command = self.delete, bg = 'orange')    # Background tombol selalu orange
        self.bt_clear.pack(side=LEFT, padx=5)

        # Membuat dan menampilkan tombol color yang berfungsi untuk mengganti warna pen
        self.bt_color = Button(master=frame1, text = 'Color', command = self.change_color, bg = self.color)     # Background tombol tergantung warna pena
        self.bt_color.pack(side=LEFT)

        # Membuat dan menampilkan tulisan "Press and drag the left mouse-button to draw"
        self.message = Label(master, text = 'Press and drag the left mouse-button to draw', fg = 'blue')     # Tulisan selalu berwarna biru
        self.message.pack(side = BOTTOM)

        # Menjalankan event loop
        master.mainloop()

    # Function untuk merekam posisi mouse sebagai awal dari kurva
    def begin(self, event):
        self.oldx, self.oldy = event.x, event.y

    # Function yang akan membuat garis-garis kecil dari posisi mouse lama ke yang baru ketika tombol kiri mouse ditekan
    def draw(self, event):
        x1, y1 = event.x, event.y

        if self.oldx and self.oldy :
            self.canvas.create_line(self.oldx, self.oldy, x1, y1, fill=self.color)

        self.oldx, self.oldy = x1, y1

    # Function yang akan membersihkan canvas utama
    def delete(self):
        self.canvas.delete('all')

    # Function yang akan mengganti warna pena
    def change_color(self):
        self.color = askcolor()[-1]     # Menampilkan sebuah menu pilihan warna yang dapat dipilih sebagai warna pena
        self.bt_color['bg'] = self.color     # Mengganti warna pena menjadi warna yang dipilih oleh user

# Menjalankan class Scribble()
if __name__ == '__main__':
    Scribble()
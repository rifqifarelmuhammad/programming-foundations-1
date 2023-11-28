# DASAR-DASAR PEMROGRAMAN 1 -- CSGE601020
# Lab 09.py
# Name : Rifqi Farel Muhammad
# NPM  : 2106650310

# Mengimport module yang dibutuhkan untuk menjalankan program
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.messagebox import *
from tkinter import Canvas

class DrawMoveRubberShapes(object):     # Membuat suatu class baru untuk menjalankan program
    # Membuat fungsi inisiasi atau fungsi utama untuk menjalankan operasi yang harus dilakukan oleh program
    def __init__(self) :
        window = Tk()     # Membuat sebuah window
        window.title("Lab 09: Draw Rubber Shapes, Select and Move")     # Judul windownya
        window.resizable(False,False)
        
        # Membuat menubar yang berbentuk pull-down untuk memilih shape yang ingin digunakan
        menubar = Menu(window)
        window.config(menu = menubar)

        # Membuat menubarnya dan menambahkan element shapenya
        shapeMenu = Menu(menubar, tearoff = True)
        Shape = IntVar()     # Menceklis pilihan shape yang ingin digunakan
        shapeMenu.add_radiobutton(label = "line", value = 0, variable = Shape,
                                    command = self.chooseLine)     # Membuat button dalam menu bar yang akan membuat shape line
        shapeMenu.add_radiobutton(label = "oval/circle", value = 1, variable = Shape,
                                    command = self.chooseOval)     # Membuat button dalam menu bar yang akan membuat shape oval/circle
        shapeMenu.add_radiobutton(label = "rectangle", value = 2, variable = Shape,
                                    command = self.chooseRectangle)     # Membuat button dalam menu bar yang akan membuat shape rectangle
        menubar.add_cascade(label = "Choose a Shape", menu = shapeMenu)     # Judul menubarnya

        self.canvas = Canvas(window, width=500, height=400, relief='ridge',
                        bg='white', bd = 5)     # Membuat sebuah canvas
        self.canvas.pack()     # Menampilkan canvas di layar
        self.canvas.bind('<ButtonPress-1>', self.onStart)     # Ketika user mengklik kiri, maka akan menjalankan fungsi onStart
        self.canvas.bind('<B1-Motion>', self.onGrow)     # Ketika user menahan & mendrag klik kiri, maka akan menjalankan fungsi onGrow
        self.canvas.bind('<B3-Motion>', self.onMove)     # Ketika user menahan & mendrag klik kanan, maka akan menjalankan fungsi onMove
        window.bind('<h>', self.message)     # Ketika user menekan huruf 'h' pada keyboard, maka akan menjalankan fungsi message
        window.bind('<d>', self.deleteDraw)     # Ketika user menekan huruf 'd' pada keyboard, maka akan menjalankan fungsi deleteDraw

        # Membuat tulisan 'Press h for help' yang selalu ada di pojok kiri atas dan tidak dapat dipindahkan ataupun dihapus
        label = Label(self.canvas, text = 'Press h for help', bg = 'white')
        label.pack()
        self.canvas.create_window(50, 18, window = label, tags = 'text')

        # Sebagai patokan gambar dan bentuk yang terakhir kali dipilih
        self.drawn = None
        self.shape = self.canvas.create_line

        # Membuat sebuah frame dan menampilkannya ke window
        frame1 = Frame(window, borderwidth=2)
        frame1.pack()

        # Membuat sebuah tombol yang berfungsi untuk mengganti dan memilih warna yang ingin digunakan
        self.fillColor = StringVar()
        self.fillColor.set('red')     # Default warnanya adalah merah
        def colorCommand():
            (rgb,color) = askcolor()
            if color != None:
                self.fillColor.set(color)
                colorButton["bg"] = color
        colorButton = Button(frame1, text = "Color",
            command=colorCommand, bg = self.fillColor.get())     # Membuat tombolnya
        colorButton.grid(row=1,column=4)     # Menampilkan tombolnya

        # Function yang akan membuat sebuah tombol untuk menghapus semua gambar yang telah dibuat
        def clear():
            self.canvas.delete('shape')     # Menghapus semua gambar yang telah dibuat
        clearButton = Button(frame1, text = "Clear",
            command=clear, bg = 'white')     # Membuat tombolnya
        clearButton.grid(row=1,column=8)     # Menampilkan tombolnya

        window.mainloop()     # Menjalankan event loop
    
    def chooseLine(self):     # Function yang akan menciptakan shape line ke canvas
        self.shape = self.canvas.create_line

    def chooseOval(self):     # Function yang akan menciptakan shape oval/circle ke canvas
        self.shape = self.canvas.create_oval
    
    def chooseRectangle(self):     # Function yang akan menciptakan shape rectangle ke canvas
        self.shape = self.canvas.create_rectangle
    
    # Function yang akan mengingat posisi mouse ketika diklik kiri oleh user sebagai awalan menggambar
    def onStart(self, event):     
        self.start = event
        self.drawn = None

    # Function yang dapat membuat gambar sesuai shape dan ukuran yang kita inginkan
    def onGrow(self, event):
        canvas = event.widget
        if self.drawn : 
            canvas.delete(self.drawn)
        objectId = self.shape(self.start.x, self.start.y, event.x,
            event.y, fill = self.fillColor.get(), width = 0, tags = 'shape')
        self.drawn = objectId
        
    # Function yang dapat memindahkan posisi gambar yang telah dibuat sebelumnya
    def onMove(self, event) :
        Widget = event.widget
        xc = Widget.canvasx(event.x)
        yc = Widget.canvasx(event.y)
        self.item = Widget.find_closest(xc, yc)[0]
        self.previous = (xc, yc)

        if self.item :
            canvas = event.widget
            x0, y0, x1, y1 = canvas.bbox(self.item)
            diffX, diffY = event.x - x0 + (x0-x1) / 2, event.y - y0 + (y0 - y1) / 2
            canvas.move(self.item, diffX, diffY)
            self.start = event
            self.start.x += (x0 - x1) / 2
            self.start.y += (y0 - y1) / 2
    
    # Function yang akan menampilkan sebuah pop up berisikan command info yang tersedia dalam program ini
    def message(self, event) :
        showinfo(title = 'Draw, Select, Move', message = 'Mouse commands:\n' '    Left+Drag = Draw new rubber shape\n'
        '    Right = Select a shape\n' '    Right+Drag = Drag the selected shape \n\n' 'Keyboard commands:\n'
        '    d = Delete the selected shape\n' '    h = Help')
    
    # Function yang akan menghapus gambar yang diinginkan oleh user
    def deleteDraw(self, event) :
        self.canvas.delete(self.item)
    
if __name__ == '__main__':     # Menjalankan class DrawMoveRubberShapes()
    DrawMoveRubberShapes()
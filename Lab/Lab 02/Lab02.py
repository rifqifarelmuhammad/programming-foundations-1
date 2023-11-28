# Nama : Rifqi Farel Muhammad
# lab02.py
# Menggunakan module turtle untuk menggambar poligon
# Meminta input komponen warna (r,g,b) dari user, serta jumlah sisi pada poligon

# Mengimport module turtle
import turtle

# Mempersiapkan module turtle
turtle.shape('turtle')
turtle.title('Lab 02')

# Meminta user untuk menginput nilai dari komponen warna merah
r = float(turtle.textinput('Lab 02', 'Komponen warna merah [antara 0 and 1]: '))

# Meminta user untuk menginput nilai dari komponen warna hijau
g = float(turtle.textinput('Lab 02', 'Komponen warna hijau [antara 0 and 1]: '))

# Meminta user untuk menginput nilai dari komponen warna biru
b = float(turtle.textinput('Lab 02', 'Komponen warna biru [antara 0 and 1]: '))

# Meminta user untuk menginput jumlah sisi poligon yang ingin digambar
n = int(turtle.textinput('Lab 02', 'Masukkan jumlah sisi pada poligon [antara 3 dan 10]: '))

# Mengkombinasikan warna dari nilai rgb yang telah diinput oleh user
turtle.color(r,g,b)

# Nilai default panjang sisi luar (keliling) pentagon
DEFAULT_SIDE_LEN = 500

# Nilai sudut dalam dari polygon
internal_angle = 360 / n

# Menyesuaikan nilai panjang dari sisi poligon relatif terhadap n
side_len = DEFAULT_SIDE_LEN // n

# Memindahkan turtle ke posisi tengah dan mengatur arahnya dengan tepat
turtle.penup()
turtle.goto(0 + (side_len / 2), 0)
turtle.setheading(180)

# Menggambar poligon dengan warna yang telah diminta oleh user
turtle.pendown()
turtle.begin_fill()

for i in range(n) :
    turtle.forward(side_len)
    turtle.right(internal_angle)

turtle.end_fill()
turtle.penup()

# Membuat turtle menjadi tak terlihat
turtle.hideturtle()

# Pesan untuk user
turtle.penup()
turtle.goto(0, 200)
turtle.pendown()
turtle.color('blue')
turtle.write("Please click on the graphics window to exit", False,
 align='center', font=('Arial', 20, 'normal'))

# Menunggu user untuk meng-click layar untuk keluar dari program turtle
turtle.exitonclick()

# Program selesai
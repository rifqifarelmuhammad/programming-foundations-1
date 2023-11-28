# lab01.py
# Beginning of Program
# Name : Rifqi Farel Muhammad
# NPM : 2106650310

# judul program
print('Lab 01\n')
print('Celcius to Temperatur X')
print('----------------------')

# nilai titik didih & beku celcius konstan, karena konversi suhu X akan dilakukan dengan bantuan suhu celcius
TITIK_DIDIH_CELCIUS = 100
TITIK_BEKU_CELCIUS = 0

# meminta user untuk menginput nilai suhu celcius, titik didih dalam skala X, dan titik beku dalam skala X
suhu_celcius = input('Masukkan suhu dalam skala celcius: ')
titik_didih_x = input('Masukkan suhu titik didih dalam skala X: ')
titik_beku_x = input('Masukkan suhu titik beku dalam skala X: ')

# konversi tipe data menjadi float
suhu_celcius = float(suhu_celcius)
titik_didih_x = float(titik_didih_x)
titik_beku_x = float(titik_beku_x)

# operasi aritmatika
perhitungan_x = titik_didih_x - titik_beku_x
perhitungan_celcius = (suhu_celcius - TITIK_BEKU_CELCIUS) / (TITIK_DIDIH_CELCIUS - TITIK_BEKU_CELCIUS)

# hasil
float_temperature_x = (perhitungan_celcius * perhitungan_x) + titik_beku_x
int_temperature_x = int(float_temperature_x)

# output
print('Nilai float dalam skala X adalah: ', float_temperature_x)
print('Nilai integer dalam skala X adalah: ', int_temperature_x)

# akhir program
print('\nEnd of program')
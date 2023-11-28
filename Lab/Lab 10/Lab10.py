# DASAR-DASAR PEMROGRAMAN 1 -- CSGE601020
# Fraction.py
# Name : Rifqi Farel Muhammad
# NPM  : 2106650310

gcd = lambda a, b : a if b == 0 else gcd(b, a%b)     # Fungsi untuk mencari FPB

def lcm(a,b):     # Fungsi untuk mencari KPK
    return (a*b)//gcd(a,b)

class Fraction(object):     # Membuat class baru yang bernama Fraction
    # Fungsi untuk menjadikan object sebagai pecahan / bilangan rasional
    def __init__(self,numer,denom=1):     # Default parameter penyebutnya bernilai 1
        self.numer = numer
        self.denom = denom

    # Fungsi untuk mencetak object sebagai pecahan dengan type data string
    def __str__(self):     
        if self.denom == 1 :     # Jika object dalam bentuk pecahan bernilai n/1, maka akan dicetak sebagai n saja
            return str(self.numer)     
        else :
            return str(self.numer)+'/'+str(self.denom)
    
    def __repr__(self):     # Fungsi yang akan memanggil self.__str__() jika user mengetik instance dalam interpreter
        return self.__str__() 
    
    def __add__(self, param):     # Fungsi yang akan menambahkan dua buah pecahan / Fraction
        if type(param) == int:     # Jika tipe data dari param adalah int, maka akan diubah terlebih dahulu menjadi Fraction
            param = Fraction(param)

        if type(param) == Fraction:     # Menambahkan dua buah pecahan
            the_lcm = lcm(self.denom, param.denom)
            numerator_sum = (the_lcm * self.numer//self.denom) + \
                (the_lcm * param.numer//param.denom)
            return Fraction(numerator_sum,the_lcm)     # Mereturn hasil penjumlahan

        else:     # Jika type data dari param bukanlah int atau Fraction
            raise TypeError('can only concatenate int or Fraction to Fraction')
    
    def __sub__(self, param):     # Fungsi yang akan mengurangi dua buah pecahan / Fraction
        if type(param) == int:     # Jika tipe data dari param adalah int, maka akan diubah terlebih dahulu menjadi Fraction
            param = Fraction(param)
        
        if type(param) == Fraction:     # Mengurangi dua buah fraction
            the_lcm = lcm(self.denom, param.denom)
            numerator_diff = (the_lcm * self.numer//self.denom) - \
                (the_lcm * param.numer//param.denom)
            return Fraction(numerator_diff, the_lcm)     # Mereturn hasil pengurangan

        else:     # Jika type data dari param bukanlah int atau Fraction
            raise TypeError('can only concatenate int or Fraction to Fraction')
    
    def reduce(self):     # Fungsi untuk menyederhanakan pecahan
        the_gcd = gcd(self.numer,self.denom)
        return Fraction(self.numer//the_gcd, self.denom//the_gcd)
    
    def __eq__(self,param):     # Fungsi untuk mengecek apakah dua pecahan memiliki nilai yang sama
        if type(param) == int:     # Jika tipe data dari param adalah int, maka akan diubah terlebih dahulu menjadi Fraction
            param = Fraction(param)
        
        if type(param) == Fraction:     # Membandingkan dua buah pencahan
            reduced_self = self.reduce()
            reduced_param = param.reduce()
            return reduced_self.numer == reduced_param.numer and\
                reduced_self.denom == reduced_param.denom     # Mereturn hasil perbandingan dalam bentuk boolean
        
        else :     # Jika type data dari param bukanlah int atau Fraction
            raise TypeError('can only concatenate int or Fraction to Fraction')

    def __radd__(self,param):     # Menghandle jika terjadi pertambahan dengan type data (not Fraction + Fraction)
        return self.__add__(param)

    def __mul__(self,param) :     # Fungsi yang akan mengalikan dua buah pecahan / Fraction
        if type(param) == int:     # Jika tipe data dari param adalah int, maka akan diubah terlebih dahulu menjadi Fraction
            param = Fraction(param)

        if type(param) == Fraction:     # Mengalikan dua buah pecahan
            numer = self.numer * param.numer
            denom = self.denom * param.denom
            return Fraction(numer, denom)     # Mereturn hasil perkalian
        
        else:     # Jika type data dari param bukanlah int atau Fraction
            raise TypeError('can only concatenate int or Fraction to Fraction')
    
    def __rmul__(self,param) :     # Menghandle jika terjadi perkalian dengan type data (not Fraction * Fraction)
        return self.__mul__(param)
    
    def __truediv__(self,param) :     # Fungsi yang akan membagi dua buah pecahan / Fraction
        if type(param) == int:     # Jika tipe data dari param adalah int, maka akan diubah terlebih dahulu menjadi Fraction
            param = Fraction(param)

        if type(param) == Fraction:     # Membagi dua buah pecahan
            numer = self.numer * param.denom
            denom = self.denom * param.numer
            return Fraction(numer, denom)     # Mereturn hasil pembagian
        
        else:     # Jika type data dari param bukanlah int atau Fraction
            raise TypeError('can only concatenate int or Fraction to Fraction')
    
    def __gt__(self,param) :     # Fungsi untuk mengecek apakah nilai dari object lebih besar daripada param
        if type(param) == int:     # Jika tipe data dari param adalah int, maka akan diubah terlebih dahulu menjadi Fraction
            param = Fraction(param)

        if type(param) == Fraction:     # Membandingkan dua buah pecahan
            the_lcm = lcm(self.denom, param.denom)
            Self = (the_lcm * self.numer//self.denom)
            Param = (the_lcm * param.numer//param.denom)
            return (Self > Param)     # Mereturn hasil perbandingan dalam bentuk boolean
        
        else:     # Jika type data dari param bukanlah int atau Fraction
            raise TypeError('can only concatenate int or Fraction to Fraction')
    
    def __ge__(self,param) :     # Fungsi untuk mengecek apakah nilai dari object lebih besar atau sama dengan nilai param
        if type(param) == int:     # Jika tipe data dari param adalah int, maka akan diubah terlebih dahulu menjadi Fraction
            param = Fraction(param)

        if type(param) == Fraction:     # Membandingkan dua buah pecahan
            the_lcm = lcm(self.denom, param.denom)
            Self = (the_lcm * self.numer//self.denom)
            Param = (the_lcm * param.numer//param.denom)
            return (Self >= Param)     # Mereturn hasil perbandingan dalam bentuk boolean
        
        else:     # Jika type data dari param bukanlah int atau Fraction
            raise TypeError('can only concatenate int or Fraction to Fraction')
    
    def __getitem__(self, index) :     # Fungsi untuk menampilkan pembilang (jika index = 1) dan penyebut (jika index = 2) dari object
        if index == 1 or index == 2 :
            return (self.numer, self.denom)[index-1]     # Mereturn pembilang atau penyebut

        else:     # Jika index yang diinput oleh user bukanlah 1 atau 2
            raise ValueError('There is an inappropriate value')

def main() :
    p1 = Fraction(3,5)
    p2 = Fraction(1,20)
    print( Fraction(8,1) ) 
    print( p1*p2 )
    print( p1/p2 ) 
    print( p1*3 ) 
    print( 3*p1 ) 
    print( p1[1] ) 
    print( p1[2] ) 
    print( p1 > p2 ) 
    print( p2 > p1 ) 
    print( Fraction(1,2) >= Fraction(3,6) ) 
    print( Fraction(50,101)[2] ) 
    print( Fraction(2,5) > Fraction(4,5) ) 
    print( Fraction(3,7) >= Fraction(1,7)*3 ) 
    print( Fraction(3,7)/3 == Fraction(1,7) ) 
    print( Fraction(9,20)*Fraction(20,9) )
    print( (Fraction(9,20)*Fraction(20,9)).reduce() )
    print( Fraction(29,100003).reduce() )
    print( p1[0] )

if __name__ == '__main__' :
    main()
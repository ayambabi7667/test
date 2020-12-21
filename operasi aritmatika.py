import os
os.system('clear')

# operasi aritmatika
a = 10
b = 3

# operasi tambah +
hasil = a + b
print(a,'+',b,'=',hasil)
# operasi kurang -
hasil = a - b
print(a,'-',b,'=',hasil)
# operasi perkalian *
hasil = a * b
print(a,'*',b,'=',hasil)
# operasi pembagian /
# otomatis nilai menjadi dalam float (data mengandung koma)
hasil = a / b
print(a,'/',b,'=',hasil)
# operasi pangkat **
hasil = a ** b
print(a,'**',b,'=',hasil)
# operasi modulus %
# (nilai sisa pembagian)
hasil = a % b
print(a,'%',b,'=',hasil)
# operasi floor division //
# (pembulatan nilai pembagian)
hasil = a // b
print(a,'//',b,'=',hasil)

# operasi prioritas
"""
   urutan prioritas:
   1. ()
   2. exponen **
   3. perkalian dan lainnya * / ** % //
   4. pertambahan dan pengurangan + -
"""

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)
#prioritas ()
hasil = x ** y * (z + x) / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)

hasil = x + y * z
print(x,'+',y,'*',z,'=',hasil)
# kurung akan mengambil langkah pertama
hasil = (x + y) * z
print('(',x,'+',y,') *',z,'=',hasil)

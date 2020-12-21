import os
os.system('clear')
print
print'\t--matematika--'
print
print'1. penjumlahan'
print'2. pengurangan'
print
pilih = input('pilih menu :')

if pilih == 1:
   print
   angka_1 = input('angka pertama :')
   angka_2 = input('angka kedua :')
   total = angka_1 + angka_2
   print
   print'total : ', total

elif pilih == 2:
   print
   angka_1 = input('angka pertama :')
   angka_2 = input('angka kedua :')
   total = angka_1 - angka_2
   print
   print'total : ', total

else:
   print"""menu
ga ada"""

import os
os.system('clear')

# data yg dimasukkan pasti tipe string

data = input("masukkan data: ")
print("data = ",data,"type =",type(data))
print

#jika ingin mengambil data int

angka = float(input("masukkan angka: "))
angka = int(input("masukkan angka: "))
print("data = ",angka,",type =",type(angka))
print

#jika ingin mengambil data boolean
#harus diubah ke int dulu menurut video(= bool(int(input..)

biner = bool(input("masukkan nilai boolean: "))
print("data = ",biner,",type =",type(biner))

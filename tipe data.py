print '\t tipe data angka satuan yg tidak ada koma (integer)'
# tipe data angka satuan yg tidak ada koma (integer)
data_integer = 1
print("data : ", data_integer)
print("- bertipe : ", type(data_integer))
print
# tipe data angka dengan koma (float)
data_float = 1.5
print("data : ", data_float)
print("- bertipe : ", type(data_float))
print
# tipe data kumpulan karakter (string)
data_string = "ucup"
print("data : ", data_string)
print("- bertipe : ", type(data_string))
print
# tipe data biner true/false (boolean)
data_bool = True
print("data : ", data_bool)
print("- bertipe : ", type(data_bool))
print
# tipe data khusus
# bilangan complex
data_complex = complex(5,6)
print("data : ", data_complex)
print("- bertipe :", type(data_complex))
print
#  tipe data dari bahasa C
from ctypes import c_double

data_c_double = c_double(10.5)
print("data :", data_c_double)
print("- bertipe :", type (data_c_double))

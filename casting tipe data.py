import os
os.system('clear')

# integer
print("integer")

data_int = 9;
print("data = ", data_int, "type =",type(data_int))

data_float = float(data_int)
data_str   = str(data_int)
data_bool  = bool(data_int) # akan false jika int = 0
print("data = ", data_float, "type =",type(data_float))
print("data = ", data_str, "type =",type(data_str))
print("data = ", data_bool, "type =",type(data_bool))

print

# float
print("float")

data_float = 9.9;
print("data = ", data_float, "type =",type(data_float))

data_int   = int(data_float) # akan dibulatkan kebawah
data_str   = str(data_float)
data_bool  = bool(data_float)
print("data = ", data_int, "type =",type(data_int))
print("data = ", data_str, "type =",type(data_str))
print("data = ", data_bool, "type =",type(data_bool))

print

# boolean
print("boolean")

data_bool = True;
print("data = ", data_bool, "type =",type(data_bool))

data_int   = int(data_bool)
data_str   = str(data_bool)
data_float = float(data_bool)
print("data = ", data_int, "type =",type(data_int))
print("data = ", data_str, "type =",type(data_str))
print("data = ", data_float, "type =",type(data_float))

print

# string
print("string")

data_str = 10;
print("data = ", data_str, "type =",type(data_str))

data_int   = int(data_str) # string harus angka
data_bool  = bool(data_str) # false jika string kosong
data_float = float(data_str)
print("data = ", data_int, "type =",type(data_int))
print("data = ", data_bool, "type =",type(data_bool))
print("data = ", data_float, "type =",type(data_float))

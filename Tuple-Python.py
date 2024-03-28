konstanta = (23, 43, 53)
print(konstanta)
print(type(konstanta))
print(len(konstanta))

name = ("Fatih", "Siti", "Nur", "Ahmad")
print(name)
print(type(name))
print(len(name))

# Access Tuple
print(konstanta[2])
print(name[1:3])

# konstanta[1] = 99 # error

name_list = list(name)
print(name_list)
name_list.append("Musa")
print(name_list)
name_list.remove("Siti")
print(name_list)

name_tuple = tuple(name_list)
print(name_tuple)

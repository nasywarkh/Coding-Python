'''
a = open("File Handling/File 1.txt","x") # x : create file , tidak mengizinkan file yang sama

a = open("File Handling/File 1.txt", "r") # r : read file

a.close()
'''
b = open("File Handling/File 2.txt", "w") # w : write . mengizinkan nama file yang sama namun di overwrite
b.write("New line in the file\nini baris baru lagi")
b.close()

d = open("File Handling/File 2.txt", "a") # a : append , menambahkan line baru pada file
d.write("\nIni line baru dari append")

d.close()

r = open("File Handling/File 2.txt", "r")

print(r.read())

r.close()
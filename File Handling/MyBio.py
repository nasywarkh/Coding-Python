file = open('File Handling/My Bio.txt', 'w')

text = "Halo nama saya Nasywa Rana Khairiyah\n"
file.write(text)

file.close()

file2 = open('File Handling/My Bio.txt', "a")

text = "Hobi saya berkuda"
file2.write(text)

file2.close()

file3 = open('File Handling/My Bio.txt', 'r')
print(file3.read())
file3.close()
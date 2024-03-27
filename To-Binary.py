number = 27

to_binary = bin(number)

print(to_binary)

to_binary2 = bin(number).replace("0b", "")
print(to_binary2)
print(type(to_binary2))
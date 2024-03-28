transport = {"Car", "Motor", "Train", "Airplane", "Helikopter"}
print(transport)
print(type(transport))

himpunan = {34, 65, 87, 23, 99}
print(himpunan)
print(type(himpunan))

# print(transport[0]) # error 

for trans in transport:
    print(trans)

# transport[0] = "Ship" # error 
    
transport.add("Ship")
print(transport)

transport.discard("Motor")
print(transport)

transport.discard("XX")
print(transport)

transport.remove("Train")
print(transport)

# transport.remove("XX")
# print(transport)

transport.pop()
print(transport)

print(50 * "=")
# Set Manipulation
negara = {"Singapura", "Turki", "Thailand", "Malaysia"}

negara_set = {"Jerman", "Jepang", "Korea"}
negara_list = {"India", "Filipina"}

negara.update(negara_set)
print(negara)

negara.update(negara_list)
print(negara)

print(50 * "=")
# Set Constructor
cars = set(("Honda", "Hyundai", "Volvo"))
print(cars)
print(type(cars))

text = set("python")
print(text)
print(type(text))


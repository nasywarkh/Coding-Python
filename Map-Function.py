def up_name(name) :
    return name.upper()

names = ["Alhazen", "Karim", "Fitri", "Fatih"]

proper_name = []
for name in names: 
    proper_name.append(up_name(name))

print(proper_name)

print("=====Map Function=====")
upper_name = map(up_name, names)
print(list(upper_name))

def kuadrat(x):
    return x * x

numbers = [1,2,3,4,5,6]
hasil = list(map(kuadrat, numbers))
print(hasil)


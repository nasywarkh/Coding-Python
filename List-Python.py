numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)
print(type(numbers))
print(len(numbers))

cars = ["Toyota", "Honda", "Volvo"]
print(cars)
print(type(cars))
print(len(cars))

print(50 * "=")
# Access List Item
print(numbers[3])
print(numbers[0:3])
print(numbers[3:7])
print(numbers[-1])

print(50 * "=")
# Append List
animals = ["Cat", "Fish", "Panda", "Frog"]
print(animals)
animals.append("Bird")
animals.append("Ant")
print(animals)
print(len(animals))
print(animals[0])
print(animals[5])

# Change List
animals[0] = "Dog"
animals[4] = "Mouse"
print(animals)

# Remove List
animals.remove("Frog")
print(animals)
animals.pop()
print(animals)

# Clear List
animals.clear()
print(animals)

# List Constructor
fruits = list(("Banana", "Apple", "Durian"))
print(fruits)

name = list("Ahmad")
print(name)

name2 = list(("Ahmad",))
print(name2)


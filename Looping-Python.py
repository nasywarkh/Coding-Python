number = 1

while number < 101:
    print("I like Python")
    number += 1 # number = number + 1 

# For Loop
print(50*"=")

names = ["Ahmad", "Fatih", "syafiq", "Umar"]

for name in names:
    print(name)

for i in range(10):
    print('Hello World!')

# Loop Break
print(50*"=")
n = 1 

while n <= 10:
    print(n)
    if n == 3:
        break
    n += 2

print(50*"=")
for angka in range(1,10,2): # start 1, end = (10-1), step = 1
    print(angka)
    if angka == 5:
        break



# Loop Continue
print(50*"=")
print("Loop Continue")

a = 0

while a <= 10:
    a += 1
    if a == 3:
        continue
    print(a)

# Loop Else
print(50*"=")
print("Loop - Else")

name = "Alhazen"

for letter in name:
    print(letter)
else:
    print(f'{name} letters are printed')

print(50*"=")
i = 1

while i <= 10:
    print(i)
    i += 1
else:
    print("all numbers are printed")

# Loop - Pass
print(50*"=")
print("Loop - Pass")

for i in range(10):
    pass

# Nested Loop
print(50*"=")
print("Nested Loop")

fruits = ["Apple", "Banana", "Cherry"]
colors = ["Green", "Red", "Yellow"]

for color in colors:
    for fruit in fruits:
        print(f'{color} {fruit}')
def greeting():
    print('Halo...')

greeting()
greeting()
greeting()

def numb1to101():
    numbers = list(range(1,101))
    print(numbers)

numb1to101()

print(50*"=")
print("Function Argumemt")

def sayHello(name):
    print(f'Hello {name}')

name = "Budi"
sayHello(name)
sayHello('Kiki')


print(50*"=")
print("Return or Print")

def addition(num1, num2):
    result = num1 + num2
    return result

num1 = 3
num2 = 5
add1 = addition(num1, num2)
print(f'{num1} + {num2} = {add1}')

r = add1 + 8
print(r)

def tableAddition(num1, num2):
    result = num1 + num2
    return f'{num1} + {num2} = {result}'

num1 = int(input("Enter Number: "))
loop = int(input("Enter how many loops : "))

for i in range(1,loop+1):
    print(tableAddition(num1,i))


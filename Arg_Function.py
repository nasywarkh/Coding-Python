def addition(a, b):
    add = a + b
    result = f"{a} + {b} = {add}"
    print(result)

addition(10, 9)

def addition2(*numbers):
    result = 0
    for num in numbers:
        result += num

    print(result)

addition2(1,3,5,7,8,9,10)

print("===Keyword Argument===")

def fullname(fname, lname):
    print(f"Your fullname is: ", end= "")
    print(fname, lname)

fullname(lname='Al Faruq', fname='Fatih')

print("Arbitrary Keyword Argument")
def fullname2(**fullname):
    result = fullname.values()
    print(" ".join(result))

fullname2(
    fname = "Sal", 
    mname = "Nur",
    lname = "Aqidah"
)

print("===Default Value===")
def sayHello(name, message="Hello"):
    print(message, name, "!")

sayHello("Syafiq")
sayHello("Syafiq", "Hai")
sayHello(name="Humaira", message="Assalamualaikum")





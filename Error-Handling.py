student = {
    "name" : "Jhon",
    "address" : "Jakarta"
}

try:
    print(stdnt)
except:
    print("An Error Occured")

print('code selanjutnya')

print(50*"=")
print("Many Exception")

try:
    print(studnt)
except NameError:
    print("Variable not defined")
except:
    print("An Error Occured")
else:
    print("Success")

print(50*"=")
print("Else Exception")

try:
    print(student)
except NameError:
    print("Variable not defined")
except:
    print("An Error Occured")
else:
    print("Success")

print(50*"=")
print("Finally Exception")

try:
    print(student)
except NameError:
    print("Variable not defined")
except:
    print("An Error Occured")
else:
    print("Success")
finally:
    print("Script has run!")

print(50*"=")
print("Raise Exception")
loop = int(input("Enter a number : "))
try:
    if loop <= 1:
        raise Exception("Number must be > 1")
    else:
        for i in range(loop):
            print(i)
except Exception as e:
    print(e)

    

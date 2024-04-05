def countDown(number):
    print(number)
    if number == 0:
        return
    else:
        countDown(number-1)

countDown(10)

print("==========")
for i in range(10,-1,-1):
    print(i)


print("Faktorial")
def factorial(number):
    if number <= 0:
        return 1
    else:
        result = number * factorial(number-1)
        return result
    
print(factorial(3))
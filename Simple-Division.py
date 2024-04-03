try:
    num1 = float(input("Enter the first number"))
    num2 = float(input("Enter the second number"))

    if num2 == 0:
        raise ZeroDivisionError("Error : Cannot divide by zero")
    result = num1/num2
    print(result)
except ZeroDivisionError as e:
    print(e)
except ValueError:
    print("Error : please enter valid number only")
except:
    print("An error occured")
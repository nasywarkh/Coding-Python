from functools import reduce

def addition(number1, number2):
    return number1 + number2

numbers = range(1,11)
hasil = reduce(addition, numbers)

print(hasil)

def max(x,y):
    return x if x > y else y

num_list = [30, 89, 23, 80, 44]
n_max = reduce(max, num_list)
print(n_max)


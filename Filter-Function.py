def even_nums(numbers):
    even_num = []
    for num in numbers:
        if num % 2 == 0:
            even_num.append(num)

    print(even_num)

numbers = range(1,101)
even_nums(numbers)

print("=====Filter Function=====")
def is_even(n):
    return n % 2 == 0

even_numbers = filter(is_even, numbers)
print(list(even_numbers))

odd_numbers = filter(lambda n : n % 2 == 1, numbers)
print(list(odd_numbers))
start = int(input("Start Number :"))
end = int(input("End Number :"))
choice = input("Even / Odd :").lower()

if choice == "even":
    print("Even numbers in the range: ")
    for i in range(start, end):
        if i % 2 == 0:
            print(i)
elif choice == "odd":
    print("Odd numbers in the range: ")
    for i in range(start, end):
        if i % 2 != 0:
            print(i)
else:
    print("Invalid Choice! Please enter 'even' or 'odd'")
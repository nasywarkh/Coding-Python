today = "sunny"

print(today == "sunny")

if today == "sunny":
    print("I don't have use umbrella")

status_battery = "full"

print(status_battery == "low")

if status_battery == "low":
    print("Your battery is low..")
    print("Please, charger your battery..")
else:
    print("Device turning on..")

print(50*"=")
print("Input your grade : A/B/C")
grade = input().upper()

if grade == "A":
    print("Congratulations")
elif grade == "B":
    print("Good Job!")
elif grade == "C":
    print("Good luck next time..")
else:
    print("Wrong Input")

# if - and statement
    print(50*"=")
    print("IF - AND")

score = 50

if score > 85 and score <= 100:
    print("Grade A")
elif score > 70 and score < 85:
    print("Grade B")
elif score > 40 and score < 70:
    print("Grade C")

# if - or statement
    print(50*"=")
    print("IF - OR")

money = 50000

if money == 50000 or money > 50000:
    print("Buy Programming Book")
else:
    print("Save more money!")

# Nested if
    print(50*"=")
    print("Nested IF")

age = 18
driver_license = False

if age > 17:
    print("User is teenager")
    if driver_license == True:
        print("And driving is allowed")
    else:
        print("But driving is not allowed")

    print("Done")    
else:
    print("User is not yet a teenager")


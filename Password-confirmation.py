import re
from stringcolor import *
print("Account Registration")
print("====================")

firstname = input("Your first name :\n")
lastname = input("Your last name:\n")
email = input("Your active email:\n")
password = input("Your password:\n")


# while password doesn't contain any of rules
while not re.fullmatch(r"[A-Za-z0-9]{8,}", password):
    print("Your password must be:")
    print("At least 8 charcater")
    print("At least has one uppercase letter")
    print("At least has one lowercase letter")
    password = input("Your password must be:\n")
else:
    print(cs("Welcome to the social media", "green"))
    print("Your name is", cs(f"{firstname} {lastname}", "blue"))


items = ["Milk", "Bread", "Sugar", "Meat", "Cheese"]

cartList = [] # global variable

def buy(item):
    global cartList
    cartList.append(item)

print("Grocery List: ")
for item in items:
    print("-", item)

while True:
    item = input("Enter an item to add the grocery list (or type 'done' to finish) : ")
    if item.lower() == 'done':
        break

    if item in items:
        buy(item)
    else:
        print("Item not found in the grocery list")
        continue

print("Your Cart")
for item in cartList:
    print("-", item)

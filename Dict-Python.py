student1 = {
    "name" : "Ahmad",
    "age" : 14,
    "address" : "Jakarta",
    "gender" : "Male"
}

print(student1)
print(type(student1))
print(len(student1))

print(student1.keys())

print(student1["age"])
print(student1["gender"])

# add new item
student1["email"] = "ahmad@mail.test"
print(student1)

# modify item
student1["address"] = "Tangerang"
print(student1)

student1.update({"age" : 15,
                  "email" : ["ahmad2@mail.test", "ahmad@mail.com"]})
print(student1)

# remove specific item
student1.pop("gender")
print(student1)

# remove last item
student1.popitem()
print(student1)

print(50 * "=")
# Dict Costructor

student2 = dict(name = "Fatih", grade = 10, address = "Bekasi")

print(student2)
print(type(student2))

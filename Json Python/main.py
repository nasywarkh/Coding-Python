import json

employee_string = '''
{
  "firstName" : "Fatih",
  "lastName" : "Al Faruq",
  "age" : 25,
  "hobbies" : ["swimming", "archery"]
}
'''

print(employee_string)

# serialize json
data = {
    "employees" :
    [
        {
            "firstName" : "Jhon",
            "lastName" : "Doe"
        },
        {
            "firstName" : "Hamzah",
            "lastName" : "Abdul Hakim"
        },
        {
            "firstName" : "Humaira",
            "lastName" : "Qonita"
        }
    ]
}

print(data)
print(type(data))

with open("Json Python/data_file.json", "w") as file:
    json.dump(data, file, indent=2)

print(json.dumps(data, indent=4))
print(type(json.dumps(data, indent=4)))

print(100*"=")
print("Deserialize Json")

employee_dict = json.loads(employee_string)
print(employee_dict)
print(type(employee_dict))
print(employee_dict["hobbies"])

with open("Json Python/data_file.json", "r") as file:
    py_data = json.load(file)

print(py_data)
print(type(py_data))
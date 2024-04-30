import json

with open("Json Python/Data-capital-of-jakarta.json", "r") as file:
    data_jkt = json.load(file)

print(json.dumps(data_jkt, indent=4))
print(type(data_jkt))
print(data_jkt[0]["independent"])
print(data_jkt[0]["region"])
print(data_jkt[0]["languages"]["ind"])
print(data_jkt[0]["name"]["official"])
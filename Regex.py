import re

text = "The quick brown fox"
text += " jumps over 56 lazy dogs!"

x = re.findall(r"\d", text)
print(x)

pattern = "[a-zA-Z]"
y = re.findall(rf"{pattern}", text)
print(y)

z = re.findall(r"cat", text)
print(z)

x = re.search(r"\d", text)
print(x)
print(x.span())
print(x.group())

x = re.split(r"\s", text, 2)
print(x)

x = re.sub(r"\s", "-", text)
print(x)

twit = "aku sedang belajar :)"
y = re.sub(r":\)", "senang", twit)
print(y)
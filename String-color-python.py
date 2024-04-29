from stringcolor import * 

text = "Hello Wolrd"
colors = ["red","blue","green"]

for color in colors:
    print(cs(text,color, "#ffff87").bold().underline())
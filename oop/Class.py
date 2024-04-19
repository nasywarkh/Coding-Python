class Animal:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def makeSound(self, sound):
        print(f"{self.name} is making {sound}")

    def eat(self, food):
        print(f"{self.name} with color {self.color} is eating {food}")

cat = Animal("Kitty", "Black")
print(cat.name)
print(cat.color)
cat.makeSound("miaowing")
cat.eat("fish")

panda = Animal("Panda", "Black White")
print(panda.name)
print(panda.color)
panda.makeSound("bleating")
panda.eat("bamboo")



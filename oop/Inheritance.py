class Person:
    def __init__(self, name):
        self.name = name

    def getInfo(self):
        print(f"This person's name {self.name}")

class Student(Person):
    def __init__(self, name, nis):
        super().__init__(name)
        self.nis = nis

    def study(self, subject):
        print(f"{self.name} NIS: {self.nis} is studying {subject}")

    def getInfo(self):
        print(f"This student's name {self.name} with NIS {self.nis}")

person1 = Person("Joko")
person1.getInfo()

student1 = Student("Ahmad", "20230101")
student1.getInfo()

student2 = Student("Malik", "20230102")
student2.getInfo()
student2.study("Math")
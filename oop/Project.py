class Student:
    def __init__(self, name, address, phoneNumber):
        self.name = name
        self.address = address
        self.phoneNumber = phoneNumber
    
    def welcomeStudent(self):
        print("Welcome to our course\n")
        print("Name :", self.name)
        print("address :", self.address)
        print("phoneNumber :", self.phoneNumber)

object1 = Student("Ahmad", "Jakarta", "0899")
object1.welcomeStudent()

object2 = Student("Alhazen", "Tangerang", "0988")
object2.welcomeStudent()

object3 = Student("Jack", "Bogor", "0799")
object3.welcomeStudent()


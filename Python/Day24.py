
class Student:
    collegename = "Codegnan"
    def __init__(self):
        self.name = "Siddhu"
        self.age = 22
        self.marks = 90
    #Instance method
    def Talk(self):
        print("My name is:",self.name)
        print("My age is:",self.age)
        print("My marks are:",self.marks)
s1=Student()
s1.Talk()
print()
s2=Student()
s2.Talk()

#Class method
class Student:
    college = "CBIT"

    @classmethod
    def show_college(cls):
        print(cls.college)

Student.show_college()


#Static Method
class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

print(Calculator.add(5,10))


#Constructor
class Student:
    def __init__(self):
        print("Object created")

s1 = Student()

#Non Parameterized constructor
class Student:
    def __init__(self):
        self.name = "Siddhartha"

s1 = Student()
print(s1.name)


#Parameterized constructor
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

s1 = Student("Siddhartha", 23, 90)
print(s1.name)
print(s1.age)
print(s1.marks)
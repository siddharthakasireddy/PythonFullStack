class Student:
    def __init__(self):
        print("I am no parameterized constructor")
        print("Address of self:",id(self))
        
s1 = Student()
print("Address of s1:",id(s1))


class Student:
    def __init__(self):
        print("I am no parameterized constructor")
        print("Address of self:",id(self))
        
s1 = Student()
print("Address of s1:",id(s1))
s2 = Student()
print("Address of s2:",id(s2))


#Instance variable
class Student:
    def __init__(self):
        self.name="siddhu"
        self.age=23
        print("My name is:",self.name)
        print("My age is:",self.age)
        
s1 = Student()
print("My name outside class is:",s1.name)
print("My age outside class is:",s1.age)


#Class variable
class Student:
    collegename="codegnan"
    def __init__(self):
        self.name="siddhu"
        self.age=23
        print("My name is:",self.name)
        print("My age is:",self.age)
        print("My college name is:",Student.collegename)
        
s1 = Student()
print("My name outside class is:",s1.name)
print("My age outside class is:",s1.age)
print(Student.collegename)
print(s1.collegename)


class Test:
    def __init__(self):
        x=10 #Local Variable
        print("Variable value is:",x)
        
t1=Test()

def greet():
    print("Hello, Python!")

greet()

def add(): #Function without parameters
    a = 10
    b = 20
    print(a + b)

add()

def greet(name): #Function with parameters
    print("Hello", name)

greet("Siddhartha")

def add(a, b):       # a and b → parameters
    print(a + b)

add(10, 20)          # 10 and 20 → arguments


def student(name, age): #Positional arguments
    print("Name:", name)
    print("Age:", age)

student("Siddhartha", 22)


def student(name, age): #Keyword arguments
    print("Name:", name)
    print("Age:", age)

student(age=22, name="Siddhartha")


def greet(name="User"): #Default arguments
    print("Hello", name)

greet()
greet("Siddhartha")


def add(*numbers): #Variable-length arguments args*
    print(numbers)

add(10, 20, 30)

def student(**details): #Variable-length arguments kwargs**
    print(details)

student(name="Siddhartha", age=22, city="Hyderabad")

def student(name, age=22, *skills): #Positional, default and variable-length arguments
    print("Name:", name)
    print("Age:", age)
    print("Skills:", skills)

student("Siddhartha", 22, "Python", "SQL", "Git")


def add(a, b): #Return statement
    return a + b

result = add(10, 20)

print(result)

        
#Conditional Statements
#If statement
a = 10

if a > 5:
    print("Hello")

print("End")

a = 20

if a > 20:
    print("Hello")

print("End")

stock = 5

if stock > 0:
    print("Product Stock Available")
else:
    print("Product Stock Not Available")

age = int(input("Enter Age: "))

if age >= 18:
    print("Eligible for Vote")
else:
    print("Not Eligible")

print("End")


num = int(input("Enter Number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
if a > b:
    print("a is Largest")
else:
    print("b is Largest")
    
    
marks = 85

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
else:
    print("Grade C")
    
num = 0

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
    
    
units = 250

if units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = units * 2.5
elif units <= 500:
    bill = units * 4
else:
    bill = units * 6

print("Electricity Bill:", bill)

username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Wrong username")
    
balance = 10000
amount = 5000

if amount > 0:
    if amount <= balance:
        print("Withdrawal successful")
        balance = balance - amount
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance")
else:
    print("Invalid amount")

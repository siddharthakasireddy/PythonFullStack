#For loop

for i in range(1, 11):

    if i % 2 == 0:
        print(i) #Even numbers from 1 to 10


for i in range(1, 6):

    if i % 2 == 0:
        print(i)

    print("end of if")#Even numbers from 1 to 5

print("end of loop")


n = int(input("Enter a number: "))
a = 1
for i in range(1, n + 1):
    a = a * i
print("Factorial:", a) #Factorial of a number


num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i) #Multiplication table of a number
    
    

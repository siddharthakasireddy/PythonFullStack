#For else loop
for i in range(1, 6):
    print(i)
else:
    print("Loop completed")
    
#For else loop with break statement
for i in range(1, 6):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed")
    
    
#While loop
i = 1

while i <= 5:
    print(i)
    i += 1
    

#While else loop
i = 1

while i <= 5:
    print(i)
    i += 1
else:
    print("Loop completed")
    
#assert statement
age = 20

assert age >= 18

print("You are eligible")

#break statement
numbers = [10, 20, 30, 40, 50]
for num in numbers:
    if num == 30:
        break
    print(num)
    
#continue statement
for i in range(1, 6):
    if i % 2 == 0:
        continue
    print(i)
    
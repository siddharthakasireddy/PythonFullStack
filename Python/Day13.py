n = 123456
s = str(n)
count = 0
for i in s:
    if(int(i) % 2 == 0):
        count += 1
print("The number of even digits in", n, "is:", count)


n = int(input("Enter a number: "))

while n > 0:
    digit = n % 10

    if digit == 2 or digit == 3 or digit == 5 or digit == 7:
        print(digit)

    n = n // 10
    
    
l = [1, 2, 3, 4, 5]
sum = 0
for i in l:
    sum += i
print("The sum of the list is:", sum)


l = [1, 2, 3, 4, 5, 6, 7]
m = []
for i in range(len(l)-1,-1,-1):
    m.append(l[i])
print("The reversed list is:", m)


n = int(input("Enter a number: "))

s = str(n)

for i in range(0, len(s), 2):
    print(s[i], end=" ")
    
    
n = int(input("Enter a number: "))

while n > 0:
    print(n % 10, end=" ")
    n //= 100
    
    
n = int(input("Enter a number: "))
sum = 0

while n > 0:
    d = n % 10
    if d in (2, 3, 5, 7):
        sum += d
    n //= 10

print(sum)


n = int(input("Enter a number: "))
count = 0

while n > 0:
    count += 1
    n //= 10

print("Number of digits:", count)


n = int(input("Enter a number: "))

temp = n
count = 0

while temp > 0:
    count += 1
    temp //= 10

if count % 2 == 1:
    middle = count // 2

    for i in range(middle):
        n //= 10

    print("Middle digit:", n % 10)
else:
    print("Middle digit does not exist")
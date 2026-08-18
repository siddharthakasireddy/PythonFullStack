def fact(n):
    if n == 0 or n == 1:       # Base case
        return 1
    else:
        return n * fact(n - 1)  # Recursive case


n = int(input("Enter a number: "))
print("Factorial:", fact(n))


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter number of terms: "))

for i in range(n):
    print(fibonacci(i), end=" ")



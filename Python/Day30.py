a = 10
b = 2
print("Execution started")
print(a + b)
print(a - b)
print(a * b)
try:
    print(a / 0)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
print('Execution completed.')



try:
    print("Execution started")
    a = int(input("Enter a value: "))
    b = int(input("Enter b value: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Invalid input. Please enter valid integers.")
print('Execution completed.')


try:
    print("Execution started")
    a = int(input("Enter a value: "))
    b = int(input("Enter b value: "))
    result = a / b
    print("Result:", result)
except (ZeroDivisionError, ValueError) as e:
    print(e)
print('Execution completed.')


try:
    print("Execution started")
    a = int(input("Enter a value: "))
    b = int(input("Enter b value: "))
    result = a / b
    print("Result:", result)
except (ZeroDivisionError, ValueError) as e:
    print(e)
else:
    print("No exceptions occurred.")
print('Execution completed.')


try:
    print("Execution started")
    a = int(input("Enter a value: "))
    print("The value of a is:", a)
except ZeroDivisionError as e:
    print(e)
finally:
    print("I am getting executed.")
    





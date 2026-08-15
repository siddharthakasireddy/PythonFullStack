def my_function(): #Local Scope
    x = 10
    print(x)

my_function()

x = 100 #Global Scope
def my_function():
    print(x)

my_function()
print(x)

x = 10

def change(): #Global Keyword
    global x
    x = 20

change()

print(x)

def outer(): #Non-local Scope
    x = 10

    def inner():
        nonlocal x
        x = 20

    inner()
    print(x)

outer()

print("Hello") #Built-in Scope
len("Python")
max(10, 20, 30)
min(10, 20, 30)
sum([1, 2, 3])

x = "Global" #Local, Enclosing, Global, Built-in (LEGB) Rule

def outer():
    x = "Enclosing"

    def inner():
        x = "Local"
        print(x)

    inner()

outer()


square = lambda x: x * x #Lambda Function
print(square(5))

add = lambda a, b: a + b
print(add(10, 20))

numbers = [1, 2, 3, 4, 5] #map() Function
result = map(lambda x: x * x, numbers)
print(list(result))


numbers = [1, 2, 3, 4, 5, 6] #filter() Function
result = filter(lambda x: x % 2 == 0, numbers)
print(list(result))


from functools import reduce #reduce() Function
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda a, b: a + b, numbers)
print(result)
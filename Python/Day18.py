#Generators
def simple_gen():
    yield 1
    yield 2
    yield 3
    yield 4

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(5):
    print(num)
    

#List Comprehensions
squares = [x**2 for x in range(10)]
print(squares)

numbers = [1, 2, 3, 4, 5, 6]
evens = [n for n in numbers if n % 2 == 0]
print(evens)


names = ["sairam", "raju", "raghu", "gokul"]
upper_names = [name.upper() for name in names]
print(upper_names)

products = ["laptop", "phone", "tablet", "monitor"]
upper_products = [p.upper() for p in products]
print(upper_products)

prices = [1000, 800, 450, 300]
discounted_prices = [price * 0.9 for price in prices]
print(discounted_prices)

in_stock = [True, False, True, False]
out_of_stock = [not item for item in in_stock]
print(out_of_stock)

products_data = [{"name": "Laptop", "price": 1000, "stock": 3},{"name": "Phone", "price": 800, "stock": 0},{"name": "Tablet", "price": 450, "stock": 5}]
available_names = [p["name"] for p in products_data if p["stock"] > 0]
print(available_names)

#Nested List Comprehensions
products_colors = [{"name": "Laptop", "colors": ["Silver", "Black"]},{"name": "Phone", "colors": ["Gold", "Blue"]}]
all_colors = [color for product in products_colors for color in product["colors"]]
print(all_colors)

m = [["apple", "banana", "cherry"], ["date", "fig", "grape"], ["kiwi", "lemon", "mango"]]
mod_m = [[f.capitalize() for f in r] for r in m]
print(mod_m)

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
odds = [e for r in m for e in r if e % 2 != 0]
print(odds)
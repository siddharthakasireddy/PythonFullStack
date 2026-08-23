prem = 10000

age = int(input())
score = int(input())
v_type = input().strip().lower()

price = prem

# Age factor
if age < 25:
    price = price + (price * 0.20)
elif 25 <= age <= 50:
    price = price
else:
    price = price + (price * 0.15)

# Health score factor
if score >= 80:
    price = price - (price * 0.10)
elif 60 <= score <= 79:
    price = price
else:
    price = price + (price * 0.20)

# Vehicle type factor
if v_type == "sports":
    price = price + (price * 0.30)
elif v_type == "suv":
    price = price + (price * 0.15)
elif v_type == "sedan":
    price = price

print(price)
    
    

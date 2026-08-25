#Method Overloading
class Greet:
    def Hello(self,name=None):
        if name:
            print("Hello",name)
        else:
            print("Hello")
g=Greet()
g.Hello("Siddhu")

class Test:
    def Add(self, *l):
        sum = 0
        for i in l:
            sum=sum+i
        print(f"the sum is {sum}")
t = Test()
t.Add(10)
t.Add(10,20)
t.Add(10,20,30)

#Constructor Overloading
class Test:
    def __init__(self):
        print("no args constructor")
    def __init__(self,a):
        print("one args constructor")
t = Test(10)

#Method Overriding
class A:
    def Employee(self):
        print("This is Employee")
class B(A):
    def Employee(self):
        print("This is Employee ID")
        
b=B()
b.Employee()

class Shop:
    def Calculatebill(self,a,b=0):
        total=a+b
        print(f"total bill(no discount): {total}")
s=Shop()
s.Calculatebill(100)
        
        
class Shop:
    def Calculatebill(self,a,b=0):
        total=a+b
        print(f"total bill(no discount): {total}")
class Specialcustomer(Shop):
    def Calculatebill(self,a,b=0):
            total=a+b
            discount=total*0.1
            totalamount=total-discount
            print(f"total bill(with discount): {totalamount}")
s=Specialcustomer()
s.Calculatebill(100,300)

#Constructor overriding
class Parent:
    def __init__(self):
        print("Parent constructor")
        
class Child(Parent):
    def __init__(self):
        print("Child constructor")
        
obj = Child()

#Operator overloading
class Book:
    def __init__(self,pages):
        self.pages = pages
    def __add__(self, other):
        return Book(self.pages+other.pages)
    def __mul__(self, other):
        return Book(self.pages*other.pages)
    def __str__(self):
        return str(self.pages)
    
b1 = Book(100)
b2 = Book(200)
print(b1+b2)
print(b1*b2)
        
    

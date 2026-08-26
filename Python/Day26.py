#Single Inheritance
class Animal:
    def sound(self):
        print("animal is making sound!")
class dog(Animal):
    def barking(self):
        print("dog is barking!")
d=dog()
d.barking()
d.sound()
a=Animal()
a.sound()

#Multiple Inheritance
class Father:
    def skill1(self):
        print("Father: Cooking")

class Mother:
    def skill2(self):
        print("Mother: Dancing")

class Child(Father, Mother):
    def skill3(self):
        print("Child: Singing")

c = Child()
c.skill1()
c.skill2()
c.skill3()

#Multilevel Inheritance
class animal:
    def eat(self):
        print("eating")
class dog(animal):
    def bark(self):
        print("barking")
class babydog(dog):
    def cry(self):
        print("crying")
b=babydog()
b.cry()
b.bark()
b.eat()

#Hierarchical Inheritance
class Vehicle:
    def fuel_type(self):
        print("Uses fuel or battery")

class Car(Vehicle):
    def drive(self):
        print("Driving the car")

class Bike(Vehicle):
    def ride(self):
        print("Riding the bike")
c = Car()
b = Bike()

c.fuel_type()
c.drive()

b.fuel_type()
b.ride()

#Hybrid Inheritance
class A:
    def m1(self):
        print("m1 method in A class")
class B(A):
    def m2(self):
        print("m2 method in B class")
class C(A):
    def m3(self):
        print("m3 method in C class")
class D(B,C):
    def m4(self):
        print("m4 method in D class")

d=D()
d.m4()
d.m2()

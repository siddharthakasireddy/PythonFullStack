from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

# Concrete class
class Car(Vehicle):

    def start_engine(self):
        print("Car engine started")

    def stop_engine(self):
        print("Car engine stopped")

my_car = Car()
my_car.start_engine()
my_car.stop_engine()

from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def loan_interest(self):
        pass

class SBI(Bank):
    def loan_interest(self):
        print("SBI interest rate is 8%")

class HDFC(Bank):
    def loan_interest(self):
        print("HDFC interest rate is 10%")

bank1 = SBI()
bank2 = HDFC()

bank1.loan_interest()
bank2.loan_interest()

from abc import ABC, abstractmethod

# Abstract class
class ATM(ABC):
    
    @abstractmethod
    def check_balance(self):
        pass
    
    @abstractmethod
    def withdraw(self, amount):
        pass
    
    @abstractmethod
    def deposit(self, amount):
        pass

    # Concrete method
    def welcome(self):
        print("Welcome to Smart ATM!")

# Concrete class
class UserAccount(ATM):
    def __init__(self, name, pin, balance):
        self.name = name
        self.__pin = pin              # Private attribute
        self.__balance = balance      # Private attribute

    def authenticate(self, pin_input):
        return self.__pin == pin_input

    def check_balance(self):
        print(f"Your current balance is: ₹{self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")
            self.check_balance()

    def deposit(self, amount):
        self.__balance += amount
        print(f"₹{amount} deposited successfully.")
        self.check_balance()


user1 = UserAccount("Siddhu", 1234, 5000)

user1.welcome()
pin = int(input("Enter your 4-digit PIN: "))

if user1.authenticate(pin):
    print(f"Hello, {user1.name}!\n")
    while True:
        print("\nChoose an option:")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            user1.check_balance()
        elif choice == '2':
            amt = float(input("Enter amount to withdraw: "))
            user1.withdraw(amt)
        elif choice == '3':
            amt = float(input("Enter amount to deposit: "))
            user1.deposit(amt)
        elif choice == '4':
            print("Thank you for using the ATM!")
            break
        else:
            print("Invalid choice. Please try again.")
else:
    print("Authentication failed! Invalid PIN.")

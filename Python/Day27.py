class BankAccount:
    def __init__(self, name, balance):
        self.name = name               # public attribute
        self.__balance = balance       # private attribute (encapsulated)
        
    # Public method to display balance
    def show_balance(self):
        print(f"{self.name}, your balance is ₹{self.__balance}")
        
    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")
            
    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")

account = BankAccount("Siddhu", 5000)

account.show_balance()     #Access through method
account.deposit(2000)
account.withdraw(1000)
account.show_balance()


class BankAccount:
    def __init__(self, name, acc_number, balance):
        self.name = name                     # public attribute
        self.__acc_number = acc_number       # private attribute
        self.__balance = balance             # private attribute

    # Method to validate account number
    def __is_valid_account(self, acc_number):
        return self.__acc_number == acc_number

    # Getter method
    def show_balance(self, acc_number):
        if self.__is_valid_account(acc_number):
            print(f"{self.name}, your balance is ₹{self.__balance}")
        else:
            print("Invalid account number.")

    # Setter method - deposit
    def deposit(self, acc_number, amount):
        if self.__is_valid_account(acc_number):
            if amount > 0:
                self.__balance += amount
                print(f"₹{amount} deposited successfully.")
            else:
                print("Invalid deposit amount.")
        else:
            print("Invalid account number.")

    # Setter method - withdraw
    def withdraw(self, acc_number, amount):
        if self.__is_valid_account(acc_number):
            if 0 < amount <= self.__balance:
                self.__balance -= amount
                print(f"₹{amount} withdrawn successfully.")
            else:
                print("Insufficient balance or invalid amount.")
        else:
            print("Invalid account number.")

account = BankAccount("Siddhu", "ACC123", 5000)

account.show_balance("ACC123")
account.deposit("ACC123", 2000)
account.withdraw("ACC123", 1000)
account.show_balance("ACC123")

account.withdraw("ACC1123", 100)


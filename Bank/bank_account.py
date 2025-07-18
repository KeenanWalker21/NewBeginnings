import time
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Bank:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"Deposited: {amount}")
        print(f"${amount} deposited.")

    def withdraw(self, amount):
        if amount > self.balance:
            self.history.append(f"Failed Withdrawal: ${amount}")
            print("Insufficient Balance")
        else:
            self.balance -= amount
            self.history.append(f"Withdrew: ${amount}")
            print(f"${amount} withdrawn.")

    def show_balance(self):
        print(f"{self.owner}'s Balance: ${self.balance}")

    def show_history(self):
        print("--------------------Transaction History--------------------\n")
        if not self.history:
            print("No Transactions Yet")
        else:
            for i, entry in enumerate(self.history, 1):
                print(f"{i}. {entry}")


clear_screen()
name = input("Welcome New Guest!! Please enter your name:\n").capitalize()
clear_screen()
start = float(input("Enter your starting amount: $"))

account = Bank(name, start)

while True:
    clear_screen()
    print("--------------------Welcome to the Bank--------------------")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Show History")
    print("5. Exit")

    choice = input("\nChoose your option: ")

    if choice == '1':
        clear_screen()
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
        time.sleep(2)
    elif choice == '2':
        clear_screen()
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
        time.sleep(2)
    elif choice == '3':
        clear_screen()
        account.show_balance()
        time.sleep(2)
    elif choice == '4':
        clear_screen()
        account.show_history()
        input("Press enter to continue")
    elif choice == '5':
        clear_screen()
        print("Goodbye!")
        time.sleep(2)
        break
    else:
        print("Invalid Option. Try Again")
        time.sleep(1.5)

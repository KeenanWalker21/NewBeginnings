import random as r
import os
import time


def clear_screen():
    os.system("cls" if os.name == 'nt' else 'clear')


def shuffle():
    print("On shoot!")
    time.sleep(1.2)
    clear_screen()
    print("Rock...✊")
    time.sleep(1.2)
    clear_screen()
    print("Paper...🖐️")
    time.sleep(1.2)
    clear_screen()
    print("Scissors...✌️")
    time.sleep(1.2)
    clear_screen()
    print("Shoot!🔫 ")
    time.sleep(1.2)
    clear_screen()


choices = ['rock', 'paper', 'scissors']


def getuser_choice():
    clear_screen()
    return input("Enter your choice (Rock/Paper/Scissors) or 'q' to quit:\n").lower()


def getsystem_choice():
    return r.choice(choices)


def winner(user_choice, system_choice):
    if user_choice == system_choice:
        return "Its a tie!!"
    elif user_choice == 'rock' and system_choice == 'scissors' or user_choice == 'paper' and system_choice == 'rock' or user_choice == 'scissors' and system_choice == 'paper':
        return "You Win!!"
    else:
        return "System Wins"


while True:
    user_choice = getuser_choice()
    if user_choice == 'q':
        clear_screen()
        print("Thanks for playing!")
        break
    if user_choice not in choices:
        print("Invalid choice...")
        time.sleep(1.5)
    else:
        shuffle()
        system_choice = getsystem_choice()
        print(f"User: {user_choice}\t\tSystem: {system_choice}")
        time.sleep(1.2)
        clear_screen()
        print(winner(user_choice, system_choice))
        time.sleep(1.5)
        input("\nPress enter to play again...")

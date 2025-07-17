import os
import time


class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def speak(self):
        if self.species.lower() == 'dog':
            print("Woof!")
        elif self.species.lower() == 'cat':
            print("Meow!")
        else:
            print("I'm a silent creature!")

    def birthday(self):
        self.age += 1
        print(f"🎉Happy Birthday {self.name}!🎉")
        print(f"{self.name} is now {self.age} years old!")

    def showinfo(self):
        print(f"{self.name}\t{self.species}\t{self.age}")


def clear_screen():
    os.system("cls" if os.name == 'nt' else 'clear')


pet_list = []


while True:
    clear_screen()
    print("--------------------Welcome to the Pet Hotel!--------------------")
    choice = input(
        "1. Store A New Pet 🐶\n2. Current Pets 🐕\n3. Celebrate Birthday 🎉\n4. Checkout A Pet 🚪\n5. Exit 👋\n")

    if choice == "1":
        clear_screen()
        name = input("Enter your pet's name: ")
        species = input("Enter your pet species: ")
        age = int(input("Enter your pet's age: "))

        new_pet = Pet(name.capitalize(), species.capitalize(), age)
        pet_list.append(new_pet)

        print(f"{name.capitalize()} has been added to the Pet Hotel")
        time.sleep(2)

    elif choice == '2':
        clear_screen()
        if not pet_list:
            print("No pets stored yet")
        else:
            for i, pet in enumerate(pet_list, 1):
                print("--------------------------")
                print(f"#{i}:")
                pet.showinfo()
                pet.speak()
        input("\nPress enter to return to menu")

    elif choice == '3':
        clear_screen()
        name = input("Who's birthday is it?!\n").capitalize()
        found = False
        for pet in pet_list:
            if pet.name == name:
                pet.birthday()
                found = True
                break
        if not found:
            print(f"No pet named {name} found.")
        time.sleep(2)

    elif choice == '4':
        clear_screen()
        name = input("Who would you like to checkout?\n").capitalize()
        found = False
        for pet in pet_list:
            if pet.name == name:
                pet_list.remove(pet)
                print(f"Bye {name.capitalize()}! See you next time")
                time.sleep(2)
                found = True
                break
        if not found:
            print("No pet found by that name...")
            time.sleep(2)

    elif choice == '5':
        print("Goodbye!")
        break

    else:
        print("Invalid entry. Try again.")
        time.sleep(2)

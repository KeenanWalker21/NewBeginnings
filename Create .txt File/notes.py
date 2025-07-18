import os
import time


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def new_note():
    with open("notes.txt", "w") as file:
        print("\nCreate your note. Type 'done' on a new line to finish:\n")
        while True:
            line = input()
            if line.lower() == 'done':
                break
            else:
                file.write(line + '\n')


def addto_note():
    with open("notes.txt", "a") as file:
        print("\nCreate your note. Type 'done' on a new line to finish:\n")
        while True:
            line = input()
            if line.lower() == 'done':
                break
            else:
                file.write(line + '\n')


def view_note():
    with open("notes.txt", 'r') as file:
        content = file.read()
        print(content)


def delete_note():
    if os.path.exists("notes.txt"):
        os.remove("notes.txt")
        print("Note Deleted...")
    else:
        print("No notes found to remove")


while True:
    clear_screen()
    print("1. New Note")
    print("2. Add to Note")
    print("3. View Note")
    print("4. Delete Note")
    print("5. Exit")

    choice = input("Select an option: ")

    if choice == '1':
        clear_screen()
        new_note()
    elif choice == '2':
        clear_screen()
        addto_note()
    elif choice == '3':
        clear_screen()
        view_note()
        input("\n\nPress Enter when you are finished")
    elif choice == '4':
        clear_screen()
        delete_note()
        time.sleep(1.5)
    elif choice == '5':
        clear_screen()
        print("Goodbye")
        time.sleep(1.5)
        break
    else:
        print("Invalid Entry. Try again")
        time.sleep(2)

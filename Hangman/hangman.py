import time
import random
import os
from words import word_list_animals, word_list_colors, word_list_food


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def build_hang(mistakes):
    stages = [
        """
  +---+
  |   |
      |
      |
      |
      |
=========""",
        """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
        """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
        """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
        """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
        """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
        """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
========="""
    ]
    print(stages[mistakes])


def choose_category():
    categories = {
        "animals": word_list_animals,
        "colors": word_list_colors,
        "food": word_list_food
    }
    name = random.choice(list(categories.keys()))
    return name, categories[name]


# Game setup
clear_screen()
print("Welcome to Hangman!")
input("Press Enter to start...")

category_name, category_list = choose_category()
word = random.choice(category_list).lower()
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6
display_word = ["_" for _ in word]

# Game loop
while True:
    clear_screen()
    build_hang(incorrect_guesses)
    print(f"\nCategory: {category_name.capitalize()}")
    print("Word: " + " ".join(display_word))
    print("Guessed Letters:", " ".join(guessed_letters))
    print(f"Incorrect Guesses: {incorrect_guesses}/{max_attempts}")

    guess = input("\nGuess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        time.sleep(1.5)
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        time.sleep(1.5)
        continue

    guessed_letters.append(guess)

    if guess in word:
        for index, letter in enumerate(word):
            if letter == guess:
                display_word[index] = guess
    else:
        incorrect_guesses += 1

    # Check win/loss conditions
    if "_" not in display_word:
        clear_screen()
        build_hang(incorrect_guesses)
        print(f"\n🎉 Congratulations! You guessed the word: {word}")
        break
    elif incorrect_guesses >= max_attempts:
        clear_screen()
        build_hang(incorrect_guesses)
        print(f"\n💀 Game Over! The word was: {word}")
        break

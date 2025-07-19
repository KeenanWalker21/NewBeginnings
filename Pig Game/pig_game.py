import random as rand
import os
import time
import sys

def clear_screen():
    os.system("cls" if os.name == 'nt' else 'clear')


def roll_dice():
    return rand.randint(1, 6)


def intro():
    return "Welcome to the game of Pig. In this game, a player rolls a dice. Each value that is rolled is added to a player's score until the target score is reached. If a player rolls a '1', their score is reset to 0 and the turn ends. A player can roll the dice as many times as they want"


clear_screen()
print(intro())
input("Press the Enter key to continue...")
clear_screen()


def get_playercount():
    clear_screen()
    return input("Enter the number of players will be participating (1-4): ")


while True:
    players = get_playercount()
    if players.isdigit() and 1 <= int(players) <= 4:
        players = int(players)
        break
    else:
        print("Invalid, try again")

if players == 1:
    clear_screen()
    print(f"There is {players} player")
    time.sleep(1.5)
    clear_screen()
else:
    clear_screen()
    print(f"There are {players} players")
    time.sleep(1.5)
    clear_screen()

print("\nYour target score is 50\n")
time.sleep(1.5)
clear_screen()

target_score = 50
player_scores = [0 for _ in range(players)]


while max(player_scores) < 50:
    for player_index in range(players):
        clear_screen()
        print(f"\nPlayer {player_index+1} turn has just started!")
        print(f"\nYour total score is {player_scores[player_index]}\n")
        current_score = 0

        while True:
            should_roll = input("\nWould you like to roll? (y) or (n)\n")
            if should_roll.lower() == "y":
                value = roll_dice()
            else:
                break
            if value == 1:
                print("You rolled a 1! Turn done.")
                current_score = 0
                time.sleep(2)
                clear_screen()
                break
            else:
                current_score += value
                clear_screen()
                print(f"\nYou rolled a {value}!\n")
                print(f"Your current score is {current_score}!")

        player_scores[player_index] += current_score
        print(
            f"Player {player_index+1}'s total score is {player_scores[player_index]}")
        time.sleep(2)
        clear_screen()
        if player_scores[player_index] >= target_score:
            max_score = max(player_scores)
            winning_index = player_scores.index(max_score)
            print(
                f"\n🎉 Player {player_index+1} wins with a score of {player_scores[player_index]}!")
            time.sleep(2)
            clear_screen()
            print("-----------------------------SCOREBOARD-----------------------------")
            for i in range(players):
                print(f"Player {i+1} score:\t\t\t\t\t\t\t{player_scores[i]}")
            exit()

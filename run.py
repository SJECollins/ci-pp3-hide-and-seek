"""
Imports
"""
import os
import sys
import time


# Variables and objects
username = ""
pick_ups = []
window_closed = False
door_open = False
stool_out = False
shadow_delayed = False


def get_user_choice(message):
    """
    Function to take input from user
    """
    user_choice = input("\n**--------------------------------------------------\
--------------------------**\n" + message + "\n").strip().lower()
    return user_choice


def clear_terminal():
    """
    Function to clear terminal
    """
    os.system("clear")


def slowprint(text):
    """
    Prints text with delay between letters.
    Code from replit, link in credits in readme.
    """
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)


def main():
    """
    Starting function. Updates username. Prompts user to begin story.
    User can choose to say no, which prints a disappointed message and game \
    doesn't start

    """
    username = input("What's your name? \n").strip().capitalize()
    start_answer = get_user_choice(f"Hello, {username}, do you want to play a game?\
 Yes or No\n")
    if start_answer == "yes":
        print("Great. To play, enter the letter of your choice in the terminal\
.")
        user_choice = get_user_choice("Ready to start?\n\
A. Yes!\n\
B. Actually, I don't think I want to play after all...\n")
        if user_choice == "a":
            clear_terminal()
            start_room()
        else:
            print(f"That's too bad, {username}")
    else:
        print(f"Well, alright {username}. Maybe next time...")


def start_room():
    """
    Starting room. Choice to get up or go back to sleep
    """
    clear_terminal()
    slowprint("You slowly open your eyes to find yourself safely in your own bed\
. At first the room seems pitch black, except for the light from the clock on\
 your bedside table. It reads: 02:00.\n\
You don't know why, but you feel wide awake and your heart is beating hard.\n")
    while True:
        user_choice = get_user_choice("Will you:\n\
A. Get up and make a cup of tea.\n\
B. Try to go back to sleep.")
        if user_choice == "a":
            # get_up()
            break
        elif user_choice == "b":
            try_sleep()
            break
        else:
            print(f"{user_choice} isn't really an option...\n")


def try_sleep():
    """
    Try to go back to sleep. Choice to get up or keep trying to sleep
    """
    clear_terminal()
    slowprint("You have to get up for school early in the morning. So, you roll \
over in your bed and pull the covers up over your head. After a few moments \
of silence, you hear a soft rustling.\n\
Very slowly, you peek out from under your covers. In the darkness, you spy the\
 window open a crack. A light breeze is moving the curtains.\n")
    while True:
        user_choice = get_user_choice("It's chilly in your room, so you:\n\
A. Get up.\n\
B. Pull the blanket tighter and close your eyes.\n")
        if user_choice == "a":
            # get_up()
            break
        elif user_choice == "b":
            # blanket_tighter()
            break
        else:
            print(f"{user_choice} isn't really an option...\n")


main()

#!/usr/bin/env python3.8

import random


def is_valid_num(s):
    if s.isdigit() == True & 1 <= int(s) <= 100:
        return True
    else:
        return False


def game():
    number = random.randint(1, 100)
    guessed_number = False
    guess = input("Pick a number between 1 and 100: ")
    while not guessed_number:
        if not is_valid_num(guess):
            guess = input("I won't count that, please try again: ")
            continue
        else:
            guess = int(guess)

        if guess < number:
            guess = input("Too low, try again please: ")

        elif guess > number:
            guess = input("Too high, try again please: ")

        else:
            print("Congratulations, you got it!")
            guessed_number = True

    print("Thanks for playing :P")

# Program to Guess the number. The computer has a secret number and we will try to guess it.
# Take input from user a number and you have to keep guessing until it matches with random number
# computer will generate a secret number for us to guess between
# that range starting from 1. The computer will tell if it's high, low or the correct number you have 
# guessed. You need to keep looping until you get the correct answer.

import random

def guess(x):
    random_number= random.randint(1,x)
    for i in range(1,x):
        if i ==random_number:
            print(f"you guessed the right number, which is {random_number}")
        elif i<random_number:
            print(f"the number is too small")
        else:
            print(f"the number is too big")
            

            

number= int(input("Enter the number"))
guess(number)



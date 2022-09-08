# Program to Guess the number. The computer has a secret number and we will try to guess it.
# Take input from user a number and you have to keep guessing until it matches with random number
# computer will generate a secret number for us to guess between
# that range starting from 1. The computer will tell if it's high, low or the correct number you have 
# guessed. You need to keep looping until you get the correct answer.

import random

def guess(x):
    random_number= random.randint(1,x)
    y=0
    while (y!= random_number):
        num= int(input(f"Guess a number between 1 and {x}"))
        if (num<random_number):
            print("Sorry, guess again. Too low")
        elif(num>random_number):
            print("Sorry, guess again. Too high")
        else:
            print(f"Yay, congrats. You have guessed the number {random_number} correctly")
            break
        

x= int(input("Enter a number for the outer range"))
guess(x)

#the code works fine but we have to let the user guess multiple time again and again, till he 
# guesss the right no. We have to tell him on each guess whether number is found, small or big.
#so we will make use of a while loop
#before starting while loop, we have to initialise a varible 

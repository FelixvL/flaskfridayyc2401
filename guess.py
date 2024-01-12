import sys
from random import choice

# With sys.argv, we can run the python module + define the variable from the terminal.
# This module is a guessing game where the player tries to guess the number between the two defined variables

num1 = 1
num2 = 10
guessing_range = list(range(num1, num2))

def guessing(player_guess, to_guess):
    if num1 < int(player_guess) < num2:
        if player_guess == to_guess:
            print('Congrats! You are a genius!')
            return True
        elif player_guess < to_guess:
            print('Please guess a higher number')
        else:
            print('please guess a lower number')

    else:
        print(f'Your number is out of the asked range')
        return False
    
def functie_een():
    to_guess = choice(guessing_range)
    while True:
        try:
            player_guess = int(
                input(f'Please guess a number between {num1} and {num2}: ')
            )

            if (guessing(player_guess, to_guess)):
                text = "Gefeliciteerd"
                return text
                break
        except ValueError:
            print('Please enter a number')




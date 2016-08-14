"""In this version, the program generates a random number with number of digits
equal to length. If the command line argument length is not provided, the
default value is 1. Then, the program prompts the user to type in a guess,
informing the user of the number of digits expected. The program will then
read the user input, and provide basic feedback to the user. If the guess is
correct, the program will print a congratulatory message with the number of
guesses made and terminate the game. Otherwise, the program will print a message
asking the user to guess a higher or lower number, and prompt the user to type
in the next guess."""

###############################################################################
#import section
from random import randint
import sys

###############################################################################
#Body
#function to generate a random n digit number where n is entered by the user or 1
def generate_random_number(no_of_digits):
    return randint(10**(no_of_digits-1),(10**no_of_digits)-1)

def the_game(random_number,no_of_digits):
    print("Let's play the mimsmind0 game.")
    #starting of the game
    user_input = input("Guess a {} digit number : ".format(no_of_digits))
    no_of_tries = 0
    while True:
        try:
            user_input = int(user_input)
        except
            #exception raised if user input is not an integer
            user_input = input("Invalid Input. Try again : ")
            continue
        no_of_tries += 1
        #case when the guessed number is the same as the guessed number
        if(user_input == random_number):
            print("Congratulations ! You guessed the number in {} tries".format(no_of_tries))
            break
        #case when the number guessed is lower than the random number
        elif(user_input < random_number):
            user_input = input("Try Again ! Guess a higher number : ")
        #case when the number guessex is higher than the random number
        elif(user_input > random_number):
            user_input = input("Try Again ! Guess a lower number : ")


###############################################################################
#main

def main():
    no_of_digits = 1
    try:
        no_of_digits = int(sys.argv[1])
    except:
        print("The no of digits you entered isnt a valid input. We will proceed with 1 digit for now")
    the_game(generate_random_number(no_of_digits),no_of_digits)
if __name__ == "__main__":
    main()

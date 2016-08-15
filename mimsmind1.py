"""usage: python mimsmind1.py [length]
Once again, the program generates a random number with number of digits equal to
 length. If the command line argument length is not provided, the default value
 is 3. This means that, by default, the random number is in the range of 000 and
 999.
In this version, the program will establish a maximum number of rounds,
maxrounds, equal to (2^length) + length. For example, if length = 3, then
maxrounds = 11.
Then, the program prompts the user to type in a guess, informing the user of
the number of digits expected. The program will then read the user input, and
provide 'bulls and cows' feedback to the user. A matching digit in the correct
position will result in a 'bull', while a matching digit in the wrong position
will result in a 'cow'. For example, if the correct answer is '123', and the
guess is '324', then the feedback will be one bull (for the digit '2') and one
 cow (for the digit '3'). More examples are provided below.
At each round, if the user guess is incorrect and maxrounds is not yet reached,
the program should increment the counter for round and issue a new prompt for
user input. Otherwise, the program should print a congratulatory or an
apologetic message with the number of guesses made, and terminate the game."""

###############################################################################
#import section
from random import randint
import sys
import math

###############################################################################
#Body
def generate_random_number(no_of_digits):
    return randint(0,(10**no_of_digits)-1)

def number_to_dictionary(number_as_a_list):
    dictionary = {}
    for each_digit in number_as_a_list:
        dictionary[each_digit] = dictionary.get(each_digit,0) + 1
    return dictionary
def get_cows(user_input_dictionary , number_as_a_dictionary):
    list_of_digit_keys = user_input_dictionary.keys()
    cows_counter = 0
    for each_key in list_of_digit_keys:
        if(not number_as_a_dictionary.get(each_key,0) == 0):
            cows_counter += 1
    return cows_counter

def get_bulls(user_input_as_a_list, number_as_a_list):
    bulls_counter = 0
    iterator = 0
    while (iterator < len(user_input_as_a_list)):
        if(user_input_as_a_list[iterator] == number_as_a_list[iterator]):
            bulls_counter += 1
        iterator += 1
    return bulls_counter

def random_number_to_list(random_number, no_of_digits):
    number_as_a_list = []
    for iterator in range(no_of_digits):
        number_as_a_list.append(random_number%10)
        random_number = int(random_number/10)
    number_as_a_list.reverse()
    return number_as_a_list

def the_game(random_number,no_of_digits):

    no_of_tries = (2**no_of_digits)+no_of_digits
    print("Let's play the mimsmind game. You have {} tries to guess the number".format(no_of_tries))
    #converting the random number into appropriate data structures
    number_as_a_list = random_number_to_list(random_number,no_of_digits)
    number_as_a_dictionary = number_to_dictionary(number_as_a_list)
    try_counter = 0
    #first message to user for entering a number
    user_input = input("Guess a {} digit number : ".format(no_of_digits))

    while(try_counter < no_of_tries):
        try:
            #checking if the input entered is a string
            rain_check = int(user_input)
        except:
            #asking for input if the user inputs an invalid one
            user_input = input("Invalid input. Try again : ")
            continue
        #invalid input if the no of digits entered by the user are not same as the random number
        if(not (len(user_input) == no_of_digits)):
            user_input = input("Invalid input. Try again : ")
            continue
        #converting user input into appropriate dictionaries
        user_input_as_a_list = [int(x) for x in str(user_input)]
        user_input_dictionary = number_to_dictionary(user_input_as_a_list)
        try_counter += 1
        #looking for bulls
        no_of_bulls = get_bulls(user_input_as_a_list,number_as_a_list)
        #looking for cows
        no_of_cows = get_cows(user_input_dictionary,number_as_a_dictionary) - no_of_bulls
        #if no of bulls and cows equals no of digits, number has been guessed correctly !
        if(no_of_cows == no_of_digits and no_of_bulls == no_of_digits):
            print("Congratulations ! You have guessed the number in {} tries".format(try_counter))
            break
        #the below lines will execute if the number hasnt been guessed correctly
        user_input =input("{} bulls(s) , {} cow(s). Try again : ".format(no_of_bulls, no_of_cows))
        continue

    #sorry message for users who are out of tries
    if(try_counter == no_of_tries):
        print("Sorry, you couldn't guess the number in {} tries. The number was {}".format(no_of_tries,random_number))


###############################################################################
#main

def main():
    no_of_digits = 3
    try:
        if(int(sys.argv[1]) > 0):
            no_of_digits = int(sys.argv[1])
    except:
        print("The no of digits you entered isnt a valid input. We will proceed with 3 digits for now")
    the_game(generate_random_number(no_of_digits),no_of_digits)
    pass
if __name__ == "__main__":
    main()

###############################################################################
# Title: Wheel of Fortune
# Class: CS30
# Assignment: Capstone Coding Project
# Name: James Glendinning
# Version: 2.2
# Date: January 18 2026
###############################################################################
'''A python recreation of the game Wheel of Fortune. Also comparable to the
game Hangman. Player guesses letters in a phrase until they have enough
information to complete the puzzle. Score is calculated based on number of
guesses.'''
###############################################################################
# Imports and Global Variables------------------------------------------------- 
import random
import os
import time

global total_score

phrases = {
    "TO BENEFIT FROM BEING ON-TIME": #clue
    "the early bird gets the worm", #answer
    "WISHING LUCK ON A PERFORMANCE":
    "break a leg",
    "DESCRIBING SOMETHING PERFECTLY":
    "hitting the nail on the head",
    "ONE ACTION GIVES TWO RESULTS":
    "kill two birds with one stone",
    "CALCULATED RISK-TAKING":
    "look before you leap",
    "ONE PERSON CHASING ANOTHER":
    "a game of cat and mouse",
    "DESTINED FOR BIGGER THINGS":
    "a big fish in a small pond",
    "NOT ALLOWED TO ENTER":
    "access denied",
    "WORSENING A BAD SITUATION":
    "adding fuel to the fire",
    "SAY THE MAGIC WORDS":
    "please and thank you",
    "TO BENEFIT FROM TWO CONFLICTING THINGS":
    "the best of both worlds",
    "OVEREXAGGERATING SOMETHING'S IMPORTANCE":
    "making a mountain out of a molehill"
}

total_score = 0

round = 0 # which round are you on?

letter_guesses = []

random_clue = random.choice(list(phrases.keys())) # chooses a random phrase from phrases

# Functions -------------------------------------------------------------------

def screen_clear():
    #clears the screen
    os.system('cls')


def get_highscore():
    #reads highscore from external file
    global high_score
    global filename
    
    filename = "highscore.txt"
    with open('high_score.txt', 'r') as file:
        high_score = file.read()


def new_highscore():
    #writes new highscore to external file
    global filename
    global high_score

    with open('high_score.txt', 'w') as file:
        file.write(high_score)
    farewell()


def start_game():
    #intro to the game, before guessing begins
    global name
    
    screen_clear()
    print("Welcome, new contestant, to America's favorite gameshow:")
    print("\033[96m")
    time.sleep(3)
    print("WHEEL!")
    time.sleep(1)
    print("OF!")
    time.sleep(1)
    print("FORTUNE!")
    time.sleep(1)
    print("\033[0m")
    name = input("What's your name, big shot? ") 
    print(f"It's great to have you here today, {name}!")
    time.sleep(1)
    print()
    print("The game is very simple: You will be given a clue relating to a phrase.")
    print("You will guess the letters of that phrase until you have enough for a final answer!")
    print("Careful: The more guesses you take, the more score you will lose.")
    ready_start = input("Now, input anything when you're ready!")


def quit_game():
    #end of game, tells player score and checks if its higher than highscore
    global high_score
    
    print("Your final score was")
    for i in range(3):
        time.sleep(1)
        print(".")
    print(total_score,"points!")
    if total_score > int(high_score):
        print("WOW! That's a new high score!")
        high_score = str(total_score)
        new_highscore()
    else:
        farewell()


def farewell():   
    #end of game
    print("Have a good day!")
    quit


def new_round():
    #loops every time player does a new round. sometimes repeats phrases
    global total_score
    global round
    
    round += 1
    round_score = 10
    letter_guesses = []
    screen_clear()
    # print("\033[31mThis is red text!\033[0m") #color test
    random_clue = random.choice(list(phrases.keys())) # chooses a random phrase from phrases
    print(f"CLUE: {random_clue}")
    print("You have guessed:", letter_guesses)
    each_guess = ""
    answer_test = phrases[random_clue]
    correct_letter_guesses = ""



    #need to step through the answer and hide the letters using the # sign

    for char in answer_test:

        if char.isspace():
            correct_letter_guesses += " "

        else:
            correct_letter_guesses += "#"

    print("\033[1;34;40m") #different colour for the masked answer
    print(correct_letter_guesses)
    print("\033[0m")       #put colour back to normal

    #loop through until all letters are guessed

    while correct_letter_guesses != answer_test:
        guess_or_no = input("Would you like to make a final guess yet? (y/n) ")
        if guess_or_no == "y":
            final_guess = input("What do you think it is? ")
            if final_guess == phrases[random_clue]:
                total_score += round_score
                print("You got it! Good job!")
                print("Your score is currently", total_score)
                play_again = input("Would you like to play again? (y/n)")
                if play_again == "y":
                    if round <= 6:
                        new_round()
                    else:
                        end_game()
                if play_again == "n":
                    quit_game()
                    break
                
            else:
                print("Nope, try again...")
                time.sleep(3)
        else:    
            letter_guess = input("Enter a single letter quess or * to quit: ")[0]
            if letter_guess.lower() == '*':
                quit_game()
                break # player quits the game
            else:       
                round_score -= 1
                each_guess += letter_guess.lower() # player guesses a letter
                letter_guesses.append(letter_guess)

            correct_letter_guesses = ""

            for char in answer_test:

                if char in each_guess:
                    correct_letter_guesses += char
                    #if correct guess, add to guessed correctly list
                    each_guess += letter_guess

                else:
                        #print("Letter not found - guess again :-)")
                        if char.isspace():
                            correct_letter_guesses += " "
                        else:
                            correct_letter_guesses += "#"

    #print("The clue is: ",clues[round], ":   ", correct_letter_guesses)
        #print()
        screen_clear()
        print()
        print(f"CLUE: {random_clue}")
        print("You have guessed:", letter_guesses)
        print("\033[1;34;40m\n")
        print(correct_letter_guesses)
        print("\033[0m")

    print()


# Main ------------------------------------------------------------------------
get_highscore()
print("\033[0m") #changes text color to white
total_score = 0
start_game()
new_round()
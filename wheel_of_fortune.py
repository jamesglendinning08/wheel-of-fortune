import random
import os

global total_score

def screen_clear():
    #clears the screen
    os.system('cls')

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

print("\033[0m") 

solve_guess = []

total_score = 0

round = 0 # counter for stepping through each clue and answer

letter_guesses = []

quit = []

random_clue = random.choice(list(phrases.keys())) # chooses a random phrase from phrases

#    print(phrases[random_clue])       <--- this gets the clue answer!!

#add a loop for playing the game using each clue(up to 10) until user quits

#while round < 13:

def quit_game():
    print("Your final score was", total_score)
    print("Have a good day!")


def new_round():
    global total_score
    
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
                    new_round()
                if play_again == "n":
                    quit_game()
                    break
                
            else:
                print("Nope, try again...")
        else:    
            letter_guess = input("Enter a single letter quess or * to quit: ")[0]
            if letter_guess.lower() == '*':
                quit_game()
                break # player quits the game
            else:       
                round_score -= 2
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
        #screen_clear()
        print()
        print(f"CLUE: {random_clue}")
        print("You have guessed:", letter_guesses)
        print("\033[1;34;40m\n")
        print(correct_letter_guesses)
        print("\033[0m")

    print()

total_score = 0
new_round()
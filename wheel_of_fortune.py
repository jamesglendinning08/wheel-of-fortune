import random
import os

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

round = 0 # counter for stepping through each clue and answer

letter_guesses = []

quit = []

random_clue = random.choice(list(phrases.keys())) # chooses a random phrase from phrases

print(f"CLUE: {random_clue}")

#    print(phrases[random_clue])       <--- this gets the clue answer!!

#add a loop for playing the game using each clue(up to 10) until user quits

#while round < 13:

screen_clear()
# print("\033[31mThis is red text!\033[0m") #color test
random_clue = random.choice(list(phrases.keys())) # chooses a random phrase from phrases
print(f"CLUE: {random_clue}")
each_guess = ""
answer_test = phrases[random_clue]
letter_guesses = []
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
    letter_guess = input("Enter a single letter quess or * to quit: ")[0]

    if letter_guess.lower() == '*':
        quit = letter_guess.lower()
        break
    else:       
        each_guess += letter_guess.lower()

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
    print(f"CLUE: {random_clue}")
    print("\033[1;34;40m\n")
    print(correct_letter_guesses)
    print("\033[0m")

    print()
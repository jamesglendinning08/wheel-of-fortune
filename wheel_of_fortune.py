import random

phrases = {
    "TO BENEFIT FROM BEING ON-TIME": #clue
    "The Early Bird Gets The Worm", #answer
    "WISHING LUCK ON A PERFORMANCE":
    "Break A Leg",
    "DESCRIBING SOMETHING PERFECTLY":
    "Hitting The Nail On The Head",
    "ONE ACTION GIVES TWO RESULTS":
    "Kill Two Birds With One Stone",
    "CALCULATED RISK-TAKING":
    "Look Before You Leap",
    "ONE PERSON CHASING ANOTHER":
    "A Game Of Cat And Mouse",
    "DESTINED FOR BIGGER THINGS":
    "A Big Fish In A Small Pond",
    "NOT ALLOWED TO ENTER":
    "Access Denied",
    "WORSENING A BAD SITUATION":
    "Adding Fuel To The Fire",
    "SAY THE MAGIC WORDS":
    "Please And Thank You",
    "TO BENEFIT FROM TWO CONFLICTING THINGS":
    "The Best Of Both Worlds",
    "OVEREXAGGERATING SOMETHING'S IMPORTANCE":
    "Making A Mountain Out Of A Molehill"
}

random_clue = random.choice(list(phrases.keys()))

print(f"Your clue is: {random_clue}")
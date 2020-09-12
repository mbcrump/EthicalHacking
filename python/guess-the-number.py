## App #2: Guess the number

#import
import random

## inform the user of what to do
print ("----------------")
print ("Guess the number")
print ("Between 0 - 100 ")
print ("----------------")
print ()

therandomnumber = random.randint(0, 100)
guess = -1
numberofguesses = 0
print(therandomnumber)
yourname = input("What is your name: ")

#check input to see if they matched it successfully
while guess != therandomnumber:
    guess_text = input("Guess a number: ")
    guess = int(guess_text)
    numberofguesses += 1
    if guess < therandomnumber:
        print("I'm sorry, {}, your guess was {} and it is too low. You have guessed {} times".format(yourname, guess_text, numberofguesses))
    elif guess > therandomnumber:
        print("I'm sorry, {}, your guess was {} and it is too high.You have guessed {} times".format(yourname, guess_text, numberofguesses))
    else:
        print ("You got it right in {} guesses!!!".format(numberofguesses))

print("Game over.")
print("Created by the CrumpFam")

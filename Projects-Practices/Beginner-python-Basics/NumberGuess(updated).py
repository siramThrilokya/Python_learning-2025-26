'''
I want that guess should be done ones and user need to guess where system helps to admire the less or greater with the computer guessed number, every choice make reduction in choice
'''

import random

sysGuess = random.randint(1,20)
choice = 5
computerScore = 0
userScore = 0

while True:
    userInput = str(input("Enter your guess: "))
    if len(userInput) == 0:
        print("Enter valid or some number on it")
    userInput = int(userInput)
    if userInput == 00:
        break
    if userInput > sysGuess:
        print("Your guessed number is greater, pick any smaller number")
        choice -= 1
    elif userInput<sysGuess:
        print("Your guessed number is smaller, pick any greater number")
        choice -= 1
    elif userInput == sysGuess:
        print("Your guessed was right")
        userScore += 1
    elif choice == 0:
        print("You run out of choice")
        computerScore += 1
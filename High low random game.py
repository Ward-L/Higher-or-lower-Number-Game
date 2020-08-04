#Rewrite the high_low.py program from section Decisions to use an random integer between 0 and 99
#instead of the hard-coded 78. Use the Python documentation to find an appropriate module and function to do this.

import random

number = random.randint(1, 100)
guess = -1 
count = 0

print("Guess the number! You must guess within 5 guesses to win!")
while guess != number: 
    guess = int(input("Is it..."))
    if guess == number: 
        print("FUCKIN YASSS YOU DID IT")
    elif guess < number:
        print("Its higher then that, guess again!")
        count = count + 1
        if count < 5:
            print("You have", 5 - count,"guesses remaining!")
        elif count == 5:
            print("Sorry you have run out of trys!")
            break
    elif guess > number:
        print("Try a bit smaller fam")
        count = count + 1
        if count < 5:
            print("You have", 5 - count,"guesses remaining!")
        elif count == 5:
            print("Sorry you have run out of tries!")
            break  
print(number)      

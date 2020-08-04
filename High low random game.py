#this imports the random module to python
import random

#This code uses the random module to create a number at random between the ranges of 1-100 and then sets variables of guess and count to what is needed to start.
number = random.randint(1, 100)
guess = -1 
count = 0


#This code creates a while loop that breaks when the guess is correct to the random number generated above. It also breaks once 5 guesses has been reached. 
#If you guess higher or lower than the number generated it will give you a clue to guess higher or lower.
print("Guess the number! You must guess within 5 guesses to win!")
while guess != number: 
    guess = int(input("Is it..."))
    if guess == number: 
        print("WELL DONE, YOU DID IT!")
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

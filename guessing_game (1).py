print("Welcome to the ultimate riddle. Do you think you can solve it? We will see.")
print("I am the Riddler and welcome to my number guessing game! Guess a number between 1 and 100 to win. If you fail well you will find out what happens. Good luck!")

import random

n = int(input("please enter a number between 1 and: "))
number = random.randint(1,n)
guess = int(input("enter a number between 1 and {}: ".format(n)))

while guess != number:
    if guess < number:
        print("To Low! Try again")
        guess = int(input("enter a number between 1 and {}: ".format(n)))    
    if guess > number:
        print("To High! Try again")    
        guess = int(input("enter a number between 1 and {}: ".format(n)))

print("Well well well looks like you are smarter than you look. Until next time. Ridller out.")






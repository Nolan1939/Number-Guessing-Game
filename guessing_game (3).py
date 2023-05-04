print("Welcome to the ultimate riddle. Do you think you can solve it? We will see.")
print("I am the Riddler and welcome to my number guessing game! Guess a number between 1 and 100 to win. If you fail well you will find out what happens. Good luck!")

import random

n = int(input("please enter a number between 1 and: "))
number = random.randint(1,n)
guess = int(input("enter a number between 1 and {}: ".format(n)))
attempts = 1

while guess != number:
    if guess < number:
        print("To Low! Try again")
        guess = int(input("enter a number between 1 and {}: ".format(n))) 
        attempts += 1   
    if guess > number:
        print("To High! Try again")   
        guess = int(input("enter a number between 1 and {}: ".format(n)))
        attempts += 1

print("Well well well looks like you are smarter than you look. Until next time. Ridller out.")
print ("The number you guessed was correct! the number was {} and it took you {} attempts.".format(number,attempts))

#credits:
#team treehouse.com, selftaughtdev(youtube), wrt tech(youtube), portfoliocourses(youtube), python.org 








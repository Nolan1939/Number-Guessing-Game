print("Welcome to the ultimate riddle. Do you think you can solve it? We will see.")
print("I am the Riddler and welcome to my number guessing game! Guess a number between 1 and 100 to win. If you fail well you will find out what happens. Good luck!")

import random
global high_score
high_score = 5
print("Current Highscore = ", str(high_score))
n = int(input("please enter a number between 1 and: "))
number = random.randint(1,n)
guess = int(input("enter a number between 1 and {}: ".format(n)))
attempts = 1


while guess != number:
    try:
        if guess < number:
            print("To Low! Try again")
            guess = int(input("enter a number between 1 and {}: ".format(n))) 
            attempts += 1   
        if guess > number:
            print("To High! Try again")   
            guess = int(input("enter a number between 1 and {}: ".format(n)))
            attempts += 1                              
    except ValueError:
        print("Well well well you were supposed to guess a number. hmmm i am in a generous mood so guess again") 
      

        if attempts < high_score:
            print("Looks like you set a new highscore well done!")
            high_score = attempts

print("Well well well looks like you are smarter than you look. Until next time. Ridller out.")
print ("The number you guessed was correct! the number was {} and it took you {} attempts.".format(number,attempts))



#credits:
#team treehouse.com, selftaughtdev(youtube), wrt tech(youtube), portfoliocourses(youtube), python.org 







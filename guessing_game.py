import random 
from statistics import mean, median, mode
def start_game():

    print("Welcome to the ultimate riddle. Do you think you can solve it? We will see.")
    print("I am the Riddler and welcome to my number guessing game! Guess a number between 1 and 100 to win. If you fail well you will find out what happens. Good luck!")

    
    global high_score
    high_score = 5
    print("Current Highscore = ", str(high_score))
    number = random.randint(1,100) 
    attempts = 1
    tries = []

    while True:
        try:
           
            
            
            print(f"{number}")
            guess = int(input("enter a number between 1 and 100: "))   
            if guess < number:
                print("To Low! Try again")
               
                attempts += 1  
                continue 
            elif guess > number:
                print("To High! Try again")   
                
                attempts += 1  
                continue 
            else:
                print("Well well well looks like you are smarter than you look. Until next time. Ridller out.\n") 
                tries.append(attempts)
                print("overall stats")
                print(f"Mean: {mean(tries)}")
                print(f"Median: {median(tries)}")
                print(f"Mode: {mode(tries)}")
                if str(input("Would you like to play again? y/N:")).upper() == "Y":
                    number = random.randint(1,100)
                    continue
                else:
                    print("Exiting Game! Thanks for playing")
                    break                        
        except ValueError:
            print("Well well well you were supposed to guess a number. hmmm i am in a generous mood so guess again")
            continue 
    
    print ("The number you guessed was correct! the number was {} and it took you {} attempts.".format(number,attempts))
start_game()


#credits:
#team treehouse.com, selftaughtdev(youtube), wrt tech(youtube), portfoliocourses(youtube), python.org 







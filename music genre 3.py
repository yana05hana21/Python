#!/usr/bin/env python

import random
genre = None

def main():
     """Start a music guessing game."""
     print("Guess the music genre!")
     
     genre = [
         "hiphop",
         "rock",
         "kpop",
         "jpop",
         "r&b",
         "jazz",
         "classical",
         ]
     
     max_attempts = 3 #set the maximum number of attempts
     score = 0
     
     while True : 
         chosen_genre = random.choice (genre)
         attempts = 0
         
         while attempts < max_attempts:
             guess = input("What music genre am I thinking of? ").lower()
        
             if guess == chosen_genre :
                score+=1
                print("You guessed {}. YEAYYY!".format(guess))
                break
             else:
                print("You guessed {}. HUHU PLEASE TRY AGAIN BRO!".format(guess))
                attempts+=1
             if attempts < max_attempts:
                    first_letter = chosen_genre[0]. upper()
                    clue = "clue : The genre start with the letter {}" .format(first_letter), len(chosen_genre)
                    print (clue)
                
             else:
                print("You've used all your attempts. The correct genre was {}.".format(chosen_genre))
                print("Your final score is : {}".format (score))
                break
            
main()
     
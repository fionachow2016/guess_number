#!/usr/bin/python

'''
Think of a number between 0 and 100. 
Try to write an algorithm which will find out what number I/'m thinking of. 
You can have as many guesses as you like, and after each guess I/'ll tell you whether you were too high, or too low.
Created by Fiona Chow
Dated: 06-25-2016
'''
import random

small = 0
large = 100
guessright = False
prevguessnum = 0
count = 0
maxplay = 5

print "Guess a number between 0 and 100."

while not guessright:
    guessnum = random.randint(small,large)
    count +=1
    if prevguessnum != guessnum:
        ans = raw_input("Is {} your guess number? Yes or No. " .format(guessnum))
        if ans.lower() == "no" or ans.lower() == "n":
            if count < maxplay:
                toohigh = raw_input("Is {} too high? " .format(guessnum))
                if toohigh.lower() == "yes" or toohigh.lower() == "y":
                    large = guessnum
                else:
                    small = guessnum
                prevguessnum = guessnum
                guessright = False
            else:
                cont = raw_input("Do you want to continue? ")
                if cont.lower() == "yes" or cont.lower() == "y":
                    count = 0
                elif cont.lower() == "no" or cont.lower() == "n":
                    print "Goodbye!"
                    break
        else:
            again = raw_input("Do you want to play again? ")
            if again.lower() == "no" or again.lower() == "n":
                guessright = True
            else:
                count = 0
    else:
        guessnum = random.randint(small,large)
        
        

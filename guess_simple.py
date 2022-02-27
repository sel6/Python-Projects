#GUESS RANDOM NUMBER IN THREE TRIALS
from random import randint
guessed = False
number = randint(0, 100)
guesses = 0
while not guessed:
    ans = input("Try to guess the number i'm thinking! only 3guess \n")
    guesses += 1
    if guesses == 3 and int(ans) != number:
        print("You can't try anymore!")
        break
    if int(ans) == number:
        print("Congrats! You guessed it correctly.\n")
        print("It took you {} guesses!".format(guesses))
        break
    elif int(ans) > number:
        print("The number is lower than what I guessed. Think!")
    elif int(ans) < number:
        print(" You idiot, it's greater than what I guessed!")
        

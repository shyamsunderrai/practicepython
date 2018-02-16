'''
Challenge
- Generate a random number between 1 & 10
- Accept input from user
- Using while, loop if random <> user input OR when user input <> "exit", else break from loop
'''
import random
guesses=[]

def guessrandom():
    while True:
        user_input = raw_input("Guess the random number between 1 and 9: ")
        xrand = random.randint(1,9)
        guesses.append(user_input)

        if (user_input.lower() == 'exit'):
            print "You decided to quit"
            print "Your previous guesses were ", guesses
            break
        elif(int(user_input) == xrand):
            print "You guessed it right"
            print "Your previous guesses were ", guesses
            break
        else:
            print "Try again."
            print "The correct answer was: ", xrand

guessrandom()


#if (xrand == user_input):
#    print "You guessed the right number"
#else:
#    print "Your guess is wrong, random number is ", xrand


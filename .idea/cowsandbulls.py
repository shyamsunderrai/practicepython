'''
Cows and Bulls game
Rules:

1. Generate a random 4 digit number, for instance 1345
2. Ask the user to guess the number
3. For each right number, in right position, for instance 1865, user gets a cow (keep track of how many right guesses)
4. For each right number, in wrong position, for instance,2169, user gets a bull (keep track of how many right guesses)
5. After each guess, print the number of cows and bulls the user has
6. When the right number is guessed, game concludes

'''

import random


def genrandom():
    game=random.randint(4000,4002)
    return game

def game():
    mypin = []
    pin = genrandom()
    for val in str(pin):
        mypin.append(val)
    return mypin


if __name__ == "__main__":

    gamelist = game()
    xval = str(0)
    totalcows = 0
    totalbulls = 0

    while ( len(xval) != 4 ):
        userlist = []
        cows = []
        bulls = []
        user_input = raw_input("Guess>> ")
        # Get the puzzle for the game
        #Conver user response to list "userlist", for comparison
        for uval in str(user_input):
            userlist.append(uval)

        xval = [i for i, j in zip(userlist,gamelist) if i == j]


        for i in range(0,4):
            if(gamelist[i] == userlist[i]):
                cows.append(i)
            elif (gamelist[i] in userlist):
                bulls.append(i)


        print len(xval)
        print gamelist
        print len(cows), "Cow, ", len(bulls), "Bull"
        totalcows += len(cows)
        totalbulls += len(bulls)

    print "You used, ", totalcows, "cows and ", totalbulls, "bulls"








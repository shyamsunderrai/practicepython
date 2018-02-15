'''
Create a game of rock paper scissors
Rules:
- Rock beats scissors
- Scissors beats paper
- Paper beats rock

rock = 1
scissor = 2
paper = 3

Take one input each from user1 and user2
Return the winner
Play 3 rounds

'''

while True:
    user1 = raw_input("User A Enter your pick: ").lower()
    user2 = raw_input("User B, Your turn, take your pick: ").lower()

    if (user1 == "rock") and (user2 != "paper"):
        print "User A won !"
    else:
        print "User B won !"
    break

    if (user1 == "paper") and (user2 != "scissor"):
        print "User A won !"
    else:
        print "User B won !"
    break

    if (user1 == "scissor") and (user2 != "rock"):
        print "User A won !"
    else:
        print "User B won !"
    break


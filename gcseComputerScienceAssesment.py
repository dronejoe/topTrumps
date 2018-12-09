#-------------------------------------------------------------------------------
# Name:        Celebrity Dogs
# Purpose:     Top trumps game
#
# Author:      hartleyj15
#
# Created:     13/09/2018
# Copyright:   (c) hartleyj15 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random
import sys
import warnings
import time

warnings.filterwarnings("ignore")

class gameSetup():
    def startGame(): #asks player if they want to play
        play = input("Play or quit (Enter P or Q)?: ")

        if play == "Q":
            print("goodbye then")
            sys.exit("Quit game")

        elif play == "P":
            print("lets play")


    def deckSize(): #asks deck size wanted
        deckNo = False
        r = range(4,31)
        global deck

        while deckNo == False:
            try:
                deck = int(input("How big do you want the deck between 4 and 30? (even)"))

                if deck % 2 != 0:
                    print("You did not enter an even number. Please try again!")
                    deckNo = False
                elif deck in r:
                    deckNo = True
                else:
                    deckNo = False

            except ValueError:
                print("Error 404 - you entered a string")
                print("Please try again")

    def cardCreate(): #creates deck of cards from file dogs.txt and randomly creates random skills
        filename = "dogs.txt"
        file = open(filename, "r")
        global dogs
        global deck
        dogs = []
        names = []

        with file as f:
            fileNames =  f.readlines()

        for x in fileNames:
            x = x.strip('\n')
            names.insert(0,x)

        for i in range(0,deck):
            name = names[i]
            dogs.append({"name":name, "E":random.randint(1,5), "I":random.randint(1,100), "F":random.randint(1,10), "D":random.randint(1,10)})



    def deckSort(): #shuffles and deals deck between cpu and player
        global dogs, cpuPlayer, humanPlayer
        cpuPlayer = []
        humanPlayer = []
        random.shuffle(dogs)

        for i in range(0, int(deck/2)):
            humanPlayer.append(dogs[0])
            dogs.pop(0)

        for i in range(0, int(deck/2)):
            cpuPlayer.append(dogs[0])
            dogs.pop(0)




class gamePlay():

    def cardDisplayed(numberOfTurn):
        card = humanPlayer[0]
        print("-------------------------------Card %s----------------------------" %(numberOfTurn + 1))
        print("Name:...............................",card["name"])
        print("Exercise:...........................",card["E"])
        print("Intelligence:.......................",card["I"])
        print("Friendliness:.......................",card["F"])
        print("Droll:..............................",card["D"])


    def attributePick():
        global playerValue,cpuValue
        playerPick = input("Please pick your attribute choice: Exercise(E), Intelligence(I), Friendliness(F),Droll(D) \n")
        playerValue = []

        playerValue = humanPlayer[0][playerPick]
        cpuValue = cpuPlayer[0][playerPick]

        return playerPick
    def moveCards(playerWin):

        humanPlayer.insert(len(humanPlayer),humanPlayer.pop(0))
        cpuPlayer.insert(len(cpuPlayer),cpuPlayer.pop(0))

        if playerWin == True:
            humanPlayer.insert(len(humanPlayer),cpuPlayer.pop(0))
        elif playerWin == False:
            cpuPlayer.insert(len(cpuPlayer),humanPlayer.pop(0))
        else:
            print("Error - couldn't move cards")
            print("Please try again")

    def playerWinRound(player,cpu,pick):
        if pick == "D":
                    if player < cpu:
                        print("You won the round!\n")
                        return True
                    elif player > cpu:
                        print("You lost the round!\n")
                        return False
                    else:
                        sys.exit("playerValue is an invalid number")

        elif pick == "E" or "I" or "F":
            if player > cpu:
                print("You won the round!\n")
                return True
            elif player < cpu:
                print("You lost the round!\n")
                return False
            else:
                sys.exit("playerValue is an invalid number")

    def cpuWinRound(player,cpu,pick):
        if pick == "D":
                    if player > cpu:
                        print("You won the round!\n")
                        return True
                    elif player < cpu:
                        print("You lost the round!\n")
                        return False
                    else:
                        sys.exit("playerValue is an invalid number")

        elif pick == "E" or "I" or "F":
            if player < cpu:
                print("You won the round!\n")
                return True
            elif player > cpu:
                print("You lost the round!\n")
                return False
            else:
                sys.exit("playerValue is an invalid number")


    def winGamePlayer():
        if len(cpuPlayer) == 0:
            return True
        else:
            return False

    def winGameCPU():
        if len(humanPlayer) == 0:
            return True
        else:
            return False

class cpuPlayerCode():

    def cpuChallenge():
        if cpuPlayer[0]["E"] > humanPlayer[0]["E"]:
            return "E"
        elif cpuPlayer[0]["I"] > humanPlayer[0]["I"]:
            return "I"
        elif cpuPlayer[0]["F"] > humanPlayer[0]["F"]:
            return "F"
        elif cpuPlayer[0]["D"] < humanPlayer[0]["D"]:
            return "D"
        else:
            sys.exit("cpu challenge error")

    def randomAttribute():

        attr = ["E","I","F","D"]
        return random.choice(attr)


try:

    gameSetup.startGame()

    gameSetup.deckSize()
    gameSetup.cardCreate()
    gameSetup.deckSort()
    previousPlayerWin = True


    for i in range(deck):


        try:




            if previousPlayerWin == True:

                gamePlay.cardDisplayed(i)
                playerPick = gamePlay.attributePick()
                player = playerValue
                cpu = cpuValue

                playerWin = gamePlay.playerWinRound(player,cpu,playerPick)

            elif previousPlayerWin == False:
                cpuPick = cpuPlayerCode.randomAttribute()
                print(cpuPick)

                time.sleep(1)

                playerValue = humanPlayer[0][cpuPick]
                cpuValue = humanPlayer[0][cpuPick]
                print(playerValue)
                print(cpuValue)

                time.sleep(1)

                playerWin = gamePlay.cpuWinRound(playerValue,cpuValue,cpuPick)

                time.sleep(4)


            previousPlayerWin = playerWin
            gamePlay.moveCards(playerWin)


        except IndexError:

            print("index error")

            if gamePlay.winGamePlayer() == True:
                print("You won the game!")
                sys.exit()
            elif gamePlay.winGameCPU() == True:
                print("You lost the game!")
                sys.exit()
            else:
                print("Error - list index out of range")
                print("please try again")
                sys.exit()


except KeyboardInterrupt:
    print("Thank you for playing")
    print("Have a good day")
    sys.exit()
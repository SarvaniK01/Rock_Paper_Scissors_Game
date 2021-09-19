print("**************************************")
print("There are 2 players in this game")
print("**************************************")

def rep():
    game=input("Do you want to START?(y/n):")
    while(game=="y"):
        print("\n*************ROCK PAPER SCISSORS GAME***********")
        print("****************************************************************")
        print("\nInput R=ROCK P=PAPER S=SCISSORS(Capitals only)")
        player1=input("ROCK PAPER SCISSORS:")
        player2=input("ROCK PAPER SCISSORS:")
        print("****************************************************************")

        if(player1==player2):
            print("\n")
            print("IT IS A TIE")
            game=input("Do you want to continue?(y/n):")

        elif(player1=="R" and player2=="P"):
            print("Player 1 has chosen "+ str(player1)+ " \n Player 2 has chosen " + str(player2))
            print("\n")
            print("PLAYER 2 WON!!!")
            print("HOORAAY!!")
            game=input("Do you want to continue?(y/n):")

        elif(player1=="R" and player2=="S"):
            print("Player 1 has chosen "+ str(player1)+ " \n Player 2 has chosen " + str(player2))
            print("\n")
            print("PLAYER 1 WON!!!")
            print("HOORAAY!!")
            game=input("Do you want to continue?(y/n):")

        elif(player1=="P" and player2=="R"):
            print("Player 1 has chosen "+ str(player1)+ " \n Player 2 has chosen " + str(player2))
            print("\n")
            print("PLAYER 2 WON!!!")
            print("HOORAAY!!")
            game=input("Do you want to continue?(y/n):")

        elif(player1=="P" and player2=="S"):
            print("Player 1 has chosen "+ str(player1)+ " \n Player 2 has chosen " + str(player2))
            print("\n")
            print("PLAYER 2 WON!!!")
            print("HOORAAY!!")
            game=input("Do you want to continue?(y/n):")

        elif(player1=="S" and player2=="R"):
            print("Player 1 has chosen "+ str(player1)+ " \n Player 2 has chosen " + str(player2))
            print("\n")
            print("PLAYER 1 WON!!!")
            print("HOORAAY!!")
            game=input("Do you want to continue?(y/n):")

        elif(player1=="S" and player2=="P"):
            print("Player 1 has chosen "+ str(player1)+ " \n Player 2 has chosen " + str(player2))
            print("\n")
            print("PLAYER 2 WON!!!")
            print("HOORAAY!!")
            game=input("Do you want to continue?(y/n):")

        else:
            print("\n")
            print("Wrong Input")
            game=input("Do you want to continue?(y/n):")
    
rep()
    
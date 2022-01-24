import functions
game = 1

while game != 0: #ofers a new game
    functions.makeboard(int(input("what game you want to play? 3 for 3x3 4 for 4x4")))
    functions.getPlayersName()
    print("board is now clear")
    functions.printBoard()
    while True: #runs until there is a winer\tie
        functions.choosePlace()
        if functions.didWin() == True:
            if functions.whosTurn() == True:
                print(f"{functions.player1} is the winer")
                break
            else:
                print(f"{functions.player2} is the winer")
                break
            break
    if functions.makeboard(input("do you want to play another game? 3 for 3x3 4 for 4x4 0 for NO!")) != True:
        break


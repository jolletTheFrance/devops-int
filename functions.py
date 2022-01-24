board = []
turn = False #used to know whos turn it is
player1 = None #used for names
player2 = None
cantgoright = False # flags that make sure you are testing thre middle of streaks
cantgoleft = False
cantgodown = False
cantgoup = False

def makeboard(size):
    global board
    print("size is", size)
    if size == 3:
        board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    elif size == 4:
        board = [["_", "_", "_", "_"], ["_", "_", "_", "_"], ["_", "_", "_", "_"], ["_", "_", "_", "_"]]
    else:
        print("thank you for playing")
        return False

def getPlayersName():
    '''
    just gets player names and greets them
    :return:
    '''
    global player1, player2
    player1 = input("enter first player name: ")
    print(f'hi {player1} welcome')
    player2 = input("enter second player name: ")
    print(f'hi {player2} welcome')

def printBoard ():
    ''' prints the board'''
    for line in range(0, len(board)):
        print(board[line])

def choosePlace ():
    global board
    '''checks for valid row\line input and states whos turn it is'''
    global player1, player2

    if turn == False: #flase = player1 true = player2
        print(f"{player1} goes now (X)")
    else:
        print(f"{player2} goes now (O)")
    line = input(f"select a line (up-down) between 1-{len(board)}") #gets input for line and checks for valid input
    while inputtester(line) == False:
        print("invalid input")
        line = input(f"select a line (up-down) between 1-{len(board)}")

    row = input(f"select a row (left-right) between 1-{len(board)}")
    while inputtester(row) == False:
        print("invalid input")
        row = input(f"select a row (left-right) between 1-{len(board)}")
    if board[int(line)-1][int(row)-1] == '_': #test if cell is taken
        changeBoard(int(line), int(row), whosTurn())
    else:
        print("this spot is taken!!! please select another one")
        choosePlace()


def inputtester(tested):
    global board
    print(tested)
    if len(board) == 3:
        if tested != str(len(board)) and tested != str(len(board)-1) and tested != str(len(board)-2) :
            return False
        else:
            return True
    if len(board) == 4:
        if tested != str(len(board)) and tested != str(len(board)-1) and tested != str(len(board)-2)\
                and tested != str(len(board)-3) :
            return False
        else:
            return True

def changeBoard(line, row, whosTurn):
    '''
    :param line: takes line from choosePlace
    :param row: takes row from choosePlace
    :param whosTurn: takes whos turn it is
    :return:
    '''
    if whosTurn == False:
        board[line-1][row-1] = 'x'
        printBoard()

    else:
        board[line - 1][row - 1] = 'O'
        printBoard()

def didWin ():
    global board
    '''checks if there is a winer or tie and returns true'''
    for row in range(len(board)):
        for col in range(len(board[0])):
            if checksqr(row, col) == True:
                return True
    return False

def checksqr(row, col):
    """
    checks if there is a winner and gives hint for winning
    :param row: takes a row
    :param col: takes a coloum
    :return: returns true if someone won
    """
    global cantgoup
    global cantgoleft
    global cantgodown
    global cantgoright
    cantgoright = False  # flags that make sure you are testing thre middle of streaks
    cantgoleft = False
    cantgodown = False
    cantgoup = False

    mysign = board[row][col]
    if row + 1 == len(board):
        cantgodown = True
    if row == 0:
        cantgoup = True
    if col + 1 == len(board[0]):
        cantgoright = True
    if col == 0:
        cantgoleft = True
    if mysign == '_':
        gaptester(row, col)
        return False

    if not cantgoleft and not cantgoright and not cantgoup and not cantgodown:  # checks if cell is in middle of 3 simmilar
        if board[row+1][col] == mysign and board[row-1][col] == mysign: #test fot win streak
            return True
        if board[row+1][col] == mysign and board[row-1][col] == '_': #test for optional win
            if input("would you like to get a hint? y for YES n for NO").lower() == 'y':
                print(f"there is a wining play for {mysign} at {row}, {col+1}")
        if board[row+1][col] == '_' and board[row-1][col] == mysign: #test for optional win
            if input("would you like to get a hint? y for YES n for NO").lower() == 'y':
                print(f"there is a wining play for {mysign} at {row+2}, {col+1}")

        if board[row][col+1] == mysign and board[row][col-1] == mysign: #test fot win streak
            return True
        if board[row][col+1] == '_' and board[row][col-1] == mysign:
            if input("would you like to get a hint? y for YES n for NO").lower() == 'y': #test for optional win
                print(f"there is a wining play for {mysign} at {row+1}, {col+2}")
        if board[row][col+1] == mysign and board[row][col-1] == '_':
            if input("would you like to get a hint? y for YES n for NO").lower() == 'y': #test for optional win
                print(f"there is a wining play for {mysign} at {row+1}, {col}")

        if board[row+1][col+1] == mysign and board[row-1][col-1] == mysign: #test fot win streak
            return True
        if board[row+1][col+1] == '_' and board[row-1][col-1] == mysign:  #test for optional win
            if input("would you like to get a hint? y for YES n for NO").lower() == 'y':
                print(f"there is a wining play for {mysign} at {row+2}, {col+2}")
        if board[row+1][col+1] == mysign and board[row-1][col-1] == '_':  #test for optional win
            if input("would you like to get a hint? y for YES n for NO").lower() == 'y':
                print(f"there is a wining play for {mysign} at {row}, {col}")


        if board[row-1][col+1] == mysign and board[row+1][col-1] == mysign: # test for win streak
            return True
        if board[row-1][col+1] == mysign and board[row+1][col-1] == '_':  # test for optional win
            if input("would you like to get a hint? y for YES n for NO").lower() == 'y':
                print(f"there is a wining play for {mysign} at {row+2}, {col}")
        if board[row-1][col+1] == '_' and board[row+1][col-1] == mysign:  # test for optional win
            if input("would you like to get a hint? y for YES n for NO").lower() == 'y':
                print(f"there is a wining play for {mysign} at {row}, {col+2}")

    if (cantgoright or cantgoleft) and not cantgodown and not cantgoup:
        if board[row+1][col] == mysign and board[row-1][col] == mysign:
            return True
        if board[row+1][col] == mysign and board[row-1][col] == '_':
            if input("would you like to get a hint? y for YES n for NO").lower() == 'y':
                print(f"there is a wining play for {mysign} at {row}, {col}")
        if board[row+1][col] == '_' and board[row-1][col] == mysign:
            if input("would you to get a hint? y for YES n for NO").lower() == 'y':
                print(f"there is a wining play for {mysign} at {row+2}, {col+1}")

    if (cantgoup or cantgodown) and not cantgoleft and not cantgoright:
        if board[row][col+1] == mysign and board[row][col-1] == mysign: # test for win streak
            return True
        if board[row][col+1] == '_' and board[row][col-1] == mysign: # test fot optional win
            if input("would you to get a hint? y for YES n for NO").lower() == 'y':
                print(f"there is a wining play for {mysign} at {row+1}, {col+2}")
        if board[row][col+1] == mysign and board[row][col-1] == '_': # test fot optional win
            if input("would you to get a hint? y for YES n for NO").lower() == 'y':
                print(f"there is a wining play for {mysign} at {row+1}, {col}")


def gaptester(row, col):
    if (cantgoright or cantgoleft) and not cantgodown and not cantgoup:
        if board[row+1][col] == board[row-1][col] != '_': #test fot gap streak
            if input("would you to get a hint? y for YES n for NO").lower() == 'y':
                print(f"there is a wining play for {board[row+1][col]} at {row + 1}, {col + 1}")
    if (cantgoup or cantgodown) and not cantgoleft and not cantgoright:
        if board[row][col+1] == board[row][col-1] != '_': # test for win streak
            if input("would you to get a hint? y for YES n for NO").lower() == 'y':
                print(f"there is a wining play for {board[row][col+1]} at {row + 1}, {col + 1}")
    if not cantgoleft and not cantgoright and not cantgoup and not cantgodown:  # checks if cell is in middle of 3 simmilar
        if board[row+1][col] == board[row-1][col] != '_': #test fot gap streak
            if input("would you to get a hint? y for YES n for NO").lower() == 'y':
                print(f"there is a wining play for {board[row+1][col]} at {row + 1}, {col + 1}")
        if board[row][col+1] == board[row][col-1] != '_': #test fot gap
            if input("would you to get a hint? y for YES n for NO").lower() == 'y':
                print(f"there is a wining play for {board[row][col+1]} at {row + 1}, {col + 1}")
        if board[row+1][col+1] == board[row-1][col-1] != '_': #test fot gap streak
            print("tested")
            if input("would you to get a hint? y for YES n for NO").lower() == 'y':
                print(f"there is a wining play for {[row+1][col+1]} at {row + 1}, {col + 1}")
        if board[row-1][col+1] == board[row+1][col-1] != '_': # test for gap streak
            if input("would you to get a hint? y for YES n for NO").lower() == 'y':
                print(f"there is a wining play for {board[row-1][col+1]} at {row + 1}, {col + 1}")

def whosTurn ():
    global turn
    if turn == False:
        turn = True
        return False
    else:
        turn = False
        return True


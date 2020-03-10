import random

board = [None, None, None, None, None, None, None, None, None]
#9 variables, one for each box. True is if it is taken by the AI, false is if it is taken by the player

#x in this check will check if that box is claimed by a player
def check_single_box(x):
    if board[x] == True:
        return False
    elif board[x] == False:
        return False
    else:
        return True

#checks to see if the board is empty, returns true if it is
def check_board_empty():
    for squares in board:
        if squares != None:
            return False
        else:
            return True

#Checks to see if there is a winning combination, and returns the value of the winning player,
#True for AI, False for Player. If no one wins, it returns false
def winning_combinations():
    if board[0] == board[1] == board[2]:
        return board[0]
    elif board[3] == board[4] == board[5]:
        return board[3]
    elif board[6] == board[7] == board[8]:
        return board[6]
    elif board[0] == board[3] == board[6]:
        return board[0]
    elif board[1] == board[4] == board[7]:
        return board[1]
    elif board[2] == board[5] == board[8]:
        return board[2]
    elif board[0] == board[4] == board[8]:
        return board[0]
    elif board[2] == board[4] == board[6]:
        return board[2]

def block_win():
    failure = random.randint(1,51)
    if failure != 50:
        if board[0] == board[1] and board[2] == None: #012 horiz
            return 2
        elif board [1] == board[2] and board[0] == None: #210
            return 0
        elif board[3] == board[4] and board[5] == None: #345
            return 5
        elif board [4] == board[5] and board[3] == None: #543
            return 3
        elif board [6] == board[7] and board[8] == None: #678
            return 8
        elif board[8] == board[7] and board[6] == None: #876
            return 6
        elif board [0] == board[2] and board[1] == None: #021
            return 1
        elif board [3] == board[5] and board[4] == None: #354
            return 4
        elif board[6] == board[8] and board[7] == None: #687
            return 7
        elif board[0] == board[3] and board[6] == None: #036 vert
            return 6
        elif board [1] == board[4] and board[7] == None: #147
            return 7
        elif board[2] == board[5] and board[8] == None: #258
            return 8
        elif board [6] == board[3] and board[0] == None: #630
            return 0
        elif board [7] == board[4] and board[1] == None: #741
            return 1
        elif board[8] == board[5] and board[2] == None: #852
            return 2
        elif board [6] == board[0] and board[3] == None: #603
            return 3
        elif board [7] == board[1] and board[4] == None: #714
            return 4
        elif board[8] == board[2] and board[5] == None: #825
            return 5
        elif board[0] == board[4] and board[8] == None: #048 diag
            return 2
        elif board [8] == board[4] and board[0] == None: #840
            return 0
        elif board[8] == board[0] and board[4] == None: #804
            return 4
        elif board [6] == board[4] and board[2] == None: #642
            return 2
        elif board [2] == board[4] and board[6] == None: #246
            return 6
        elif board[6] == board[2] and board[4] == None: #624
            return 4
    else:
        return False

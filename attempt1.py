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

def check_board_empty():
    for squares in board:
        if square != None:
            return False
            break

def winning_combinations():
    if (board[0] == board[1] == board[2] or 
        board[3] == board[4] == board[5] or 
        board[6] == board[7] == board[8] or 
        board[0] == board[3] == board[6] or 
        board[1] == board[4] == board[7] or 
        board[2] == board[5] == board[8] or 
        board[0] == board[4] == board[8] or 
        board[2] == board[4] == board[6]):
        return True
    else:
        return False

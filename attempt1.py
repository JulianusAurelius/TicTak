import random

board = [None, None, None, None, None, None, None, None, None]
#9 variables, one for each box. True is if it is taken by the AI, false is if it is taken by the player

#x in this check will check if that box is not claimed by a player or AI
def check_single_box(x):
    if board[0] == None:
            return True
    else:
        return False

#Checks to see if there is a winning combination, and returns the value of the winning player,
#True for AI, False for Player. If no one wins, it returns None
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

#Checks to see if there are two in a row, and this function, if true, gives the block number to block the win
def block_win():
    failure = random.randint(1,50)
    if failure != 50: #Since a perfect AI is not fun, there is a 2% chance the AI will make a mistake and not see the two in a row
        if board[0] == board[1] and board[2] == None: #012 horiz
            return 2
        elif board[1] == board[2] and board[0] == None: #210
            return 0
        elif board[3] == board[4] and board[5] == None: #345
            return 5
        elif board[4] == board[5] and board[3] == None: #543
            return 3
        elif board[6] == board[7] and board[8] == None: #678
            return 8
        elif board[8] == board[7] and board[6] == None: #876
            return 6
        elif board[0] == board[2] and board[1] == None: #021
            return 1
        elif board[3] == board[5] and board[4] == None: #354
            return 4
        elif board[6] == board[8] and board[7] == None: #687
            return 7
        elif board[0] == board[3] and board[6] == None: #036 vert
            return 6
        elif board[1] == board[4] and board[7] == None: #147
            return 7
        elif board[2] == board[5] and board[8] == None: #258
            return 8
        elif board[6] == board[3] and board[0] == None: #630
            return 0
        elif board[7] == board[4] and board[1] == None: #741
            return 1
        elif board[8] == board[5] and board[2] == None: #852
            return 2
        elif board[6] == board[0] and board[3] == None: #603
            return 3
        elif board[7] == board[1] and board[4] == None: #714
            return 4
        elif board[8] == board[2] and board[5] == None: #825
            return 5
        elif board[0] == board[4] and board[8] == None: #048 diag
            return 2
        elif board[8] == board[4] and board[0] == None: #840
            return 0
        elif board[8] == board[0] and board[4] == None: #804
            return 4
        elif board[6] == board[4] and board[2] == None: #642
            return 2
        elif board[2] == board[4] and board[6] == None: #246
            return 6
        elif board[6] == board[2] and board[4] == None: #624
            return 4

#Checks to see if the board is full
def is_full():
    for square in board:
        if square == None:
            return False
    return True

def randint():
    return random.randint(0, 8)

def choose_move():
    i = 0
    while (i == 0):
        x = randint()
        if check_single_box(x) == True:
            return x




##### Deciding if the player is X or O can be on the GUI, this will deal with just raw moves
########################## INPUT OUTPUT

while (is_full() == False):
    if winning_combinations() != None:
        break
    elif block_win() != None:
        board[block_win()] = True
    else:
        board[block_win()] = True
    break #this is if you press run, without input output, the computer will run this forever right now
    board[false] = False


if winning_combinations() != None:
    winner = winning_combinations()
elif is_full() == True:
    winner = None



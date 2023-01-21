board = ['-','-','-',
'-','-','-',
'-','-','-']
currentPlayer = 'X'
winner = None
gameRunning = True

# print the game board 

def display_list(board):
    print(board[0]+ '|' +  board[1] + '|' + board[2])
    print('-'*5)
    print(board[3]+ '|' +  board[4] + '|' + board[5])
    print('-'*5)
    print(board[6]+ '|' + board[7] + '|' + board[8])

display_list(board)

# take player input 
def playerInput(board):
    inp = int(input('Enter a number 1-9: '))
    if inp >= 1 and inp <= 9 and board[inp-1] == '-':
        board[inp-1] = currentPlayer
    elif inp not in range (1,10):
        print('Please select a valid input of 1-9!')
    else: 
        print('Oops! Spot already taken!')
        
# game running 

#while gameRunning:
    #display_list(board)
    #playerInput(board)

# checking for winner in all directions

def checkHorizontal():
    global winner
    if board[0] == board[1] == board[2] and board[1] != '-':
        winner = board[0]
        return True
    if board[3] == board[4] == board[5] and board[4] != '-':
        winner = board[3]
        return True
    if board[6] == board[7] == board[8] and board[7] != '-':
        winner = board[6]
        return True

# game check 
        
        
def checkRow():
    global winner
    if board[0] == board[3] == board[6] and board[3] != '-':
        winner = board[0]
        return True
    if board[1] == board[4] == board[7] and board[4] != '-':
        winner = board[1]
        return True
    if board[2] == board[5] == board[8] and board[5] != '-':
        winner = board[1]
        return True
    
def checkDiagonal():
    global winner
    if board[0] == board[4] == board[5] and board[4] != '-':
        winner = board[0]
        return True
    if board[2] == board[4] == board[6] and board[4] != '-':
        winner = board[2]
        return True

# check for tie
def checkTie():
    if '-' not in board:
        print('You tied!')

#def winCheck(board):
    #checkRow(board)
    #checkHorizontal(board)
    #checkDiagonal(board)
    #checkTie(board)

# Alternate Player

def switchPlayer():
    global currentPlayer
    if currentPlayer == 'X':
        currentPlayer = 'O'
    else:
        currentPlayer = 'X'
    

while gameRunning:
    display_list(board)
    playerInput(board)
    checkDiagonal()
    checkHorizontal()
    checkRow()
    checkTie()
    switchPlayer()
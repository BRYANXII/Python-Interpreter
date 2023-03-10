winner = None
gameRunning = True
currentPlayer = 'X'
board = ['-','-','-',
    '-','-','-',
    '-','-','-']
def Board(board):  
    print(board[0]+ ' | ' +  board[1] + ' | ' + board[2])
    print('-'*9)
    print(board[3]+ ' | ' +  board[4] + ' | ' + board[5])
    print('-'*9)
    print(board[6]+ ' | ' + board[7] + ' | ' + board[8])

# print the game board 

# take player input 
def playerInput(board):
    global currentPlayer
    inp = int(input('Enter a number 1-9: '))
    if inp >= 1 and inp <= 9 and board[inp-1] == '-':
        board[inp-1] = currentPlayer
    elif inp not in range (1,10):
        print('Please select a valid input of 1-9!')
        switchPlayer()
    else: 
        print('Oops! Spot already taken!')
        switchPlayer()
        

# checking for winner in all directions

def checkRow(board):
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
        
        
def checkColumn(board):
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
    
def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[5] and board[4] != '-':
        winner = board[0]
        return True
    if board[2] == board[4] == board[6] and board[4] != '-':
        winner = board[2]
        return True

# check for tie
def checkTie(board):
    global gameRunning
    if '-' not in board:
        main(board)
        print('You tied!')
        gameRunning = False

def checkWin():
    global gameRunning
    if checkColumn(board) or checkDiagonal(board) or checkRow(board):
        print (board)
        print(f'{winner} has won!') 
        gameRunning = False

# Alternate Player

def switchPlayer():
    global currentPlayer
    if currentPlayer == 'X':
        currentPlayer = 'O'
    else:
        currentPlayer = 'X'

# Play Again Prompt?


def playAgain():
    global gameRunning
    if gameRunning == False:
         prompt = input('Play again? Y or N: ')
    while gameRunning == False:
        main()
        print(prompt)
        if prompt == 'Y':
            gameRunning = True
        else:
            main(board)
            break
    
        

    

while gameRunning:
    Board(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    playAgain()
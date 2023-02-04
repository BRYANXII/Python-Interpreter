#Tic Tac Toe Project
'''print("Welcome to Tic Tac Toe")

def display_board(board):
    test_board= [['']*3,
['']*3,
['']*3]
    print(test_board[0])
    print(test_board[1])
    print(test_board[2])
# test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(board)

def player_input():
    pass

player_input()

def place_marker(board, marker, postition):
    pass

place_marker(test_board,'$',8)
display_board(test_board)

def win_check(board,mark):
    pass

win_check(test_board,'X')

import random

def choose_first():
    pass

def space_check(board, poistion):
    pass

def full_board_check(board):
    pass
def replay():
    pass

print('Welcome to Tic Tac Toe!')

#while True:
    # Set the game up here
    #pass

    #while game_on:
        #Player 1 Turn
        
        
        # Player2's turn.
            
            #pass

    #if not replay():
        #break'''
board = ['-','-','-',
'-','-','-',
'-','-','-']
currentPlayer = 'X'
winner = None
gameRunning = True

# print the game board 

def printBoard(board):
    print(board[0]+ ' | ' +  board[1] + ' | ' + board[2])
    print('-'*9)
    print(board[3]+ ' | ' +  board[4] + ' | ' + board[5])
    print('-'*9)
    print(board[6]+ ' | ' + board[7] + ' | ' + board[8])

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
        switchPlayer()
        print('Oops! Spot already taken! Try again')

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
        printBoard(board)
        print('You tied!')
        gameRunning = False

def checkWin():
    global gameRunning
    if checkColumn(board) or checkDiagonal(board) or checkRow(board):
        printBoard(board)
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
    while checkWin() == True:
        try:
            prompt = input('Play again? Y or N: ')
        except: 
            print(f'Please enter Y or N')
            continue
        else:
            break
        




''' if gameRunning == False:
         prompt = input('Play again? Y or N: ')
    while gameRunning == False:
        printBoard(board)
        print(prompt)
        if prompt == 'Y':
            gameRunning = True
        else:
            gameRunning = False
            printBoard(board)
            break '''
    
        

    

while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    playAgain()
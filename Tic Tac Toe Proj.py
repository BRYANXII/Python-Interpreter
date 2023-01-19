board = ['-','-','-',
'-','-','-',
'-','-','-']
currentPlayer = 'X'
winner = None
gameRunning = True

# print the game board 

def display_list(board):
    print(board[0]+ '|' +  board[1] + '|' + board[2])
    print(board[3]+ '|' +  board[4] + '|' + board[5])
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
        print('Oops spot already taken!')

while gameRunning:
    display_list(board)
    playerInput(board)
    
def checkHorizontal:
	global winner 
    if board[0]=board[1]=board[2] and board[1] != '-':
    	winner = board[0]
        return True 
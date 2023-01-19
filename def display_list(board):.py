test_board = [['-']*3,
['-']*3,
['-']*3]
currentPlayer = 'X'
winner = None
gameRunning = True
def display_list(test_board):
   print(test_board[0][0] + '|' + test_board[0][1] + '|' + test_board[0][2])
   print(test_board[1][0] + '|' + test_board[1][1] + '|' + test_board[1][2])
   print(test_board[2][0] + '|' + test_board[2][1] + '|' + test_board[2][2])
   # top_row = ['']*3
   # mid_row = ['']*3
   # bottom_row = ['']*3
   # print(top_row)
   # print(mid_row)
   # print(bottom_row)

display_list(test_board)

def playerInput(test_board):
    inp = int(input('Enter a number 1-9: '))
    if inp >= 1 and inp <= 9 and board[inp-1] == '-':
        board[inp-1] = currentPlayer
    # elif inp not >= 1 or inp not <=9:
      # print('Please enter a number 1-9!')
    elif inp not in range (1,10):
      print('Please enter a number 1-9!')
    else:
        print('Oops spot already taken!')

while gameRunning:
   display_list(test_board)
   playerInput(test_board)



def player_input():
    user1_input = input('Select either X or O to begin: ') #append? 
    input_options = ['X','O']
    player_1 = []
    if user1_input not in input_options:
            print('Please choose either X or O to begin')
    elif user1_input == input_options:
            print('You are now {user1_input}, ready to begin?')
            user1_input.append(player_1)
    else:
         print('Please choose either X or O to begin')
   
player_input()

#def test_func():
 #  print('I made this func in github')
   
# test_func()
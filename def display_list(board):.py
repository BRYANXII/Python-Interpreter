def display_list(board):
   test_board= [['']*3,
['']*3,
['']*3]
    print(test_board[0])
    print(test_board[1])
    print(test_board[2])
   # top_row = ['']*3
   # mid_row = ['']*3
   # bottom_row = ['']*3
   # print(top_row)
   # print(mid_row)
   # print(bottom_row)

display_list(board)

def player_input():
    user1_input = input('Select either X or O to begin: ') #append? 
    input_options = ['X','O']
    while user1_input not in input_options:
            print('Please choose either X or O to begin')
    if user1_input == input_options[0] or input_options[1]:
            user1_input.apppend()
player_input()

def test_func(github):
   print('I made this func in github')
   
test_func(github)
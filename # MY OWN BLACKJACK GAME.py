# MY OWN BLACKJACK GAME
# Global Variable 

player1 = None
dealer = None
sum_player1 = []
sum_dealer = []

# START GAME
def welcome():
    basics = """In blackjack, players attempt to reach a score of 21—without exceeding it—before the dealer hits 17. 
You can win if you don’t bust and your total is higher than the dealer cards. 
Hitting exactly 21 can mean even bigger winnings."""""
    print("Welcome to Black Jack!")
    show_rules =(input(f'Do you know how to play? (Y or N): '))
    if show_rules == 'Y' or 'y':
        print(f"Okay then, let's start!")
    else:
        print(basics)
welcome()
# SUM OF FIRST TWO CARDS 
def first_deal():
    pass
# GAME LOGIC
def game_logic():
    global sum_player1
    while sum_player1 >= 1 and sum_player1 <= 21:
        print(sum_player1)
        print(input('Hit? (Y or N): '))
        if input == 'Y':
            print(sum_player1 + )   
        else:
            print('BUSTED')
            break 
    
# SUM OF DEALERS FIRST CARD


# HIT OR STAY 

# BUST ?

# DEALER HIT OR STAY (MUST HIT SOFT 17)

# DEALER SUM OF TWO CARDS OR MORE

# DEALER BUST OR WIN 

# WHO WON


import random
player1 = None #what is the need for sum and player1 values? 
dealer = None
card = [1,2,3,4,5,6,7,9,10] #test card values 


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
 
# Creating a Card Class
class Cards():
    import random
    # Sum like this deck = (random.randint(1,10))*4
    def __init__(self,suit,value,face):
        self.suit = suit
        self.value = value
        self.face = face
    def __str__(self):
        print(f'{self.face} of {self.suit}(Value: {self.value})')

class CardValue():
    def __init__(self):
        for self.suit in deck:
            pass

# First Deal   
    
    
# GAME LOGIC
def game_logic():
    global card
    global sum_player1
    while sum_player1 >= 1 and sum_player1 <= 21:
        print(sum_player1)
        print(input('Hit? (Y or N): '))
        if input == 'Y':
            print(sum_player1 + card)   
        else:
            print('BUSTED')
            break 
    
# SUM OF DEALERS FIRST CARD


# HIT OR STAY 
def hit_stay():
    pass
# BUST ?
def bust_check():
    pass

# DEALER HIT OR STAY (MUST HIT SOFT 17)

# DEALER SUM OF TWO CARDS OR MORE

# DEALER BUST OR WIN 


# WHO WON


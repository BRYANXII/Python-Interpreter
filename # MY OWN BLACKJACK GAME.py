import random
suits = ('Hearts', 'Diamons', ' Spades', 'Clubs') #has to be created as a global variable 
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five': 5, 'Six':6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten':10, 'Jack':11, 'Queen':12, 'King': 13, 'Ace': 14}

# START GAME
def welcome():
    basics = """In blackjack, players attempt to reach a score of 21—without exceeding it—before the dealer hits 17. 
You can win if you don’t bust and your total is higher than the dealer cards. 
Hitting exactly 21 can mean even bigger winnings."""""
    print("Welcome to Black Jack!")
    show_rules =(input(f'Do you know how to play? (Y or N): '))
    if show_rules == 'Y': # or 'y' does not work!!
        print(f"Okay then, let's start!")
    else:
        print(basics)
welcome()
 
# Creating a Card Class
class Cards():
    # Sum like this deck = (random.randint(1,10))*4
    def __init__(self,ranks,suits,values):
        self.ranks = ranks
        self.suits = suits
        self.values = values
    def __str__(self):
        print(f'{self.rank} of {self.suit}')

class Deck():

    def __init__(self):
        
        self.deck_of_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Deck(suit,rank)
                self.deck_of_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.deck_of_cards)

    def deal_one(self):

        return self.deck_of_cards.pop(0) #NEED TO RETURN

# CREATING PLAYER CLASS

class Player():

    def __init__(self,name):
        self.name = name
        self.player_cards = []
        
    def remove_one(self): #probably won't need for black jack???
        return self.player_cards.pop(0)

    def add_cards(self,new_cards):

        self.player_cards.append(new_cards)

    def player_score(self):
        return self.player_cards.sum() # IDK IF THIS WILL WORK

        #find a way to add cards values together 

    def __str__(self):
        return f"Player Score: {self.player_cards.sum()}" # want to display sum for player 


# Create Dealer Class

class Dealer():

    def __init__(self,dealer_sum):
        self.dealer_cards = []
        self.dealer_sum = dealer_sum.sum(self.dealercards)
    def __str__(self):
        return f"Dealer Score: {self.dealer_sum}"

        
new_player = Player("Bryan")

print(new_player)
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


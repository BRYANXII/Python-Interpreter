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
        return sum(self.player_cards) # IDK IF THIS WILL WORK

        #find a way to add cards values together 

    def __str__(self):
        return f"Player Score: test" # want to display sum for player 


# Create Dealer Class

class Dealer():

    def __init__(self,dealer_name):
        self.dealer_name = dealer_name
        self.dealer_cards = []
    def __str__(self):
        return f"Dealer Score: {self.dealer_cards.sum()}"

dealer_one = Dealer("Johnny Sins (Dealer)")
player_one = Player("Bryan")

print(player_one)
print(dealer_one)

# CHIPS and BET SIZES

class Chips():

    def __init__(self,chip,bet_size,bank_roll):
        
        self.chip = chip
        self.bet_size = bet_size
        self.bank_roll = bank_roll

    def bet_ammount(self):
        pass

    def __str__(self):
        return (f"Player Bet Size: {self.bet_size}")


# Shuffle Deck and set game_on to True

new_deck = Deck()
new_deck.shuffle()

game_on = True

# BET AMMOUNT

def initial_bet():
    bet_ammount = input(int("Place your bet your bets! (minimum $5)\nBet ammount?: "))
    
    while:

        if bet_ammount >= 5 and bet_ammount <= bank_roll:
            break
    
        else:
            print("Please select a bet size greater than $5: ")
            continue

# GAME LOGIC

while game_on:
    if player_one bet_size > 0:
        player_cards.append(new_deck.deal_one()) # trying to deal first card to player



    # BET SIZE


    # FIRST DEAL


    # SUM OF DEALERS FIRST CARD


    # HIT OR STAY 


    # DEALER SUM


    # DEALER HIT OR STAY (MUST HIT SOFT 17)


    # DEALER BUST OR WIN


    # PUSH




# WHO WON


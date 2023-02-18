import random
import os
#suit_values = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"} #has to be created as a global variable 
suits = ('Hearts', 'Diamons', ' Spades', 'Clubs') #has to be created as a global variable 
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five': 5, 'Six':6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten':10, 'Jack':11, 'Queen':12, 'King': 13, 'Ace': 14}
# START GAME
def welcome():
    basics = """In blackjack, players attempt to reach a score of 21—without exceeding it—before the dealer hits 17. 
You can win if you don’t bust and your total is higher than the dealer cards. 
Hitting exactly 21 can mean even bigger winnings."""
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
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return (f'{self.rank} of {self.suit}') # had print() instead of return. printing deck was calling printing memory location of it

class Deck():

    def __init__(self):
        
        self.deck_of_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Cards(suit,rank) #I was calling Deck() for the append instead of Card() for created obj
                self.deck_of_cards.append(created_card)
    def shuffle(self):
        random.shuffle(self.deck_of_cards)

    def deal_one(self):

        return self.deck_of_cards.pop() #NEED TO RETURN
            # The argument passed to the method is optional. If not passed, the default index -1 is passed as an argument (index of the last item).

    def __str__(self):

        deck_comp = ''  # start with an empty string
        for card in self.deck_of_cards:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp
        

# CREATING PLAYER CLASS

class Player():

    def __init__(self,name,bank_roll):
        self.name = name
        self.bank_roll = bank_roll
        self.player_cards = []
        self.player_score = ""

    def bet_ammount(self):
        while True:
            try:
                self.bet = int(input("Place you bet ammount: "))
                if self.bet > self.bank_roll:
                    print('Cannot bet more than your current bank roll.')
                elif self.bet <= self.bank_roll:
                    print(f"{self.name} has bet {self.bet} \nCurrent Bankroll:{self.bank_roll-self.bet}")
                    return self.bank_roll - self.bet # not sure if this works?
            except:
                print('Please select a valid input. Must be a numberical value')
                continue
        
    def remove_one(self): #probably won't need for black jack???
        return self.player_cards.pop(0)

    def add_cards(self,new_cards):

        self.player_cards.append(new_cards)

    def score(self):
         
        self.player_score += card.value # IDK IF THIS WILL WORK

        #find a way to add cards values together 

    def __str__(self):
        return f"{self.name} has ${self.bank_roll}" # want to display sum for player 

    def chips(self):
        pass


# Create Dealer Class

class Dealer():

    def __init__(self,dealer_name):
        self.dealer_name = dealer_name
        self.dealer_cards = []


    def __str__(self):
        return f"Dealer: {self.dealer_name}"
    

dealer_one = Dealer("Johnny Sins")
player_one = Player("Bryan",200)

print(player_one)
print(dealer_one)
#player_one.bet_ammount()
new_deck = Deck()
new_deck.shuffle()
print (new_deck)
player_one_cards = []
while len(player_one_cards) < 2:
    player_one_cards += new_deck.deal_one()
    break

print(player_one_cards)
#print(new_deck) # currently printing the location of new_deck but not the list of it

'''for x in range (51): # had this at 53 so pop() was not working. Type Error: pop() from empty list (self.deck_of_cards)
    player_one.add_cards(new_deck.deal_one())

print(new_deck)'''

# CHIPS and BET SIZES

'''class Chips():

    def __init__(self,chip,bet_size):
        
        self.chip = chip
        self.bet_size = bet_size

    def __str__(self):
        return (f"Player Bet Size: {self.bet_size}")


# Shuffle Deck and set game_on to True

new_deck = Deck()
new_deck.shuffle()

game_on = True

# BET AMMOUNT

def initial_bet():
    bet_ammount = input(int("Place your bet your bets! (minimum $5)\nBet ammount?: "))
    
    if bet_ammount >= 5:
            print('Your bet size is {bet_ammount}')
    
    else:
            print("Please select a bet size greater than $5: ") '''
# how do I integrate the bet before the game begins??


# GAME LOGIC

'''def game_on():
    
    player_cards = []
    dealer_cards = []
    player_score = []
    dealer_score = []


    while len(player_cards) < 2:
        player_cards.append(new_deck.deal_one())
    
        #start dealing cards to player here 

        input()

        if len(player_cards) == 2:
            print(player_cards)
            break
            

        break



            # player now has two cards


game_on()'''


        
    # FIRST DEAL


    # SUM OF DEALERS FIRST CARD


    # HIT OR STAY 


    # DEALER SUM


    # DEALER HIT OR STAY (MUST HIT SOFT 17)


    # DEALER BUST OR WIN


    # PUSH




# WHO WON


import random

suits = ('Hearts', 'Diamonds', ' Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five': 5, 'Six':6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten':10, 'Jack':11, 'Queen':12, 'King': 13, 'Ace': 14}

playing = True

class Cards():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return (f'{self.rank} of {self.suit}') 
    
class Deck:

    def __init__(self):
        
        self.deck_of_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Cards(suit,rank) #I was calling Deck() for the append instead of Card() for created obj
                self.deck_of_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.deck_of_cards)
        
    def deal(self):
        
        single_card = self.deck_of_cards.pop()
        return single_card

    def __str__(self):

        deck_comp = '' #create empty string 
       
        for card in self.deck_of_cards: # for card in deck. Card isn't a variable 
            deck_comp += "\n" + card.__str__() # adds the cards string value to the empety string of deck_comp
        return "The deck has: " + deck_comp # retunrs the full string valu of deck_comp

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        # from Deck.deal() --> single Card(suit,rank)
        self.cards.append(card) #card pased in is from Deck 
        self.value += values[card.rank] # THATS HOW YOU ADD THE VALUE. FROM THE VALUES DICTIONARY
        
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces: #if self.aces has a value it will return the bolean of "True"
            self.value -= 10
            self.aces -= 1

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
        return self.total
    
    def lose_bet(self):
        self.total -= self.bet
        return self.total
    
    def take_bet(chips):
    
        while True:
                try:
                    chips.bet = int(input("How many chips would you like to bet? "))
                except: 
                    print("Sorry please provide an inter ")
                else:
                    if chips.bet > chips.total:
                        print(f"Sorry, you do not hav enough chips! You have {chips.total}")
                    else:
                        break #breaks out of while loop

def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        x = input("Hit or Stand? Enter H or S. ")
        if x[0].lower() == "h":
            hit(deck,hand)
        elif x[0].lower() == "s":
            print("Player Stands Dealer's Turn")
            playing = False

        else:
            print("Please provide a valid input")
            continue
        break

def show_some(player,dealer):

    print("\n Delaer's Hand: ")
    print("First card hidden!")
    print(dealer.cards[1])


    print("\n Player's Hand:")
    for card in player.cards:
        print(card)
    
def show_all(player,dealer):

    print("\n Dealer's Hand:")
    for card in dealer.cards:
        print(card)
    
    print("\n PLayer's Hand:")
    for card in player.cards:
        print(card)
    print(f"Value of Player's Hand is: {player.value}")

def player_busts(player,dealer,chips):
    print("Bust Player!")
    chips.lose_bet()
def player_wins(player,dealer,chips):
    print('Player Wins!')
    chips.win_bet()

def dealer_busts(player, dealer,chips):
    print('Player Wins! Dealer Busted!')
    chips.win_bet()
    
def dealer_wins(player, dealer,chips):
    print("Dealer Wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print('Dealer and player tie! PUSH')

while True:
    # Print an opening statement

    print("WELCOME TO BLACKJACK")
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())


        
    # Set up the Player's chips
    
    player_chips = Chips()
    # Prompt the Player for their bet

    take_bet()    
    # Show cards (but keep one dealer card hidden)

    show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
    

        # Prompt for Player to Hit or Stand
        
        hit_or_stand(deck,player_hand)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        
    if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)

            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    
    if player_hand.value <= 21:
            
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
        # Show all cards
        show_all(player_hand,dealer_hand)
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else: 
            push(player_hand,dealer_hand,player_chips)
    
    # Inform Player of their chips total 
   # print("\n Player total chips are at: {}".format(player_chips.total))

    # Ask to play again
    new_game = input("would you like to play again? Enter Y or N:")

    if new_game[0].lower() == "y":
        playing = True
        continue
    else:
        print('Thank you for playing!')
        break


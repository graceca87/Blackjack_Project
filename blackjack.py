import random

# random_fruits = ['apple', 'mango', 'banana'] #make a list of fruits and store it in the variable
# print(random.choice(random_fruits)) #print fruits randomly
# # What are my objects?
# Player, Dealer, Game

    #What are the adjectives that describe the game?
        
        #52 cards (4 categories - face cards (name = value), Jack = 10, Queen = 10, King = 10, Ace = method to determine (1 or 11))
        # deck = [ ] #maybe I should make it a set?
        # blackjack = c1 

    #What does the game need to do? 
        # 1. init (creates an instance)
        # 2. start game
                #deal one card to deal and two cards to player (but say you're dealing two cards to the dealer)
        # 3. hit
        # 4. stay
        # 5. blackjack
        # 6. ace
        # 7. shuffle deck
        # 8. display cards

    #What does the player need to do?
        # 1. place a bet
    #     2. choose hit or stay
    #     3. choose if ace should be 1 or 11

    # Dealer's choices should be automated
    
# def shuffle_deck():
#     list = []
#     suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
#     names = [2, 3, 4, 5, 6, 7, 8, 9, 'Jack', 'Queen', 'King', 'Ace']
#     for suit in suits:
#         for name in names:
#             list.append(f"{name} of {suit}") 
#     return list


# deck = shuffle_deck()
# print(f" this is my deck: {deck}")

# print(random.choice(deck)) 
# #^^^^^^^^^^^^^^^^^^^ This code works to create a deck and generate a random card


# def deal_card():
#     deck = shuffle_deck()
#     print(random.choice(deck)) 



# def generate_deck():
#     dictionary = {
#         "card": "f{number} of {suit}",
#         "number": {number},
#         "suit": {suit}
#         }
#     suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
#     numbers = [2, 3, 4, 5, 6, 7, 8, 9, 'Jack', 'Queen', 'King', 'Ace']
#     for suit in suits:
#         for number in numbers:
#             dictionary.append.items() 
#     print(dictionary)


class Card():

    def __init__(self, num_value, suit):  #creating each card with it's own instance
        self.suit = suit
        self.num_value = num_value
        name = num_value
        if num_value == 1:
            name = "Ace"
        if num_value == 11:
            name = "Jack"
        if num_value == 12:
            name = "Queen"
        if num_value == 13:
            name = "King"
        self.name = f"{name} of {suit}"

       
# Now that I've made the deck, I need to change the value for the face cards back to 10
# def _value_of_facecards(self, num_value, suit):
#          if suit == "Jack":
#             num_value -= 10



        
       
      
# nine_of_hearts = Card(9, "hearts")
# print(nine_of_hearts.name)

class Deck():
    cards = []

    def generate_deck(self):
        suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
        for suit in suits:
            for i in range(13):
                num_value = i + 1                   #need to add one because the range starts at index 0
                card = Card(num_value, suit)
                self.cards.append(card)

    

#     # need Draw Card method    

my_deck = Deck()
my_deck.generate_deck()
for card in my_deck.cards:
    print(card.name, card.num_value)


#This is our game's "Brain":

while True:
    player_name = input("What is your name?")
    to_do = input(f"What would you like to do, {player_name}? 1. Hit 2. Stand")

    if to_do == 1:
        player_name.hit()


 def hit(self):
        card = my_deck.deal_card()
        print(f"You received a {card}")
        self.hand = Player(self.hand)
        self.hand.append(card)
        print(self.hand)
        
player_name = Player(input("What is your name?"))
player_name.hit()

bet = int(input("""
    How much would you like to bet?:
    1. $10
    2. $100
    3. $1000
    4. $5000
    5. $10000 """))
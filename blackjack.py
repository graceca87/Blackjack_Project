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
    
def shuffle_deck():
    list = []
    suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    names = [2, 3, 4, 5, 6, 7, 8, 9, 'Jack', 'Queen', 'King', 'Ace']
    for suit in suits:
        for name in names:
            list.append(f"{name} of {suit}") 
    return list


deck = shuffle_deck()
print(f" this is my deck: {deck}")

print(random.choice(deck)) 
#^^^^^^^^^^^^^^^^^^^ This code works to create a deck and generate a random card


def deal_card():
    deck = shuffle_deck()
    print(random.choice(deck)) 



def generate_deck():
    dictionary = {
        "card": "f{number} of {suit}",
        "number": {number},
        "suit": {suit}
        }
    suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 'Jack', 'Queen', 'King', 'Ace']
    for suit in suits:
        for number in numbers:
            dictionary.append.items() 
    print(dictionary)

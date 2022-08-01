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




import random


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
        
class Deck():
    cards = []

    def generate_deck(self):
        suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
        for suit in suits:
            for i in range(13):
                num_value = i + 1                   #need to add 1 because the range starts at index 0
                card = Card(num_value, suit)
                self.cards.append(card)             #adding each instance of card to the deck (list) of cards


    def deal_card(self):
        card = random.choice(self.cards)
        # here I need to remove the random card chosen from the cards list
        # need to create a variable for the chosen card
        return card
            


my_deck = Deck()
my_deck.generate_deck()

class Dealer(Player):
    hand = []

    def __init__(self, dealer_name):
        self.dealer_name = dealer_name
        names = ["Jasper", "Candy", "Billy Bob", "Clarence", "Barb", "Montgomery", "Sam", "Mabel"]
        dealer_name = random.choice(names)

dealer = Dealer(dealer_name)


class Player():
    

    def __init__(self, name):
        self.name = name
        self.hand = []   #when a player is dealt a card it should go into their "hand" list.

    def hit(self, deck):
        card = deck.deal_card()
        self.hand.append(card)
        
        
    def show_hand(self):
        for card in self.hand:
            if card:
                print(card.name)
        return f"-------------"

    def sum_of_hand(self):
        total = 0
        for card in self.hand:
            score = card.num_value
            if score > 10:
                score = 10
            total += score
        return total
            

    # def stand(self):
    #     pass

    # def choose_ace_value(self):
    #     pass


# player_name = input("Player 1 - What is your name?")
# player = Player(player_name)
# player.hit(my_deck)
# player.hit(my_deck)
# print(f"{player.name} - Here's your hand:")
# print(player.show_hand())
# print("the sum of your cards is:")
# print(player.sum_of_hand())


#         deal_card() #if hit is selected initiate the deal card function to generate a new card. 
#         print(sum(hand))  #return the sum of the new card and the existing card(s)

# player_name = input("Player 2 - What is your name? ")
# clear_output()
# player2 = Player(player_name)
# player2.hit(my_deck)
# player2.hit(my_deck)
# print(f"{player2.name} - Here's your hand: ")
# print(player2.show_hand())
# print("the sum of your cards is: ")
# print(player2.sum_of_hand())


# print(f"the sum of {player.name}'s cards is: ")
# print(player.sum_of_hand())

# This is the Brains of the operation:
class Game():

    def __init__(self):
        self.dealer = dealer
        self.player = player

    def start(self):
        print(f"""
            Thanks for joining! The game is Blackjack.
            Your dealer today will be {dealer.dealer_name}""")
        player = Player(input("Please tell us your name"))
        print(f"Nice to meet you, {player.name}!")
        bet_answer = input(f"Would you like to place a bet? Y/n ")
        if bet_answer == "y".lower:
            bet = int(input("Great! How much would you like to put down? $"))
        print(f" Woah big spender! Let's get started...")

        player.hit(my_deck)
        player.hit(my_deck)
        print(f"{player.name} - Here's your hand:")
        print(player.show_hand())
        print("the sum of your cards is:")
        print(player.sum_of_hand())

game = Game
game.start()

while True:
    to_do = int(input(f"""
    What would you like to do, {player.name}? 
    Your choices are: 
    1. Hit 
    2. Stand
    3. Show hand
    3. Quit
    """))

    if to_do == 1:
        player.hit(my_deck)

    if to_do == 3:
        player.show_hand()

    if to_do == 3:
        break


if player.sum_of_hand() > player2.sum_of_hand():
    print(f"{player.name} wins! : )")
elif player.sum_of_hand() == player2.sum_of_hand():
    print(f"It's a draw. : ( Better luck next time!")
else:
    print(f"{player2.name} wins! : )")



class Game():

    def __init__(self):
       self.game_number = game_number

    def start(self):
        print(f"""
        Thanks for joining! The game is Blackjack.
            Your dealer today will be {dealer.name}.""")
        print(f"""          _____
                |A .  | _____
                | /.\ ||A ^  | _____
                |(_._)|| / \ ||A _  | _____
                |  |  || \ / || ( ) ||A_ _ |
                |____V||  .  ||(_'_)||( v )|
                        |____V||  |  || \ / |
                            |____V||  .  |
                                    |____V|""")
        player = Player(input("Please tell us your name "))

        clear_output(wait=True)

        print(f"""{dealer.name} says,

        '{player.name.title()} was my mother's name! And a lovely name it is. 

        ..... Let's get started, shall we? 
            
                    Good luck!'
        """)
        # bet_answer = input(f"Would you like to place a bet? Y/n ")
        # if bet_answer == "y".lower:
        #     player.bet()
        print(f"{dealer.name} dealt you two cards: ")
        print("*************************")
        player.hit(my_deck)
        player.hit(my_deck)
        print("*************************")
        print(f"\n{dealer.name} has a: ")
        dealer.hit(my_deck)
        

    def play_again(self):
        play_again = input(f"Would you like to play again? Y/n")
        if play_again == "y".lower():
            start()
        else:
            print(f"Thanks for playing {player.name}! Don't let the door hit ya in the you know what!")


# new_game = Game(dealer.name, player.name)
# new_game.start()

while True:
                                #having some issues with number responses acting funny, especially with stand 
    to_do = int(input(f"""
    It's your move, {player.name.titl()}. What would you like to do?    
    Your choices are: 
    1. Hit 
    2. Stand
    3. Show hand
    4. Add up hand
    5. Quit
    """))

    if to_do not in (1,2,3,4,5):
        print("Sorry, that's not a valid response. Please type a number to represent your choice. For example, type '1' if you want to hit or '2' if you want to stand.")

    # Player hits:
    elif to_do == 1:
        print(f"\n{dealer.name} deals you another card:")
        player.hit(my_deck)
        
        if player.sum_of_hand() == 21:
            print(f"\nYou have a Blackjack! You win!")

        elif player.sum_of_hand() > 21:
            print(f"Your cards add up to {player.sum_of_hand()}")
            print(f"\nSorry, you bust! : ( {dealer.name} wins the round")
            play_again()

    if to_do == 2:
        player.stand()

        if dealer.sum_of_hand() <= 17:
            dealer.hit(my_deck)

        elif dealer.sum_of_hand() == 21:
            print(f"\n{dealer.name} has a Blackjack and wins the round!")

        elif dealer.sum_of_hand() > 21:
            print(f"\n{dealer.name} busts and the round is over")
            break

        elif player.sum_of_hand() == 21:
            print(f"\nYou have a Blackjack! You win!")

        elif player.sum_of_hand() > 21:
            print(f"\nSorry, you bust. {dealer.name} wins the round")

        elif dealer.sum_of_hand() >= 17 and dealer.sum_of_hand() > player.sum_of_hand():
            print(f"""
            {dealer.name} has won this round.
            Better luck next time!""")

        elif dealer.sum_of_hand() == player.sum_of_hand(): 
            print(f"\nIt's a draw!")

        else:
            print(f"""
            Winner Winner Chicken Dinner!!
            {player.name}, you win! 
                    : )
            """)
    # Player can look at all the cards in their hand
    elif to_do == 3:
        print(f"""
        *********************
        {player.show_hand()}
        *********************
        """)
    # Calculates current total of cards in player's hand
    elif to_do == 4:
        print(f"Your cards add up to {player.sum_of_hand()}")

    # To Quit
    elif to_do == 5:
        print("Thanks for playing! See you next time.")
        break

    

    # class Game():

#     def __init__(self, game_number):
#        self.game_number = game_number

    # def play_again(self):
    #     play_again = input(f"Would you like to play again? Y/n")
    #     if play_again == "y".lower():
    #         player.start()
    #     else:
    #         print(f"Thanks for playing {player.name}! Don't let the door hit ya in the you know what!")

    # def start(self):
    #     print(f"""
    #     Thanks for joining! The game is Blackjack.
    #         Your dealer today will be {dealer.name}.""")
    #     print(f"""   
    #          _____
    #         |A .  | _____
    #         | /.\ ||Q ^  | _____
    #         |(_._)|| / \ ||K _  | _____
    #         |  |  || \ / || ( ) ||J_ _ |
    #         |____V||  .  ||(_'_)||( v )|
    #                |____V||  |  || \ / |
    #                       |____V||  .  |
    #                              |____V| 
                                    
    #                                      """)
    #     player = Player(input("Please tell us your name "))

    #     clear_output(wait=True)

    #     print(f"""{dealer.name} says,

    #     '{player.name.title()} was my mother's name! And a lovely name it is. 

    #     ..... Let's get started, shall we? 
            
    #                 Good luck!'
    #     """)
    #     # bet_answer = input(f"Would you like to place a bet? Y/n ")
    #     # if bet_answer == "y".lower:
    #     #     player.bet()
    #     print(f"{dealer.name} dealt you two cards: ")
    #     print("*************************")
    #     player.hit(my_deck)
    #     player.hit(my_deck)
    #     print("*************************")
    #     print(f"\n{dealer.name} has a: ")
    #     dealer.hit(my_deck)
        

# game = Game(1)
# game.start()

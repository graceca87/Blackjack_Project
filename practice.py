
from IPython.display import clear_output
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
        self.cards.remove(card)
        return card

my_deck = Deck()
my_deck.generate_deck()


class Player():

    def __init__(self, name):
        self.name = name
        self.hand = []   #when a player is dealt a card it should go into their "hand" list.


    def hit(self, deck):
        card = deck.deal_card()
        self.hand.append(card)
        # if card.num_value == "Ace":
        #     score = input(f"You drew an Ace. Would you like to count that as one or eleven? ")
        print(card.name)


    def show_hand(self):
        print(f"Here's your hand: ")
        for card in self.hand:
            if card:
                print(card.name)
        print("""
                                         _____
             _____                _____ |6    |
            |2    | _____        |5    || o o | 
            |  o  ||3    | _____ | o o || o o | _____
            |     || o o ||4    ||  o  || o o ||7    |
            |  o  ||     || o o || o o ||____9|| o o |
            |____Z||  o  ||     ||____S|       |o o o|
                   |____E|| o o |              | o o |
                          |____h|              |____L|
                    """)


    def sum_of_hand(self):
        total = 0
        for card in self.hand:
            score = card.num_value
             # changes the value for the face cards back to 10:
            if score > 10:
                score = 10
            total += score
            # if card.num_value == "Ace":
            #     score = input(f"You drew an Ace. Would you like to count that as one or eleven? ")
        return total


    def bet(self):
        earnings = 0
        bet = int(input("Great! How much would you like to put down? $"))
        print(f"Big spender!")
        earnings += bet
        return earnings

    def stand(self):
        print(f"\n{dealer.name}'s second card is a...")
        dealer.hit(my_deck)
        print(f"\n{dealer.name}'s hand is at: {dealer.sum_of_hand()}")
        print(f"\nand your hand adds up to: {player.sum_of_hand()}")
        
    # def start(self):
    #     self.hand.clear()
    #     dealer.hand.clear()
    #     # Shuffling up a fresh deck:
    #     my_deck = Deck()
    #     my_deck.generate_deck()

    # def play_again(self):
    #     answer = input(f"\nWould you like to play again? Y/n")
    #     if self.play_again != "Y".lower() and self.play_again != "n".lower():
    #         print("That is not a valid answer. Please type 'Y' or 'n'")
    #     elif self.play_again == "n".lower():
    #         print(f"Thanks for playing {player.name}!")
    #     else:
    #         player.start()
            

class Dealer(Player):
    hand = []

    def __init__(self):
        names = ["Jasper", "Candy", "Billy Bob", "Clarence", "Barb", "Monty", "Sam", "Mabel"]
        self.name = random.choice(names)

dealer = Dealer()
  
# ________________________Run Game___________________________

print(f"""
Thanks for joining! The game is Blackjack.
    Your dealer today will be {dealer.name}.""")
print(f"""
          _____        
         |A .  | _____
         | /.\ ||J ^  | _____
         |(_._)|| / \ ||Q _  | _____
         |  |  || \ / || ( ) ||K_ _ |
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
start = input("Press any key to start playing")
clear_output(wait=True)

while True:  

    # player.start() 
    print(f"{dealer.name} dealt you two cards: ")
    print("*************************")
    player.hit(my_deck)
    player.hit(my_deck)
    print("*************************")
    print(f"\n{dealer.name} has a: ")
    dealer.hit(my_deck)
                    
    to_do = int(input(f"""
    It's your move, {player.name.title()}. What would you like to do?    
    Your choices are: 
    1. Hit 
    2. Stand
    3. Show hand
    4. Add up hand
    5. Quit
    """))
    clear_output(wait=True)

    if to_do not in (1,2,3,4,5):
        print("Sorry, that's not a valid response. Please type a number to represent your choice. For example, type '1' if you want to hit or '2' if you want to stand.")

    # Player hits:
    elif to_do == 1:
        print(f"\n{dealer.name} deals you another card:")
        player.hit(my_deck)
        
        if player.sum_of_hand() == 21:
            print(f"\nYou have a Blackjack! You win!")
            # play_again = input(f"\nWould you like to play again? Y/n")
            # if play_again != "Y".lower() and play_again != "n".lower():
            #     print("That is not a valid answer. Please type 'Y' or 'n'")
            # elif play_again == "n".lower():
            #     print(f"Thanks for playing {player.name}!")
            break

        elif player.sum_of_hand() > 21:
            print(f"Your cards add up to {player.sum_of_hand()}")
            print(f"\nSorry, you bust! : ( {dealer.name} wins the round")
            # play_again = input(f"\nWould you like to play again? Y/n")
            # if play_again == "n".lower():
            #     print(f"Thanks for playing {player.name.title()}!")
            #     break
            player.play_again()
            

    # Player stands:
    if to_do == 2:
        player.stand()

        if dealer.sum_of_hand() == 21:
            print(f"\n{dealer.name} has a Blackjack and wins the round!")

        elif dealer.sum_of_hand() > 21:
            print(f"\n{dealer.name} busts and the round is over")
           

        elif player.sum_of_hand() == 21:
            print(f"\nYou have a Blackjack! You win!")
            print(f"""
            88          88                       88        88                       88         
            88          88                       88        ""                       88         
            88          88                       88                                 88         
            88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
            88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
            88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
            88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
            8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                                          ,88                                  
                                                        888P"                                  """)

        elif player.sum_of_hand() > 21:
            print(f"\nSorry, you bust. {dealer.name} wins the round")

        elif dealer.sum_of_hand() >= 17 and dealer.sum_of_hand() > player.sum_of_hand():
            print(f"""
            {dealer.name} has won this round.
            Better luck next time!""")
            # play_again = input(f"\nWould you like to play again? Y/n")
            # if play_again == "n".lower():
            #     print(f"Thanks for playing {player.name.title()}!")
            #     break

        elif dealer.sum_of_hand() == player.sum_of_hand(): 
            print(f"\nIt's a draw!")

        else:
            print(f"""
            Winner Winner Chicken Dinner!!
            {player.name.title()}, you win! 
                    : )
            """)
    # Player can look at all the cards in their hand
    elif to_do == 3:
        player.show_hand()
        
    # Calculates current total of cards in player's hand
    elif to_do == 4:
        print(f"Your cards add up to {player.sum_of_hand()}")

    # To Quit
    elif to_do == 5:
        print("\nThanks for playing! See you next time!")
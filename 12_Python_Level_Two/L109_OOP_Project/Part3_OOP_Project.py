#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """

    def __init__(self):
        self.allcards = [(s,r) for s in SUITE for r in RANKS]

    def shuffle(self):
        shuffle(self.allcards)

    def split_deck(self):
        half = int(len(self.allcards)/2)
        return [self.allcards[:half],self.allcards[half:]]


class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''

    def __init__(self, cards):
        self.cards = cards

    def add(self, new_cards):
        self.cards.extend(new_cards)

    def remove(self):
        return self.cards.pop()


class Player(Hand):
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play(self):
        drawn_card = self.hand.remove()
        print("{} has placed: {}".format(self.name,drawn_card))
        print("\n")
        return drawn_card

    def remove_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards

    def has_cards(self):
        """
        Return True if player still has cards left
        """
        return len(self.hand.cards) != 0


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

# Use the 3 classes along with some logic to play a game of war!

# Create a new deck
deck = Deck()
deck.shuffle()
half1,half2 = deck.split_deck()

# Create Players
comp = Player("computer",Hand(half1))

name = input("What is your name? ")
user = Player(name,Hand(half2))

total_rounds = 0
war_count = 0

while user.has_cards() and comp.has_cards():
    total_rounds += 1
    print("Time for a {} round".format(total_rounds))
    print("Here are the current standings")
    print(user.name + " has the count: " + str(len(user.hand.cards)))
    print(comp.name + " has the count: " + str(len(comp.hand.cards)))
    print("play a card!")
    print('\n')

    table_cards = []

    c_card = comp.play()
    u_card = user.play()

    table_cards.append(c_card)
    table_cards.append(u_card)

    if c_card[1] == u_card[1]:
        war_count += 1

        print("War!")

        table_cards.extend(user.remove_cards())
        table_cards.extend(comp.remove_cards())

        if RANKS.index(c_card[1]) < RANKS.index(u_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

    else:
        if RANKS.index(c_card[1]) < RANKS.index(u_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

print("Game over, number of rounds: " + str(total_rounds))
print("A war happened " + str(war_count) + " times")
print("\n")

if user.has_cards():
    winner = user.name
else:
    winner = comp.name

print("The winner is: {}".format(winner))




from random import shuffle


class Table:

    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer


class BJT:

    def __init__(self):
        self.hand = []

'''    def hit(self, )'''

# hit will add a card to the hand from the deck


class Cards:

    def __init__(self, suit_class, card_value, rank):
        self.suit
        self.card_value
        self.rank


class Deck:

    def __init__(self):
        self.card_index = []
        self.suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
        self.card_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                            "7": 7, "8": 8, "9": 9, "10": 10, "J": 10,
                            "Q": 10, "K": 10, "A": 11}
        for suit in self.suits:
            for card_value in self.card_values:
                self.card_index.append((suit, card_value))


deck = Deck()
shuffle(deck.card_index)

print(deck.card_index)

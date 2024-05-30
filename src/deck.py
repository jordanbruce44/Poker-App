import random
from card import Card  # Make sure to import the Card class

class Deck:
    def __init__(self):
        """Initializes a new deck of cards. (52 cards in total; 13 ranks in each of the 4 suits)
        """
        self.cards = [Card(rank, suit) for suit in Card.SUITS for rank in Card.RANKS]
        self.shuffle()

    def shuffle(self):
        """Shuffles the deck of cards."""
        random.shuffle(self.cards)

    def deal(self, count=1):
        """Deals 'count' number of cards from the deck. Returns a list of cards.
        
        Args:
            count (int): The number of cards to deal from the deck. Defaults to 1.

        Returns:
            list: A list of dealt cards.
        """
        if count > len(self.cards):
            raise ValueError("Not enough cards in the deck to deal")
        dealt_cards = self.cards[:count]
        self.cards = self.cards[count:]
        return dealt_cards

    def __repr__(self):
        """Returns a string representation of the deck."""
        return f"Deck of {len(self.cards)} cards"
    
"""
deck = Deck()  # Creates and shuffles a new deck
print(deck)    # Prints the representation of the deck

cards = deck.deal(5)  # Deals 5 cards from the deck
print(cards)          # Prints the list of dealt cards

print(deck)    # Prints the updated representation of the deck
"""
class Card:
    SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']


    def __init__(self, rank, suit):
        """Initializes a new card with a rank and suit.

        Args:
            rank (str): The rank of the card. Must be one of the values in Card.RANKS.
            suit (str): The suit of the card. Must be one of the values in Card.SUITS.

        Raises:
            ValueError: If the rank or suit is not valid.
        """
        if rank in Card.RANKS and suit in Card.SUITS:
            self.rank = rank
            self.suit = suit
        else:
            raise ValueError("Invalid card rank or suit")
        
    def __repr__(self):
        """Returns a string representation of the card."""
        return f"{self.rank} of {self.suit}"
    
    def __eq__(self, other):
        """Checks if this card's rank is equal to another card.

        Args:
            other (Card): The other card to compare this card to.

        Returns:
            bool: True if the cards' ranks are equal, False otherwise.
        """
        if not isinstance(other, Card):
            return NotImplemented
        return self.rank == other.rank  # Only compare ranks for equality

    def __lt__(self, other):
        """
        Checks if this card's rank is less than another card.
        
        Args:
            other (Card): The other card to compare this card to.
            
        Returns: 
            bool: True if this card's rank is less than the other card's rank, False otherwise.
        """
        if not isinstance(other, Card):
            return NotImplemented
        # Compare only by rank, ignoring suits
        return Card.RANKS.index(self.rank) < Card.RANKS.index(other.rank)
    
    def rank_value(self):
        """Returns the numerical value of the card's rank."""
        return Card.RANKS.index(self.rank) + 2  # +2 because '2' is the lowest rank and should have
    

"""  
# Creating some cards
card1 = Card('Ace', 'Spades')
card2 = Card('Ace', 'Hearts')
card3 = Card('King', 'Spades')

# Comparing cards
print(card1 == card2)  # True
print(card1 == card3)   # False

# Sorting cards
deck = [card1, card2, card3]
deck.sort()
print(deck)  # Output will show cards sorted by rank and then by suit
"""

    



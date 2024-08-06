import random
from collections import defaultdict, Counter

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
    
    def __hash__(self):
        return hash((self.rank, self.suit))

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
def test_card():
    # Creating some cards
    card1 = Card('Ace', 'Hearts')
    card2 = Card('King', 'Spades')
    card3 = Card('Ace', 'Spades')

    # Comparing cards
    print(card1 == card2)  # False
    print(card1 == card3)   # True

    # Sorting cards
    deck = [card1, card2, card3]
    deck.sort(reverse=True)

    print(deck)
#test_card()

class Deck:
    def __init__(self):
        """Initializes a new deck of cards. (52 cards in total; 13 ranks in each of the 4 suits)
        """
        self.cards = [Card(rank, suit) for suit in Card.SUITS for rank in Card.RANKS]
        self.shuffle()

    def shuffle(self):
        """Shuffles the deck of cards."""
        random.shuffle(self.cards)

    def remove_cards(self, cards_to_remove):
        """Removes a list of cards from the deck.

        Args:
            cards_to_remove (list): The cards to remove from the deck.
        """
        self.cards = [card for card in self.cards if card not in cards_to_remove]

    def remove_specific_card(self, rank, suit):
        """Removes a specific card from the deck.

        Args:
            rank (str): The rank of the card to remove.
            suit (str): The suit of the card to remove
        """
        self.cards = [card for card in self.cards if not (card.rank == rank and card.suit == suit)]

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
def test_deck():
    deck = Deck()  # Creates and shuffles a new deck
    print(deck)    # Prints the representation of the deck

    cards = deck.deal(5)  # Deals 5 cards from the deck
    print(cards)          # Prints the list of dealt cards

    print(deck)    # Prints the updated representation of the deck
#test_deck()

def rank_counts(cards): #obsolete function due to rank_counts_advanced
    """Returns a dictionary of the count of each rank in the hand.
    """
    """Returns a dictionary of the count of each rank in the hand, sorted by frequency and then by rank value."""
    count = Counter(card.rank for card in cards)
    # Sorting by frequency first, then by the rank value if frequencies are the same
    return dict(sorted(count.items(), key=lambda item: (-item[1], -Card.RANKS.index(item[0]))))
#print(rank_counts([Card('6', 'Spades'), Card('Ace', 'Hearts'), Card('2', 'Spades'), Card('2', 'Hearts'), Card('5', 'Spades'), Card('4', 'Hearts'), Card('5', 'Hearts')]))

def rank_counts_advanced(cards):
    """Returns a dictionary of the count of each rank in the hand, sorted by frequency and then by rank value.
    Does not record count for 1, and but records all counts from its highest to 2.
    [Card('6', 'Spades'), Card('6', 'Hearts'), Card('2', 'Spades'), Card('2', 'Hearts'), Card('6', 'Spades'), Card('4', 'Hearts'), Card('5', 'Hearts')]
    should return {3: ['6'], 2: ['6','2']}
    """
    counts = Counter(card.rank for card in cards)
    organized_counts = defaultdict(list)
    # Process ranks in descending order of count (highest to lowest)
    for rank, count in sorted(counts.items(), key=lambda item: item[1], reverse=True):
        if count > 1:
            organized_counts[count].append(rank)
            # Add rank to lower counts as well (except 1)
            for lower_count in range(count - 1, 1, -1):
                organized_counts[lower_count].append(rank)
    for count in organized_counts:
        organized_counts[count].sort(key=lambda rank: -Card.RANKS.index(rank))
    return dict(organized_counts)
def test_rank_counts_advanced():
    cards = [[Card('6', 'Spades'), Card('Ace', 'Hearts'), Card('2', 'Spades'), Card('2', 'Hearts'), Card('5', 'Spades'), Card('4', 'Hearts'), Card('5', 'Hearts')],
             [Card('6', 'Spades'), Card('6', 'Hearts'), Card('2', 'Spades'), Card('2', 'Hearts'), Card('6', 'Spades'), Card('4', 'Hearts'), Card('5', 'Hearts')],
             [Card('6', 'Spades'), Card('Ace', 'Hearts'), Card('2', 'Spades'), Card('2', 'Hearts'), Card('2', 'Diamonds'), Card('2', 'Clubs'), Card('5', 'Hearts')]]
    for card in cards:
        print(rank_counts_advanced(card))
#test_rank_counts_advanced()

def suit_counts(cards):
    """Returns a dictionary of the count of each suit in the hand.
    """
    return Counter(card.suit for card in cards)

def is_straight(cards):
    """Checks to see if the sorted hand contains a straight and returns the cards that make the straight.
    returns a list of a boolean and a list of cards. If false, the list of cards is empty
    """
    ranks = sorted(card.rank_value() for card in cards)  # Sort ranks
    if 14 in ranks:  # Ace is present, consider as high and low
        ranks.append(1)
    
    # Create a dictionary to hold cards by their rank values
    rank_to_cards = {rank: [] for rank in set(ranks)}
    for card in cards:
        rank_to_cards[card.rank_value()].append(card)
        if card.rank_value() == 14:  # Add the Ace as low as well
            rank_to_cards[1].append(card)

    # Find the highest straight
    straight_cards = []
    sorted_ranks = sorted(set(ranks),reverse=True)  # Sort unique ranks again for sequence checking
    #finds the highest straight from cards ranked high to low
    for i in range(len(sorted_ranks) - 4):  # Need at least 5 consecutive cards
        if sorted_ranks[i] - sorted_ranks[i + 4] == 4:
            # Extract one card of each rank from the sorted list to form the straight
            straight_cards = [rank_to_cards[rank][0] for rank in sorted_ranks[i:i+5]]
            break

    if straight_cards:
        straight_cards = sorted(straight_cards, key=lambda card: card.rank_value(), reverse=True)
        if straight_cards[0].rank == 'Ace' and straight_cards[-1].rank == '2':
            # Move Ace to the end if it's part of a 5-high straight
            straight_cards.append(straight_cards.pop(0))
        return True, straight_cards
    return False, []
def test_is_straight():
    cards = [[Card('8', 'Spades'), Card('Ace', 'Hearts'), Card('2', 'Spades'), Card('2', 'Hearts'), Card('5', 'Spades'), Card('4', 'Hearts'), Card('3', 'Hearts')],
             [Card('6', 'Spades'), Card('6', 'Hearts'), Card('2', 'Spades'), Card('2', 'Hearts'), Card('6', 'Spades'), Card('4', 'Hearts'), Card('5', 'Hearts')],
             [Card('3', 'Spades'), Card('Ace', 'Hearts'), Card('4', 'Spades'), Card('2', 'Hearts'), Card('2', 'Diamonds'), Card('5', 'Clubs'), Card('6', 'Hearts')]]
    for card in cards:
        print(is_straight(card))
#test_is_straight()

def is_flush(cards):
    """Checks to see if the hand contains a flush and returns the cards that make the flush.
    returns a list of a boolean and a list of cards. If false, the list of cards is empty
    """
    suits = [card.suit for card in cards]
    suit_counts = Counter(suits)
    
    flush_suit = next((suit for suit, count in suit_counts.items() if count >= 5), None)
    if flush_suit:
        flush_cards = [card for card in cards if card.suit == flush_suit]
        flush_cards = sorted(flush_cards, key=lambda card: card.rank_value(), reverse=True)[:5]
        return True, flush_cards
    return False, []
def test_is_flush():
    cards = [[Card('6', 'Hearts'), Card('Ace', 'Hearts'), Card('2', 'Spades'), Card('2', 'Hearts'), Card('5', 'Spades'), Card('4', 'Hearts'), Card('5', 'Hearts')],
             [Card('6', 'Spades'), Card('6', 'Hearts'), Card('2', 'Spades'), Card('2', 'Hearts'), Card('6', 'Spades'), Card('4', 'Hearts'), Card('5', 'Hearts')]]
    for card in cards:
        print(is_flush(card))
#test_is_flush()

def is_straight_flush(suit,cards):
    """Checks to see if the hand contains a straight flush and returns the cards that make the straight flush.
    returns a list of a boolean and a list of cards. If false, the list of cards is empty
    """
    #takes all cards from flush suit
    flush_cards = [card for card in cards if card.suit == suit]
    #checks if the flush suit has a straight
    straight_flush, straight_flush_cards = is_straight(flush_cards)
    return straight_flush, straight_flush_cards
def test_is_straight_flush():
    cards = [
        [Card('6', 'Hearts'), Card('Ace', 'Hearts'), Card('2', 'Spades'), Card('2', 'Hearts'), Card('3', 'Hearts'), Card('4', 'Hearts'), Card('5', 'Hearts')],
        [Card('6', 'Spades'), Card('Ace', 'Hearts'), Card('2', 'Spades'), Card('2', 'Hearts'), Card('3', 'Spades'), Card('4', 'Spades'), Card('5', 'Spades')]
    ]
    for card_set in cards:
        print(is_straight_flush('Hearts', card_set))
#test_is_straight_flush()

def is_four_of_a_kind(cards, rank_counts):
    """Checks to see if the hand contains four of a kind and returns the cards that make the four of a kind and the next highest card.
    returns a list of a boolean and a list of cards. If false, the list of cards is empty
    """
    if 4 in rank_counts:
        rank = rank_counts[4][0]  # Since the list is sorted, we take the first element
        four_of_a_kind_cards = [card for card in cards if card.rank == rank]
        remaining_cards = [card for card in cards if card.rank != rank]
        return True, four_of_a_kind_cards + remaining_cards[:1]
    return False, []
def test_is_four_of_a_kind():
    cards1= [Card('6', 'Spades'), Card('Ace', 'Hearts'), Card('2', 'Spades'), Card('2', 'Hearts'), Card('2', 'Diamonds'), Card('2', 'Clubs'), Card('5', 'Hearts')]
    cards2 = [Card('6', 'Spades'), Card('Ace', 'Hearts'), Card('2', 'Spades'), Card('2', 'Hearts'), Card('3', 'Hearts'), Card('4', 'Hearts'), Card('5', 'Hearts')]
    print(is_four_of_a_kind(cards1, rank_counts_advanced(cards1)))
    print(is_four_of_a_kind(cards2, rank_counts_advanced(cards2)))
#test_is_four_of_a_kind()

def is_full_house(cards, rank_counts):
    """Checks to see if the hand contains a full house and returns the cards that make the full house.
    returns a list of a boolean and a list of cards. If false, the list of cards is empty
    """
    if 3 in rank_counts:
        three_rank = rank_counts[3][0]  # Assuming the first one is the highest for a full house
        # Check for a pair
        for rank in rank_counts[2]:
            if rank != three_rank:
                full_house_cards = [card for card in cards if card.rank == three_rank][:3] + [card for card in cards if card.rank == rank][:2] #
                return True, full_house_cards
    return False, []
def test_is_full_house():
    cards = [[Card('6', 'Spades'), Card('Ace', 'Hearts'), Card('2', 'Spades'), Card('2', 'Hearts'), Card('2', 'Diamonds'), Card('3', 'Clubs'), Card('3', 'Hearts')], #regular flush
                [Card('6', 'Spades'), Card('3', 'Spades'), Card('2', 'Spades'), Card('2', 'Hearts'), Card('2', 'Diamonds'), Card('3', 'Clubs'), Card('3', 'Hearts')], #2 sets
                [Card('6', 'Spades'), Card('3', 'Spades'), Card('2', 'Spades'), Card('2', 'Hearts'), Card('3', 'Diamonds'), Card('3', 'Clubs'), Card('3', 'Hearts')], #quads and par
                [Card('6', 'Spades'), Card('3', 'Spades'), Card('2', 'Spades'), Card('8', 'Hearts'), Card('10', 'Diamonds'), Card('3', 'Clubs'), Card('3', 'Hearts')], #set, not pair
                [Card('6', 'Spades'), Card('Ace', 'Hearts'), Card('2', 'Spades'), Card('2', 'Hearts'), Card('3', 'Diamonds'), Card('4', 'Clubs'), Card('5', 'Hearts')]] #straight
    for card in cards:
        print(is_full_house(card, rank_counts_advanced(card)))
#test_is_full_house()

def is_set(cards, rank_counts):
    """Checks to see if the hand contains a set and returns the cards that make the set.
    returns a list of a boolean and a list of cards. If false, the list of cards is empty
    """
    if 3 in rank_counts:
        rank = rank_counts[3][0]
        three_of_a_kind_cards = [card for card in cards if card.rank == rank]
        remaining_cards = [card for card in cards if card.rank != rank]
        return True, three_of_a_kind_cards + remaining_cards[:2]
    return False, []
def test_is_set():
    cards = [[Card('6', 'Spades'), Card('Ace', 'Hearts'), Card('2', 'Spades'), Card('2', 'Hearts'), Card('2', 'Diamonds'), Card('3', 'Clubs'), Card('5', 'Hearts')],
                [Card('6', 'Spades'), Card('Ace', 'Hearts'), Card('2', 'Spades'), Card('2', 'Hearts'), Card('3', 'Hearts'), Card('4', 'Hearts'), Card('5', 'Hearts')]]
    for card in cards:
        print(is_set(card, rank_counts_advanced(card)))
#test_is_set()

def is_two_pair(cards, rank_counts):
    """Checks to see if the hand contains two pairs and returns the cards that make the two pairs and the next highest card.
    returns a list of a boolean and a list of cards. If false, the list of cards is empty
    """
    if 2 in rank_counts and len(rank_counts[2]) >= 2:
        first_pair_rank = rank_counts[2][0]
        second_pair_rank = rank_counts[2][1]
        two_pair_cards = [card for card in cards if card.rank == first_pair_rank][:2] + [card for card in cards if card.rank == second_pair_rank][:2]
        remaining_cards = [card for card in cards if card.rank not in {first_pair_rank, second_pair_rank}]
        #if there's no remaining card, return one additional card from the deck if it's not one of the two pairs
        if len(remaining_cards) == 0:
            return True, two_pair_cards + [card for card in cards if card.rank not in two_pair_cards[:2]][:1]
        return True, two_pair_cards + remaining_cards[:1]
    return False, []
def test_is_two_pair():
    cards = [[Card('6', 'Spades'), Card('6', 'Hearts'), Card('2', 'Spades'), Card('2', 'Hearts'), Card('3', 'Diamonds'), Card('4', 'Clubs'), Card('5', 'Hearts')],
                [Card('6', 'Spades'), Card('Ace', 'Hearts'), Card('2', 'Spades'), Card('2', 'Hearts'), Card('3', 'Hearts'), Card('4', 'Hearts'), Card('5', 'Hearts')]]
    for card in cards:
        print(is_two_pair(card, rank_counts_advanced(card)))
#test_is_two_pair()

def is_pair(cards, rank_counts):
    """Checks to see if the hand contains a pair and returns the cards that make the pair and the next highest cards.
    returns a list of a boolean and a list of cards. If false, the list of cards is empty
    """
    if 2 in rank_counts:
        rank = rank_counts[2][0]
        pair_cards = [card for card in cards if card.rank == rank][:2]
        remaining_cards = [card for card in cards if card.rank != rank]
        return True, pair_cards + remaining_cards[:3]
    return False, []
def test_is_pair():
    cards = [[Card('6', 'Spades'), Card('Ace', 'Hearts'), Card('2', 'Spades'), Card('2', 'Hearts'), Card('3', 'Diamonds'), Card('4', 'Clubs'), Card('5', 'Hearts')],
                [Card('6', 'Spades'), Card('Ace', 'Hearts'), Card('2', 'Spades'), Card('8', 'Hearts'), Card('3', 'Diamonds'), Card('4', 'Clubs'), Card('5', 'Hearts')]]
    for card in cards:
        print(is_pair(card, rank_counts_advanced(card)))
#test_is_pair()

class Hand(Deck):
    """A class representing a hand of cards. Inherits from the Deck class.
    """
    def __init__(self, cards):
        self.cards = cards
    
    def all_cards(self):
        """Returns all the cards in the hand in a sorted list
        """
        return sorted(self.cards, key=lambda card: card.rank_value(), reverse=True)
    
    def evaluate_hand(self):
        """Evaluates the hand and returns the best possible hand.
        """
        cards = self.cards
        rank_count = rank_counts_advanced(cards)
        sorted_cards = sorted(cards, key=lambda card: card.rank_value(), reverse=True)
        
        # straight flush, four of a kind, full house, flush, straight, three of a kind, two pair, one pair, high card
        strengths_list = [0, 0, 0, 0, 0, 0, 0, 0, 1]
        strengths_dict = {
            "Straight Flush": [],
            "Four of a Kind": [],
            "Full House": [],
            "Flush": [],
            "Straight": [],
            "Three of a Kind": [],
            "Two Pair": [],
            "One Pair": [],
            "High Card": sorted_cards[:5]
        }

        # Straight and flush checks
        straight_exists, straight_cards = is_straight(sorted_cards)
        flush_exists, flush_cards = is_flush(sorted_cards)

        # Check for straight flush
        if straight_exists and flush_exists:
            # list comprehension to add all cards from sorted_cards to list if same suit as flush_cards
            straight_flush_exists, straight_flush_cards = is_straight_flush(flush_cards[0].suit, sorted_cards)

            if straight_flush_exists:
                strengths_list[0] = 1
                strengths_dict["Straight Flush"] = straight_flush_cards[:5]

        # Check for four of a kind
        four_of_a_kind_exists, four_kind_cards = is_four_of_a_kind(sorted_cards, rank_count)
        if four_of_a_kind_exists:
            strengths_list[1] = 1
            strengths_dict["Four of a Kind"] = four_kind_cards

        # Check for full house
        full_house_exists, full_house_cards = is_full_house(sorted_cards, rank_count)
        if full_house_exists:
            strengths_list[2] = 1
            strengths_dict["Full House"] = full_house_cards

        # Check for flush
        if flush_exists:
            strengths_list[3] = 1
            strengths_dict["Flush"] = flush_cards[:5]
        
        # Check for straight
        if straight_exists:
            strengths_list[4] = 1
            strengths_dict["Straight"] = straight_cards[:5]

        # Check for three of a kind
        set_exists, set_cards = is_set(sorted_cards, rank_count)
        if set_exists:
            strengths_list[5] = 1
            strengths_dict["Three of a Kind"] = set_cards

        # Check for two pairs
        two_pair_exists, two_pair_cards = is_two_pair(sorted_cards, rank_count)
        if two_pair_exists:
            strengths_list[6] = 1
            strengths_dict["Two Pair"] = two_pair_cards

        # Check for one pair
        pair_exists, pair_cards = is_pair(sorted_cards, rank_count)
        if pair_exists:
            strengths_list[7] = 1
            strengths_dict["One Pair"] = pair_cards

        return strengths_list, strengths_dict   
def test_evaluate_hand():
    cards = [
        Card('3', 'Spades'), 
        Card('4', 'Hearts'), 
        Card('3', 'Clubs'), 
        Card('3', 'Diamonds'), 
        Card('4', 'Clubs'), 
        Card('4', 'Diamonds'), 
        Card('4', 'Spades')
    ]
    hand = Hand(cards)
    print(hand.evaluate_hand()) 
    cards = [
        Card('6', 'Spades'),
        Card('Ace', 'Hearts'), 
        Card('2', 'Spades'), 
        Card('2', 'Hearts'), 
        Card('3', 'Hearts'), 
        Card('4', 'Hearts'), 
        Card('5', 'Hearts')
    ]
    hand = Hand(cards)
    print(hand.evaluate_hand())  
#test_evaluate_hand()
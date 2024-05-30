from itertools import combinations
from collections import Counter
from card import Card

class Hand:
    def __init__(self, cards):
        self.cards = cards

    def rank_counts(self):
        """Returns a dictionary of the count of each rank in the hand."""
        return Counter(card.rank for card in self.cards)

    def is_straight(self):
        """Checks to see if the hand contains a straight and returns the cards that make the straight.
        
        Returns:
            tuple: (bool, list) A tuple where the first item is True if the hand is a straight, 
                False otherwise, and the second item is the list of cards forming the straight.
        """
        ranks = sorted(card.rank_value() for card in self.cards)  # Sort ranks
        if 14 in ranks:  # Ace is present, consider as high and low
            ranks.append(1)
        
        # Create a dictionary to hold cards by their rank values
        rank_to_cards = {rank: [] for rank in set(ranks)}
        for card in self.cards:
            rank_to_cards[card.rank_value()].append(card)
            if card.rank_value() == 14:  # Add the Ace as low as well
                rank_to_cards[1].append(card)

        # Find the highest straight
        straight_cards = []
        sorted_ranks = sorted(set(ranks))  # Sort unique ranks again for sequence checking
        for i in range(len(sorted_ranks) - 4):  # Need at least 5 consecutive cards
            if sorted_ranks[i + 4] - sorted_ranks[i] == 4:
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
    
    def is_flush(self):
        """Checks to see if at least 5 cards in the hand have the same suit and returns those cards.
        
        Returns:
            tuple: (bool, list) A tuple where the first item is True if the hand is a flush, 
                False otherwise, and the second item is the list of cards forming the flush.
        """
        suits = [card.suit for card in self.cards]
        suit_counts = Counter(suits)
        
        flush_suit = next((suit for suit, count in suit_counts.items() if count >= 5), None)
        if flush_suit:
            flush_cards = [card for card in self.cards if card.suit == flush_suit]
            flush_cards = sorted(flush_cards, key=lambda card: card.rank_value(), reverse=True)[:5]  # Get the top 5 cards
            return True, flush_cards
        return False, []
    
    def evaluate_hand(self):
        # First, get the rank counts
        rank_count = self.rank_counts()
        # Sort counts in descending order to easily identify the highest combinations
        counts = sorted(rank_count.values(), reverse=True)
        ranks = sorted(rank_count, key=lambda rank: rank_count[rank], reverse=True)

        # Get cards sorted by rank, high to low
        sorted_cards = sorted(self.cards, key=lambda card: card.rank_value(), reverse=True)

        # Check for four of a kind
        if counts[0] == 4:
            four_kind_cards = [card for card in sorted_cards if card.rank == ranks[0]][:4]
            kicker = [card for card in sorted_cards if card.rank != ranks[0]][0]
            return "Four of a Kind", four_kind_cards + [kicker]

        # Check for full house
        if counts[0] == 3 and counts[1] >= 2:
            three_kind_cards = [card for card in sorted_cards if card.rank == ranks[0]][:3]
            two_kind_cards = [card for card in sorted_cards if card.rank == ranks[1]][:2]
            return "Full House", three_kind_cards + two_kind_cards
            
        # straight and flush functions
        is_flush, flush_cards = self.is_flush()
        is_straight, straight_cards = self.is_straight()
        
        # Check for straight flush
        if is_flush and is_straight:
        # Find intersection of flush and straight cards based on suits and ranks
            straight_flush_cards = [card for card in straight_cards if card in flush_cards]
            if len(straight_flush_cards) == 5:
                # Sort the potential straight flush cards to check order
                straight_flush_cards_sorted = sorted(straight_flush_cards, key=lambda card: card.rank_value(), reverse=True)
                # Check for five-high straight flush
                if straight_flush_cards_sorted[0].rank == 'Ace' and straight_flush_cards_sorted[-1].rank == '2':
                    # If Ace is high but actually should be low
                    straight_flush_cards_sorted.append(straight_flush_cards_sorted.pop(0))
                return "Straight Flush", straight_flush_cards_sorted
        
        # Check for flush
        if is_flush:
            return "Flush", flush_cards

        # Check for straight
        if is_straight:
            return "Straight", straight_cards
        
        # Check for three of a kind
        if counts[0] == 3:
            three_kind_cards = [card for card in sorted_cards if card.rank == ranks[0]][:3]
            kickers = [card for card in sorted_cards if card.rank != ranks[0]][:2]
            return "Three of a Kind", three_kind_cards + kickers

        # Check for two pairs
        if counts[0] == 2 and counts[1] == 2:
            first_pair_cards = [card for card in sorted_cards if card.rank == ranks[0]][:2]
            second_pair_cards = [card for card in sorted_cards if card.rank == ranks[1]][:2]
            kicker = [card for card in sorted_cards if card.rank not in (ranks[0], ranks[1])][0]
            return "Two Pair", first_pair_cards + second_pair_cards + [kicker]

        # Check for one pair
        if counts[0] == 2:
            pair_cards = [card for card in sorted_cards if card.rank == ranks[0]][:2]
            kickers = [card for card in sorted_cards if card.rank != ranks[0]][:3]
            return "One Pair", pair_cards + kickers

        # If none of the above, return high card
        high_cards = sorted_cards[:5]
        return "High Card", high_cards



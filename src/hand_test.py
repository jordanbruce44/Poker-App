from hand import Hand
from card import Card

"""# Example Usage of straight flush (good)
cards = [
    Card('Ace', 'Spades'), 
    Card('6', 'Hearts'), 
    Card('3', 'Hearts'), 
    Card('4', 'Hearts'), 
    Card('7', 'Hearts'), 
    Card('5', 'Hearts'), 
    Card('9', 'Spades')]
hand = Hand(cards)
print(hand.evaluate_hand())  
# Should output ('Straight Flush', [7 of Hearts, 6 of Hearts, 5 of Hearts, 4 of Hearts, 3 of Hearts])
"""

#"""# Example Usage of five-high straight flush
cards = [
    Card('10', 'Spades'), 
    Card('Ace', 'Hearts'), 
    Card('3', 'Hearts'), 
    Card('4', 'Hearts'), 
    Card('2', 'Hearts'), 
    Card('5', 'Hearts'), 
    Card('9', 'Spades')]
hand = Hand(cards)
print(hand.evaluate_hand())  
# Should output ('Flush', [5 of Hearts, 4 of Hearts, 3 of Hearts, 2 of Hearts, Ace of Hearts])
#"""

"""# Example Usage of four of a kind (good)
cards = [
    Card('4', 'Spades'),
    Card('4', 'Clubs'), 
    Card('Queen', 'Spades'), 
    Card('Jack', 'Spades'), 
    Card('4', 'Diamonds'),
    Card('Ace', 'Spades'), 
    Card('4', 'Hearts')  
]
hand = Hand(cards)
print(hand.evaluate_hand())  
# Should output ('Four of a Kind', [4 of Spades, 4 of Clubs, 4 of Diamonds, 4 of Hearts, Ace of Spades])
"""

"""# Example Usage of flush (good)
cards = [
    Card('4', 'Spades'),
    Card('King', 'Clubs'), 
    Card('Queen', 'Spades'), 
    Card('Jack', 'Spades'), 
    Card('10', 'Spades'),
    Card('Ace', 'Spades'), 
    Card('3', 'Hearts')  
]
hand = Hand(cards)
print(hand.evaluate_hand())  
# Should output ('Flush', [Ace of Spades, Queen of Spades, Jack of Spades, 10 of Spades, 4 of Spades])
"""

"""# Example Usage of straight (good)
cards = [
    Card('Ace', 'Spades'), 
    Card('6', 'Hearts'), 
    Card('3', 'Clubs'), 
    Card('4', 'Diamonds'), 
    Card('7', 'Hearts'), 
    Card('5', 'Hearts'), 
    Card('9', 'Hearts')
]
hand = Hand(cards)
print(hand.evaluate_hand())  
# Should output ('Straight', [7 of Hearts, 6 of Hearts, 5 of Hearts, 4 of Diamonds, 3 of Clubs])
"""

"""# Example Usage of  five-high straight
cards = [
    Card('Ace', 'Spades'), 
    Card('Ace', 'Hearts'), 
    Card('3', 'Clubs'), 
    Card('4', 'Diamonds'), 
    Card('2', 'Hearts'), 
    Card('5', 'Hearts'), 
    Card('9', 'Hearts')
]
hand = Hand(cards)
print(hand.evaluate_hand())  
# Should output ('Straight', [7 of Hearts, 6 of Hearts, 5 of Hearts, 4 of Diamonds, 3 of Clubs])
"""

"""# Example Usage of three of a kind (good)
cards = [
    Card('4', 'Spades'),
    Card('4', 'Clubs'), 
    Card('Queen', 'Spades'), 
    Card('Jack', 'Spades'), 
    Card('4', 'Diamonds'),
    Card('Ace', 'Spades'), 
    Card('3', 'Hearts')  
]
hand = Hand(cards)
print(hand.evaluate_hand())  
# Should output ('Three of a Kind', [4 of Spades, 4 of Clubs, 4 of Diamonds, Ace of Spades, Queen of Spades])
"""

"""# Example Usage of two pair (good)
cards = [
    Card('4', 'Spades'),
    Card('4', 'Clubs'), 
    Card('Queen', 'Spades'), 
    Card('Jack', 'Spades'), 
    Card('3', 'Diamonds'),
    Card('Ace', 'Spades'), 
    Card('3', 'Hearts')  
]
hand = Hand(cards)
print(hand.evaluate_hand())  
# Should output ('Two Pair', [4 of Spades, 4 of Clubs, 3 of Diamonds, 3 of Hearts, Ace of Spades])
"""

"""# Example Usage of one pair (good)
cards = [
    Card('4', 'Spades'),
    Card('4', 'Clubs'), 
    Card('Queen', 'Spades'), 
    Card('Jack', 'Spades'), 
    Card('3', 'Diamonds'),
    Card('Ace', 'Spades'), 
    Card('9', 'Hearts')  
]
hand = Hand(cards)
print(hand.evaluate_hand())  
# Should output ('One Pair', [4 of Spades, 4 of Clubs, Ace of Spades, Queen of Spades, Jack of Spades])
"""

"""# Example Usage of high card (good)
cards = [
    Card('4', 'Spades'),
    Card('King', 'Clubs'), 
    Card('Queen', 'Spades'), 
    Card('Jack', 'Spades'), 
    Card('3', 'Diamonds'),
    Card('Ace', 'Spades'), 
    Card('9', 'Hearts')  
]
hand = Hand(cards)
print(hand.evaluate_hand())  
# Should output ('High Card', [Ace of Spades, King of Clubs, Queen of Spades, Jack of Spades, 9 of Hearts])
#"""
from poker import Deck, Hand

class Player:
    def __init__(self, name):
        self.name = name
        self.hand_cards = []  # The two initial cards
        self.full_hand = None  # Full hand including community cards

    def set_hand(self, cards):
        self.hand_cards = cards

    def combine_with_community(self, community_cards):
        self.full_hand = Hand(self.hand_cards + community_cards)
        return self.full_hand.evaluate_hand()

    def __str__(self):
        return f"{self.name} with cards: {', '.join(map(str, self.hand_cards))}"
    
class Game:
    def __init__(self, players, deck):
        """Initializes a game with a list of players and a deck
        Args:
            players (list): A list of players
            deck (Deck): A deck of cards
        """
        self.players = players
        self.deck = deck
        self.community_cards = []
    
    def deal_hands(self):
        """Deals two cards to each player
        """
        for player in self.players:
            player.set_hand(self.deck.deal(2))

    def simulate_phases(self, phases):
        if 'flop' in phases:
            self.community_cards.extend(self.deck.deal(3))
        if 'turn' in phases:
            self.community_cards.extend(self.deck.deal(1))
        if 'river' in phases:
            self.community_cards.extend(self.deck.deal(1))

    def evaluate_hands(self):
        results = {}
        for player in self.players:
            results[player.name] = player.combine_with_community(self.community_cards)
        return results
        

# Simulate the round and format the output:
def print_results(game):
    print("Community Cards:")
    for card in game.community_cards:
        print(f"  {card}")
    print()

    for player in game.players:
        print(f"{player}'s hand: {', '.join(str(card) for card in player.hand_cards)}")
        hand_result = player.full_hand.evaluate_hand()
        for key in hand_result[1]:  # Access the dictionary of hand evaluation
            if hand_result[1][key]:  # Only print if the hand type has cards
                print(f"  {key}: {', '.join(str(card) for card in hand_result[1][key])}")
        print()

if __name__ == "__main__":
    player_names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"]
    players = [Player(name) for name in player_names]  # Create Player objects from names
    deck = Deck()  # Create a deck instance
    game = Game(players, deck)  # Pass Player objects and the deck to the Game constructor
    game.deal_hands()
    game.simulate_phases(['flop', 'turn', 'river'])
    results = game.evaluate_hands()
    print_results(game)
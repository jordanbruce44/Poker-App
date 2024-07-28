from poker import Deck, Hand
from game import Player, Game, print_results
import concurrent.futures

"""
Golden Nugget Ultimate Texas Hold'em
-------------------------------------
This is a simulation of the Golden Nugget Ultimate Texas Hold'em game.
The game is played with a single deck of cards and the players are dealt
two cards each. The community cards are dealt in two phases: the flop, and 
the turn and river together.

I'm trying to find the estimated payout when playing the game with the side bets
Diamonds and Trips. The payouts are as follows (multiplied by the bet):
- Diamonds: 4 cards: 3, 5 cards: 10, 6 cards: 30, 
7 cards: 100, 8 cards: 300, 9 cards: 1000
- Trips: Straight Flush: 40, Four of a Kind: 30, Full House: 8, 
Flush: 7, Straight: 4, Three of a Kind: 3

The players aren't playing against each other, but against the dealer. The dealer
must have a pair or better to qualify. If the dealer doesn't qualify, the player
wins the Ante bet and the Play bet is returned. If the dealer qualifies, the player
wins if their hand is better than the dealer's.

Diamonds: The player wins if they have a certain number of diamonds in their 
personal hand, the community cards, and the dealer's cards (out of 9 total cards).
"""


diamonds_rewards = {
    4:3,
    5:10,
    6:30,
    7:100,
    8:300,
    9:1000,
}

trips_rewards = {
    "Straight Flush": 40,
    "Four of a Kind": 30,
    "Full House": 8,
    "Flush": 7,
    "Straight": 4,
    "Three of a Kind": 3,
}

def simulate_trips(num_simulations=10000):
    # Initialize payout counts
    payouts = {key: 0 for key in trips_rewards.keys()}

    # Start the simulation loop
    for _ in range(num_simulations):
        # Initialize a new deck and shuffle it
        deck = Deck()
        
        # Create a player
        player = Player("Simulated Player")
        
        # Initialize the game with one player
        game = Game([player], deck)
        
        # Deal hands and simulate all game phases
        game.deal_hands()
        game.simulate_phases(['flop', 'turn', 'river'])
        
        # Combine player's hand with community cards
        player.combine_with_community(game.community_cards)
        
        # Evaluate the player's hand
        _, strengths_dict = player.full_hand.evaluate_hand()

        # Record the highest payout hand
        for hand_type in trips_rewards.keys():  # Ensures checking from highest to lowest
            if strengths_dict[hand_type]:  # Check if hand type is not empty
                payouts[hand_type] += 1
                break  # Stop after recording the highest hand type

    # Calculate expected payouts
    expected_payout = sum(trips_rewards[hand] * (count / num_simulations) for hand, count in payouts.items())
    return expected_payout, payouts

def simulate_diamonds(num_simulations=100000):
    counts = {k: 0 for k in range(4, 10)}  # Initialize counts for each diamond count starting from 4 to 9
    
    for _ in range(num_simulations):
        deck = Deck()  # Reset the deck for each simulation
        player = Player("Player")
        dealer = Player("Dealer")
        game = Game([player, dealer], deck)
        
        game.deal_hands()  # Deal hands to both player and dealer
        game.simulate_phases(['flop', 'turn', 'river'])
        
        # Combine all cards to count diamonds
        all_cards = player.hand_cards + dealer.hand_cards + game.community_cards
        diamond_count = sum(1 for card in all_cards if card.suit == 'Diamonds')
        
        if diamond_count >= 4:
            counts[diamond_count] += 1

    # Calculate expected payouts
    expected_payout = sum(diamonds_rewards.get(d, 0) * (count / num_simulations) for d, count in counts.items())
    return expected_payout, counts

def main():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        trips_future = executor.submit(simulate_trips, 100000)  # 10,000 simulations
        diamonds_future = executor.submit(simulate_diamonds, 100000)  # 10,000 simulations

        # Wait for both futures to complete
        trips_result = trips_future.result()
        diamonds_result = diamonds_future.result()

        print("Expected Payout for Trips Side Bet:\n", trips_result[0])
        print("Counts of Each Hand Type for Trips:\n", trips_result[1])
        print("Percentage of Each Hand Type for Trips:\n", {k: v / 100000 for k, v in trips_result[1].items()})
        print("Expected Payout for Diamonds Side Bet:\n", diamonds_result[0])
        print("Diamond Counts Distribution:\n", diamonds_result[1])
        print("Percentage of Each Number of Diamonds:\n", {k: v / 100000 for k, v in diamonds_result[1].items()})

if __name__ == "__main__":
    main()
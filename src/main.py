import streamlit as st
from poker import Card, Deck, Hand
from game import Player, Game

# Initialize the deck
deck = Deck()

# Helper function to get available ranks and suits
def get_available_ranks_suits(deck):
    available_ranks = sorted(set(card.rank for card in deck.cards), key=lambda x: Card.RANKS.index(x))
    available_suits = sorted(set(card.suit for card in deck.cards), key=lambda x: Card.SUITS.index(x))
    return available_ranks, available_suits

def main():
    st.title('Poker Odds Calculator')

    available_ranks, available_suits = get_available_ranks_suits(deck)

    # Select the first card
    col1, col2 = st.columns(2)
    with col1:
        selected_rank1 = st.selectbox('Select rank for Card 1:', options=available_ranks, index=0, key='rank1')
    with col2:
        selected_suit1 = st.selectbox('Select suit for Card 1:', options=available_suits, index=0, key='suit1')

    # Remove the selected card from the deck
    if selected_rank1 and selected_suit1:
        deck.remove_specific_card(selected_rank1, selected_suit1)

    # Update available cards for the second selection
    available_ranks, available_suits = get_available_ranks_suits(deck)

    # Select the second card
    col3, col4 = st.columns(2)
    with col3:
        selected_rank2 = st.selectbox('Select rank for Card 2:', options=available_ranks, index=0, key='rank2')
    with col4:
        selected_suit2 = st.selectbox('Select suit for Card 2:', options=available_suits, index=0, key='suit2')

    # Display selected cards
    st.write(f"You have selected: {selected_rank1} of {selected_suit1} and {selected_rank2} of {selected_suit2}")

if __name__ == "__main__":
    main()
# Tarot Reading

## Overview
The purpose of this project is to develop a simple tarot card selector. This way, a reading is still possible even if you don't have a deck at hand! The program is based on a few functions which define the deck, shuffle it, select the cards, and announce the result.

## Functionality
The tarot card is composed of the major arcana (written out in list form) and additional cards in four suits, similar to a regular deck of cards. The suit_card_combine function takes an iterative approach to the list of suits and cards to create a single list containing one card of each suit.

```
# Function to put together suits and cards
def suit_card_combine(suits, cards):
    deck = []
    for suit in suits:
        for card in cards:
            deck.append(card + " of " + suit)
    return deck
```

The shuffle_deck function takes a deck and generates a random number to select that card to 

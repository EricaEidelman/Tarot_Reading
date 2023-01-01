# Tarot Reading

## Overview
The purpose of this project is to develop a simple tarot card selector. This way, a reading is still possible even if you don't have a deck at hand! The program is based on a few functions which define the deck, shuffle it, select the cards, and announce the result.

## Resources
Software: Python 3.7.6

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

The shuffle_deck function takes a deck and generates a random number to select that card to a list representing the shuffled deck. The same card is removed from the original input deck so that the shuffled deck does not have duplicate cards.

```
# Function to shuffle the complete deck
def shuffle_deck(deck):
    i = 78
    shuffled_deck = []
    while i > 0:
        index = random.randrange(0,i)
        shuffled_deck.append(deck[index])
        deck.remove(deck[index])
        i -= 1
    return shuffled_deck
```

The card_selector and card_teller functions then loop through the shuffled deck to select three cards (past, present, and future) and print an output telling the user what the cards are.

```
# Function to select three cards
def card_selector(shuffled_deck):
    i = 78
    selected_cards = []
    while i > 75:
        selected_cards.append(shuffled_deck[random.randrange(0,i)])
        i -= 1
    return(selected_cards)

# Function to announce selected cards
def card_teller(selected_deck):
    print("Your past card is " + selected_deck[0])
    print("Your present card is " + selected_deck[1])
    print("Your future card is " + selected_deck[2])
```

The image below shows what the program output is when run in its entirety.

![This is an image](https://github.com/EricaEidelman/Tarot_Reading/blob/main/Output.png)

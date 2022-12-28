# Imports
import random

# Write out the cards
major_arcana = ["The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor", "The Hierophant",
 "The Lovers", "The Chariot", "Strength", "The Hermit", "Wheel of Fortune", "Justice", "The Hanged Man", "Death", 
 "Temperance", "The Devil", "The Tower", "The Star", "The Moon", "The Sun", "Judgement", "The World"]

suits = ["Wands", "Cups", "Swords", "Coins"]
cards = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Page", "Knight", "Queen", "King"]

# Function to put together suits and cards
def suit_card_combine(suits, cards):
    deck = []
    for suit in suits:
        for card in cards:
            deck.append(card + " of " + suit)
    return deck

suit_deck = suit_card_combine(suits, cards)

complete_deck = major_arcana + suit_deck

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

print(shuffle_deck(complete_deck))

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

input("Hello, are you here for a tarot card reading? Let's get started. What is your name?")
print("Ok, now I will shuffle the cards.")

shuffled_deck = shuffle_deck(complete_deck)

print("The cards are now shuffled. I will now select three cards to represent your past, present, and future.")

selected_cards = card_selector(shuffled_deck)
card_teller(selected_cards)
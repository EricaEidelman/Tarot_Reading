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

print(complete_deck)
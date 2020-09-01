import random

suits = ['Spade', 'Heart', 'Club', 'Diamond']
values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

# Example:
# >>> deck = generate_deck()
# >>> deck
# >>> [['Ace', 'Spade'], ['2', 'Spade'], ['3', 'Spade'], ...]
def generate_deck():
    deck = []
    for suit in suits:
        for value in values:
            deck.append([value, suit])
    return deck

# Example:
# >>> card = draw(deck)
# >>> card
# >>> ['Ace', 'Spade']
def draw(deck):
    card = deck[0]
    deck.remove(card)
    return card

# Example:
# >>> card = deal(deck, 2)
# >>> card
# >>> [['Ace', 'Spade'], ['2', 'Spade']]
def deal(deck, num):
    hand = []
    for i in range(num):
        hand.append(draw(deck))
    return hand

# Example:
# >>> cut(deck)
def cut_deck(deck):
    length = len(deck)
    cut_loc = random.randint(0, length-1)
    deck[:] = deck[cut_loc:] + deck[:cut_loc]

# Example:
# >>> insert(deck, ['Ace', 'Heart'])
# or
# >>> insert(deck, card)
def insert(deck, card):
    length = len(deck)
    loc = random.randint(0, length-1)
    deck[:] = deck[:loc] + [card] + deck[loc:]

def shuffle(deck):
    for i in range(100):
        cut_deck(deck)
        card = draw(deck)
        insert(deck, card)

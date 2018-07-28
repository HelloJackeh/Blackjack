from random import shuffle

class Shoe():
    """
    A shoe (sometimes referred as 'dealing shoe' or 'dealer's shoe')
    holds multiple decks of cards, ranging from 1-8 decks
    In Blackjack, not all cards get dealt so a shoe penetration (blank card) is placed
    at a point in the deck where the dealer will only deal up to that, then shoe'll be shuffled.
    """
    def __init__(self, deck_amount):
        
        self.shoe = []
        self.deck_amount = deck_amount
        self.build_shoe()
        
    def __len__(self):
        return len(self.shoe)
        
    def build_shoe(self):
        # shuffles each deck before adding it to the shoe
        for i in range(self.deck_amount):
            deck = Deck()
            deck.shuffle()
            self.shoe += deck.get_deck()
    
    def remaining(self):
        return "\n" + str(len(self.shoe)) + " cards remaining in the shoe."
            
    def shuffle(self):
        shuffle(self.shoe)
        
    def deal_card(self):
        return self.shoe.pop()
    
class Deck():
    """
    A deck HAS 52 cards, with numbered cards designating their values from 2-10,
    with face cards: 'J', 'Q', 'K' having a value of 10, and a special card 'A',
    has value of 1 or 11 depending on the player's hand.
    """
    
    def __init__(self):
        """
        unicodes for card suits
        spade - ♠ - '\u2660'
        club - ♣ - '\u2663'
        diamond - ♦ - '\u2666'
        heart - ♥ - '\u2665'
        """
        spade = "\u2660"
        club = "\u2663"
        diamond = "\u2666"
        heart = "\u2665"
        
        self.cards = []
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        
        for suits in [spade, diamond, heart, club]:
            for value in values:
                self.cards.append(Card(value, suits))
          
    def remaining(self):
        return "\n" + str(len(self.cards)) + " cards remaining in the deck."
    
    def deal_card(self):
        return self.cards.pop()
    
    def get_deck(self):
        return self.cards
    
    def shuffle(self):
        shuffle(self.cards)
        
    def show(self):
        for card in self.cards:
            print(card.show())
    
class Card():
    card_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 
                 '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
    
    def __init__(self, value, suit):
        self.name = value
        self.value = self.card_dict[value]
        self.suit = suit

    def show_card(self):
        return ("[{} {}]".format(self.suit, self.name))
        
    def show(self):
        print ("[{} {}]".format(self.suit, self.name), end = " ")
        
    def get_value(self):
        return self.value
    
    def get_suit(self):
        return self.suit
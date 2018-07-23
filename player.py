import ace

class Player():
    """
    What can a player do?
    - Can draw cards from deck
    - Can return it's name
    - Show their hand
    - Get the value of cards in their hands
    - Can track it's wins and losses (TO-DO: incorpoate this with data analysis?)
    - Possibly analyze their chances of winning (via counting cards?, possibly something on TO-DO)
    """
    def __init__(self, name):
        self._name = name
        self.hand = []
        self.a = ace.Ace()
        
        self._blackjack = False
        self.ace = False
        
        self.win_count = 0
        self.lose_count = 0
        self.tie_count = 0
        
    @property
    def name(self):
        return self._name
        
    @property
    def has_blackjack(self):
        return self._blackjack
    
    @has_blackjack.setter
    def has_blackjack(self, bj):
        if (bj is True or bj is False):
            self._blackjack = bj
        else:
            print("Can only set blackjack status to True or False")
    
    def bust(self, status):
        self.bust = status
        
    def has_ace(self):
        return self.ace
        
    def win(self):
        self.win_count += 1
        
    def lose(self):
        self.lose_count += 1
        
    def tie(self):
        self.tie_count += 1
    
    def draw(self, deck):
        """
        Each card drawn will be checked if it's an ace.
        """
        self.hand.append(deck.deal_card())
        
        self.a.check_card_drawn(self)
        self.a.check_ace(self)
        
    def last_card_drawn(self):
        return self.last_card.show_card()
    
    @property
    def last_card(self):
        return self.hand[-1]
    
    def drawn_card_value(self):
        return self.last_card.value

    def get_name(self):
        return self.name
        
    def show_hand(self):
        for card in self.hand:
            card.show()
            
    def reset_ace(self):
        self.a.reset(self)
        
    def value(self):
        value = 0
        for card in self.hand:
            value = value + card.value
        
        print("Your hand's value is: " + str(value))
        
    def get_hand_value(self):
        value = 0
        for card in self.hand:
            value += card.value
            
        return value
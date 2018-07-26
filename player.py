import ace

class Player():
    """
    What can a player do?
    - Can draw cards from deck
    - Show their hand
    - Get the value of cards in their hands
    - Can track it's wins and losses (TO-DO: incorpoate this with data analysis?)
    - Possibly analyze their chances of winning (via counting cards?, possibly something on TO-DO)
    """
    def __init__(self, name):
        self._name = name
        self.hand = []
        self.a = ace.Ace()
        self.hand_value = 0
        
        self._blackjack = False
        self.ace = False
        
        self._win = 0
        self._lose = 0
        self._tie = 0
        
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
            print("Can only set blackjack status to True or False.")
    
    def bust(self, status):
        if (status is True or status is False):
            self.bust = status
        else:
            print("bust value can only be True or False.")
        
    def has_ace(self):
        return self.ace
    
    @property
    def bankroll(self):
        return self._bankroll
    
    @bankroll.setter
    def bankroll(self, amount):
        self._bankroll = amount
    
    @property
    def win(self):
        self._win += 1
        
    @property
    def lose(self):
        self._lose += 1
        
    @property
    def tie(self):
        self._tie += 1
    
    def draw(self, deck):
        """
        Each card drawn will be checked if it's an ace.
        """
        self.hand.append(deck.deal_card())
        self.hand_value += self.drawn_card_value()
        
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
            
    def reset_hand(self):
        self.a.reset(self)
        self.hand_value = 0
        
    def value(self):
        value = 0
        for card in self.hand:
            value = value + card.value
        
        print("Your hand's value is: " + str(value))
        
    def get_hand_value(self):
        for card in self.hand:
            self.value += card.value
            
        return self.value
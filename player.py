import ace
from strategy import strategy as strat
import bankroll as br

class Player():
    """
    What can a player do?
    - Can draw cards from deck
    - Has a bankroll
    - Show their hand
    - Get the value of cards in their hands
    - Can track it's wins and losses (TO-DO: incorpoate this with data analysis?)
    - Possibly analyze their chances of winning (via counting cards?, possibly something on TO-DO)
    """
    def __init__(self, name):
        
        self._bankroll = br.Bankroll(1000)

        self.strategy = strat.Strategy(self)

        self._name = name
        self.hand = []
        self.a = ace.Ace()
        self.hand_value = 0
        
        self._blackjack = False
        self.ace = False
        self.bust = False
        
        self._win = 0
        self._lose = 0
        self._tie = 0
        
    @property
    def name(self):
        return self._name

    def is_soft(self):
        if self.hand[0] == 'A' or self.hand[1] == 'A':
            self.soft = True
        else:
            self.soft = False

    def is_split(self):
        if self.hand[0].name == self.hand[1].name:
            # Never split 5s or 10s
            if self.hand[0].value == 5 or self.hand[0].value == 10:
                self.split = False
            else:
                self.split = True
        else:
            self.split = False

    def check_initial_hand(self):
        self.has_blackjack

        if not self.has_blackjack:
            self.is_split()
            self.is_soft()

    @property
    def has_blackjack(self):
        if self.hand_value == 21:
            self.has_blackjack = True
        else:
            self.has_blackjack = False
        return self._blackjack
    
    @has_blackjack.setter
    def has_blackjack(self, bj):
        if (bj is True or bj is False):
            self._blackjack = bj
        else:
            print("Can only set blackjack status to True or False.")
        
    def has_ace(self):
        return self.ace
    
    @property
    def bankroll(self):
        return self._bankroll
    
    @bankroll.setter
    def bankroll(self, amount):
        self._bankroll = amount
        
    def bet(self, amount):
        self._bankroll.balance -= amount
    
    @property
    def win(self):
        self._win += 1
        
    @property
    def lose(self):
        self._lose += 1        

    @property
    def tie(self):
        self._tie += 1
        
    def game_record(self):
        return self._win, self._lose, self._tie
    
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
        self.bust = False
        self.a.reset(self)
        self.hand_value = 0
        
    def value(self):
        value = 0
        for card in self.hand:
            value = value + card.value
        
        print("Your hand's value is: " + str(value))

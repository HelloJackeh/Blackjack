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
        self.name = name
        self.hand = []
        self.ace = []
        
        self.blackjack = False
        self.ace = False
        
        self.strategy = None

        self.win_count = 0
        self.lose_count = 0
        self.tie_count = 0
        
        
    def has_blackjack(self):
        return self.blackjack
    
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
        self.hand.append(deck.deal_card())
        ace.check_sub_ace(self)
        ace.ace(self)
        #print("Drew {}".format(self.hand[-1].show_card()))
        
    def last_card_drawn(self):
        return self.last_card().show_card()
    
    def last_card(self):
        return self.hand[-1]
    
    def drawn_card_value(self):
        return self.last_card().value

    def get_name(self):
        return self.name
        
    def show_hand(self):
        for card in self.hand:
            card.show()

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
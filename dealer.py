from time import sleep

class Dealer():
    """
    A dealer will always play with a player(s). But should we be passing player object
    to dealer to handle interactions?
    The dealer's responsibilities?
    - Deals cards to themselves and the player(s) at the table
    - Reach soft 17 otherwise continue hitting until 17 is reached or bust
    - Analyze chances of winning via statistical and probability analysis (TO-DO)
    """
    def __init__(self, deck):
        self.game_status = True
        self.hand = []
        self.deck = deck
        
    def draw(self):
        self.hand.append(self.deck.deal_card())
        
    def drawn_card_value(self):
        # gets the recent card drawn's value
        drawn_card_val = self.hand[-1].get_value()
        return self.hand[-1].card_dict[str(drawn_card_val)]

    def show_hand(self):
        for card in self.hand:
            card.show()

    def initial_deal_cards(self):
        print("Dealing: ")
        
        for i in range(2):
            self.draw()
            
            for player in self.players:
                player.draw(self.deck)
                print("{} received {}".format(player.name, player.last_card_drawn()))
        
        print ("\n Dealer's face up card: {}".format(self.hand[0].show_card()))

    def add_players(self, players):
        # Dealer needs to know who the players are so it can interact with it
        self.players = list(players)
    
    def get_bust(self):
        return self.bust
    
    def get_hand_value(self):
        value = 0
        for c in self.hand:
            value += c.card_dict[str(c.get_value())]
            
        return value
    
    def dealer_turn(self):     
        dealer_cards = self.get_hand_value()
        self.bust = False
        
        while (dealer_cards <= 17):
            self.draw()
            dealer_cards += self.drawn_card_value()
            sleep(2) # mimics delay of actual card drawing
            print("Dealer drew: {}".format(self.hand[-1].show_card()))
            
        if dealer_cards > 21:
            self.bust = True
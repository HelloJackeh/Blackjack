import time

class Dealer():
    """
    A dealer will always play with a player(s). But should we be passing player object
    to dealer to handle interactions? ... to-do: read up more on OOP design principles
    The dealer's responsibilities?
    - Deals cards to themselves and the player(s) at the table
    - Analyze chances of winning (to-do)
    - Reach soft 17 otherwise continue hitting until 17 is reached or bust
    """
    def __init__(self, deck):
        # create dealer as a player object
        self.game_status = True
        self.hand = []
        self.shoe = deck
        
    def draw(self):
        self.hand.append(self.shoe.get_card())
        
    def initial_deal_cards(self):
        for i in range(2):
            self.draw()
        
            print("Dealing: ", end = "")
            for j in range(len(self.players)):
                self.players[j].draw(self.shoe)
                print("{}".format(self.players[j].last_card_drawn()), end = " ")
        
        print ("Dealer's face up card: {}".format(self.hand[-1].show_card()))

    # Dealer needs to know who the players are so it can interact with it
    def add_players(self, players):
        self.players = list(players)
    
    def dealer_turn(self):        
        self.dealer_bust = False
        
        while (self.dealer_cards <= 17):
            self.dealer.draw(self.deck)
            self.dealer_cards = self.dealer_cards + self.dealer.drawn_card_value()
            time.sleep(2)
            print("Dealer drew: {}".format(self.hand[-1].show_card()))
            
        if self.dealer_cards > 21:
            self.dealer_bust = True
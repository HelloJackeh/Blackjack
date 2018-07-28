from time import sleep
import player as pl

class Dealer(pl.Player):
    """
    Technically, a dealer IS a player but with extra responsibilities, it can do everything a player can do.
    The dealer's responsibilities?
    - Deals cards to themselves and the player(s) at the table
    - Reach soft 17 otherwise continue hitting until 17 is reached or bust
    - Analyze chances of winning via statistical and probability analysis (TO-DO)
    """
    def __init__(self, deck):
        super().__init__("Dealer")
        
        self.strategy = None
        self.deck = deck
        
    def add_players(self, players):
        # Dealer needs to know who the players are so it can interact with it
        self.players = players

    def deal_cards(self):
        print("\nDealing: ")

        for i in range(2):
            self.draw(self.deck)
            
            for player in self.players:
                player.draw(self.deck)
                    
        print ("Dealer's face up card: {}".format(self.hand[0].show_card()))
    
    def dealer_turn(self):
        self.bust = False
        
        # Stand on 17
        while self.hand_value < 17 and not self.has_blackjack:
            self.draw(self.deck)
            #sleep(1) # mimics delay of actual card drawing

        if self.hand_value > 21:
            self.bust = True

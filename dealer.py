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
        #self.game_status = True
        super().__init__("Dealer")
        
        self.strategy = None
        self.deck = deck
        
    def add_players(self, players):
        # Dealer needs to know who the players are so it can interact with it
        self.players = players

    def deal_cards(self):
        print("\nDealing: ")
        
        """
        On the second card dealt, check if players and/or dealer has blackjack
        """
        for i in range(2):
            self.draw(self.deck)
            
            for player in self.players:
                player.draw(self.deck)
                print("{} received {}".format(player.name, player.last_card_drawn()))
        
                if i == 1:
                    if player.get_hand_value() == 21:
                        player.has_blackjack = True
                    else:
                        player.has_blackjack = False
            
            if i == 1:
                if self.get_hand_value() == 21:
                    self.has_blackjack = True
                else:
                    self.has_blackjack = False
                    
        print ("Dealer's face up card: {}".format(self.hand[0].show_card()))
    
    def dealer_turn(self):     
        dealer_cards = self.get_hand_value()
        self.bust = None
        
        # Stand on 17
        while (self.get_hand_value() < 17):
            self.draw(self.deck)
            #dealer_cards += self.drawn_card_value()
            sleep(2) # mimics delay of actual card drawing
            print("Dealer drew: {}".format(self.last_card.show_card()))
            
        if dealer_cards > 21:
            self.bust = True
            
    
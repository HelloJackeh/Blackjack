class Ace():
    
    def __init__(self):
        # list of index of aces valued at 11 in player/dealer's hand
        self.ace_index = []

    def check_card_drawn(self, player):
        """
        Checks if player has drawn any ace cards.
        If Ace is drawn, store the indices of their Ace for easier searching
        when we need to manipulate the value of the Ace.
        """    
        if player.hand[-1].name == 'A':
            player.ace = True
            
            last_index = len(player.hand) - 1
            self.ace_index.append(last_index)

    def check_ace(self, player):
    
        player_hand = player.get_hand_value()
        
        if player_hand > 21 and player.has_ace:
            if self.ace_index:
                last_index = self.ace_index[-1]
                player.hand[last_index].value = 1
                self.ace_index.pop()                
        
    def reset(self, player):
        self.ace_index.clear()
        player.ace = False
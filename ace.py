"""
Handles changing of Ace value from being counted as 11 or 1
depending on value of player's hand
"""
class Ace():
    def __init__(self):
        # store index of aces valued at 11 in player/dealer's hand
        self.ace_index = []

    def check_card_drawn(self, player):
        """
        Checks if player has drawn any ace cards.
        If Ace is drawn, store the indices of their Ace (valued at 11) for easier searching
        when we need to manipulate the value of the Ace to 1.
        """    
        if player.hand[-1].name == 'A':
            player.ace = True
            
            last_index = len(player.hand) - 1
            self.ace_index.append(last_index)

    def check_ace(self, player):
    
        player_hand = player.get_hand_value()
                
        if player_hand > 21 and player.has_ace:
            """
            If there are no Aces valued at 11 stored in 'ace_index', 
            don't need to set ace value to 1, instead set player.ace to False indicating
            player does not have anymore aces valued at 11
            """
            if self.ace_index:
                index_of_ace = self.ace_index[-1]
                player.hand[index_of_ace].value = 1
                self.ace_index.pop()
            else:
                player.ace = False                
    
    def reset(self, player):
        self.ace_index.clear()
        player.ace = False
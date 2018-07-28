class Ace():
    def __init__(self):
        # store aces in player/dealer's hand
        self.aces = []

    def check_card_drawn(self, player):
        if player.last_card.name == 'A':
            player.ace = True
            self.aces.append(player.last_card)
        
    def check_ace(self, player):
    
        player_hand = player.hand_value
                
        if player_hand > 21 and player.has_ace:
            """
            Reduce player's hand value by 10 if their hand exceeds 21 if they hold an ace,
            this effectively reduces the ace's value from 11 to 1.
            """
            if self.aces:
                player.hand_value -= 10
                self.aces.pop()
            else:
                player.ace = False                
    
    def reset(self, player):
        self.aces.clear()
        player.ace = False
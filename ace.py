"""
If a player or dealer has a natural/blackjack, this 'ace check' isn't executed.
These helper functions only look at aces drawn beyond the initial two cards 
and will modify the value of an Ace as value of 1 or 11, depending on the user's hand value.
"""

# list of index of aces valued at 11 in player/dealer's hand
ace_index = []

def check_initial_ace(player):
    # this is only called during the initial card dealing phase
    reset(player)
    for i in range(2):
        card = player.hand[i].name
        if card == 'A':
            player.ace = True
            ace_index.append(i)
            
def check_sub_ace(player):
    """
    Checks if player has drawn aces beyond their initial 2 cards.
    If Ace is drawn, store the indices of their Ace for easier searching
    when we need to manipulate the value of the Ace.
    """
    last_index = len(player.hand) - 1
    
    if player.hand[-1].name == 'A':
        player.ace = True
        ace_index.append(last_index)

def ace(player):
    
    player_hand = player.get_hand_value()
        
    if player_hand > 21 and player.has_ace:
        if ace_index:
            last_index = ace_index[-1]
            player.hand[last_index].value = 1
            ace_index.pop()
        
def reset(player):
    ace_index.clear()
    player.ace = False
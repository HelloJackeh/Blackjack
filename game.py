import shoe as sh
import dealer as dl
import player as p

class Game():
    """
    - Handles the logic required in a typical casino-style BlackJack game:
        - Deals cards to players (Max player is 6)
        - Determine the winner at end of round, restart round 
        - Keep track of how many cards are in the shoe
        - Ensures the dealer knows who it's (players) playing with
    """
    
    def __init__(self, players, deck_amount, pen_amount):
        """
        - Pass how many decks will be in the shoe.
        - Ensure dealer knows how many players are playing via 'confirm_player'
        """
        # Players who haven't bust are placed in this list so when round is over
        # dealer will compare cards with players in this list
        self.active_players = []
        
        self.decks = sh.Shoe(deck_amount)
        self.decks.shuffle()
        self.dealer = dl.Dealer(self.decks)
        
        # create copy of the deck to keep track of the length
        self.clone = self.decks.shoe.copy()
        
        # Holds cards cleared at the end of each round
        self.trash_pile = []
        
        self.players = players
        self.confirm_players(self.players)

        # Average shoe penetration in Blackjack is usually 25% (0.25)
        self.pen = len(self.decks) * (pen_amount / 100)
        print ("{} cards are in the shoe after cut.".format(self.remaining_cards()))
        
        self.greet_message()
        
    def confirm_players(self, players):
        self.dealer.add_players(players)
        
    def remaining_cards(self):
        return int(len(self.decks) - self.pen)
        
    def greet_message(self):
        for player in self.players:
            print("Welcome player " + player.get_name())
            
    def shoe_count(self):
        return len(self.decks) - self.pen
        
    def get_current_players(self):
        for pl in self.players:
            print(pl.get_name())
            
    def get_num_of_players(self):
        for count in range(len(self.players)):
            count += 1
            
        print("Number of players: " + str(count))

    def clear_cards(self):
        # Discard cards from dealer and players at end of the round
        self.dealer.hand.clear()
        
        for player in self.players:
            player.hand.clear()
    
    def reset(self):
        self.active_players.clear()
    
    def not_out(self, player):
        self.active_players.append(player)
        
    
    def decide_winner(self):
        dealer_hand = self.dealer.get_hand_value()
        
        # If active_players list has no players, everyone has busted.
        if self.active_players:
            for player in self.active_players:
                
                player_hand = player.get_hand_value()
                
                if self.dealer.bust or player_hand > dealer_hand:
                    player.win()
                    print("{} wins with {} in their hand.".format(player.name, player_hand))
                elif player_hand < dealer_hand:
                    player.lose()
                    print("{} loses with {} in their hand.".format(player.name, player_hand))
                else:
                    player.tie()
                    print("{} ties with {} in their hand.".format(player.name, player_hand))
        else:
            print("Everyone busted.")
        
    def start_game(self):
        self.dealer.initial_deal_cards()
        card_value = 0
        
        for player in self.players: 
            player_choice = None
            
            if player.has_blackjack():
                self.not_out(player)
                continue
            
            print("\n\n{}'s turn.".format(player.name))
            player.show_hand()
            
            while (player_choice != "stay"):
                player_choice = input("Type 'hit' (to draw), 'stay' (to stay), 'value' (calculate card value in hand). ")
                
                if player_choice == "hit":
                    player.draw(self.decks)
                    
                    card_value = player.get_hand_value()

                    print("Drew {}".format(player.last_card_drawn()))
                    print("Your hand's value is {}".format(card_value))
                    
                    bj = 21 - card_value
                    
                    if card_value < 21:
                        print ("You need {} for blackjack".format(bj))
                    elif card_value == 21:
                        self.not_out(player)
                        player.show_hand()
                        player_choice = "stay"
                    else:
                        print("You busted.")
                        player.lose()
                        player_choice = "stay"
                        
                elif player_choice == "stay":
                    self.not_out(player)
                    player.show_hand()
                elif player_choice == "value":
                    player.value()
                elif player_choice == "show":
                    player.show_hand()
                else:
                    print("Please only type 'hit', 'stay', or 'value'.")
        print("")
        self.dealer.dealer_turn()
        self.dealer.show_hand()
        
        print("\nDealer's hand count: {}".format(self.dealer.get_hand_value()))
        # print("{}'s hand count: {}".format(self.players[0].get_name(), card_value))
        
        self.decide_winner()            
        self.clear_cards()
        self.reset()
        
        print("\n{} cards remaining in the shoe.".format(self.remaining_cards()))
            
if __name__ == '__main__':                
    p1 = p.Player("bob")
    p2 = p.Player("joe")
    list_player = [p1, p2]
    g = Game(list_player, 6, 25)
    #g.get_current_players()
    #g.get_num_of_players()
    g.start_game()
    
    while(input("play again? n to exit. ") != "n"):
        g.start_game()
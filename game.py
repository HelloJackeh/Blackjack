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
        
        TODO:
        - Implement function to check if player has BlackJack (natural) in first 2 cards
        - For those players who has blackjack, or has not busted at end of round,
        place them in another list so dealer doesn't have to check cards of players who busted
    """
    
    def __init__(self, players, deck_amount):
        """
        - Initialize how many decks will be in the shoe.
        - Ensure dealer knows how many players are playing via 'confirm_player'
        """
        self.active_play = []
        
        self.decks = sh.Shoe(deck_amount)
        self.shuffle_shoe()
        self.dealer = dl.Dealer(self.decks)
        
        self.players = list(players)
        self.confirm_players(self.players)
        
        self.greet_message()
        
    def confirm_players(self, players):
        self.dealer.add_players(players)
        
    def greet_message(self):
        for player in self.players:
            print("Welcome player " + player.get_name())
        
    def get_current_players(self):
        for pl in self.players:
            print(pl.get_name())
            
    def get_num_of_players(self):
        for count in range(len(self.players)):
            count = count + 1
            
        print("Number of players: " + str(count))

    def clear_cards(self):
        # Discard cards from dealer and players at end of the round
        self.dealer.hand.clear()
        
        for player in self.players:
            player.hand.clear()
        
    def shuffle_shoe(self):
        self.decks.shuffle()
        
    def check_blackjack(self, player):
        
        if player.get_value() == 21:
            self.not_out(player)
            return True
            
    def get_dealer_hand(self):
        return self.dealer.get_hand_value()
    
    def reset(self):
        self.active_play.clear()
    
    def not_out(self, player):
        self.active_play.append(player)
    
    def decide_winner(self):
        dealer_hand = self.dealer.get_hand_value()
        
        if self.active_play:
            for player in self.active_play:
                player_hand = player.get_value()
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
            
            if self.check_blackjack(player):
                continue
            
            print("\n\n {}'s turn.".format(player.name))
            player.show_hand()
            
            while (player_choice != "stay"):
                card_value = player.get_value()
                player_choice = input("Type 'hit' (to draw), 'stay' (to stay), 'value' (calculate card value in hand). ")
                
                if player_choice == "hit":
                    player.draw(self.decks)
                    card_value = player.get_value()

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
                        player.bust(True)
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
        
        print("\nDealer's hand count: {}".format(self.get_dealer_hand()))
        # print("{}'s hand count: {}".format(self.players[0].get_name(), card_value))
        
        self.decide_winner()            
        self.clear_cards()
        self.reset()
        
        print(self.decks.remaining())
            
if __name__ == '__main__':                
    p1 = p.Player("bob")
    p2 = p.Player("joe")
    list_player = [p1, p2]
    g = Game(list_player, 4)
    #g.get_current_players()
    #g.get_num_of_players()
    g.start_game()
    
    while(input("play again? n to exit. ") != "n"):
        g.start_game()
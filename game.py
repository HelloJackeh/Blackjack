import shoe as sh
import dealer as deal

class Game():
    """
    Imagine this as the controller in a MVC pattern.
    Initializes the shoe, players, and dealer
    """
    
    def __init__(self, players):
        self.decks = sh.Shoe(4)
        self.shuffle_shoe()
        self.dealer = deal.Dealer(self.decks)
        self.players = list(players)
        self.confirm_players(self.players)
        
        self.greet_message()
        
    def confirm_players(self, players):
        self.dealer.add_players(players)
        
    def greet_message(self):
        for i in range(len(self.players)):
            print("Welcome player " + self.players[i].get_name())
        
    def get_current_players(self):
        for p in self.players:
            print(p.get_name())
            
    def get_num_of_players(self):
        for count in range(len(self.players)):
            count = count + 1
            
        print("Number of players: " + str(count))
            
    #def shuffle_deck(self):
        #self.deck.shuffle()
        
    def shuffle_shoe(self):
        self.decks.shuffle()
        
    def blackjack_count(self, card_value):
        blackjack = 21
        return blackjack - card_value
            
    def get_dealer_hand(self):
        return self.dealer_cards
            
    def start_game(self):
        self.dealer.initial_deal_cards()
        card_value = 0
        
        for i in range(len(self.players)): 
            player_choice = None
            print("\n" + self.players[i].get_name() + "'s turn.")
            
            while (player_choice != "stay"):
                card_value = self.players[i].get_value()
                player_choice = input("Type 'hit' (to draw), 'stay' (to stay), 'value' (calculate card value in hand). ")
                
                if player_choice == "hit":
                    self.players[i].draw(self.decks)
                    card_value = self.players[i].get_value()
                    blackjack = 21

                    print("Drew {}".format(self.players[i].last_card_drawn()))
                    print("Your hand's value is {}".format(card_value))
                    
                    if card_value <= blackjack:
                        print ("You need {} for blackjack".format(self.blackjack_count(card_value)))
                    else:
                        print("You busted.")
                        player_choice = "stay"
                        
                elif player_choice == "stay":
                    self.players[i].show_hand()
                elif player_choice == "value":
                    self.players[i].value()
                elif player_choice == "show":
                    self.players[i].show_hand()
                else:
                    print("Please only type 'hit', 'stay', or 'value'.")
        
        print("\n")
        self.dealer_turn()
        
        print("Dealer's hand count: {}".format(self.get_dealer_hand()))
        print("{}'s hand count: {}".format(self.players[0].get_name(), card_value))
        
        if self.dealer_cards >= card_value:
            print("dealer wins.")
        elif self.dealer_bust == True or self.dealer_cards < card_value:
            print(self.players[0].get_name() + " wins.")
        
        #print(self.deck.remaining())
            
if __name__ == '__main__':                
    p1 = Player("bob")
    list_player = [p1]
    g = Game(list_player)
    #g.get_current_players()
    #g.get_num_of_players()
    g.start_game()
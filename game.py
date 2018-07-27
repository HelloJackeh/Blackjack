import shoe as sh
import dealer as dl
import player as pl

class Game():
    """
    - Handles the logic required in a typical casino-style BlackJack game:
        - Deals cards to players (Max player is 6)
        - Determine the winner at end of round, restart round 
        - Keep track of how many cards are in the shoe
        - Ensures the dealer knows who it's (players) playing with
        - Pay out bets
    """
    
    def __init__(self, players, deck_amount, pen_amount):
        """
        - Pass how many decks will be in the shoe.
        - Ensure dealer knows how many players are playing via 'confirm_player'
        """
        self.decks = sh.Shoe(deck_amount)
        self.decks.shuffle()
        
        self.dealer = dl.Dealer(self.decks)
        
        self.players = players
        self.confirm_players(self.players)
        
        # Holds cards cleared at the end of each round
        self.trash_pile = []

        # Average shoe penetration in Blackjack is usually 25% (0.25)
        self.pen = len(self.decks) * (pen_amount / 100)
        print ("{} cards are in the shoe after cut.".format(self.remaining_cards()))
        
        self.greet_message()
        
    def confirm_players(self, players):
        self.dealer.add_players(players)

    #def shuffle_shoe(self):
        
    
    """
    Build shoe either with new decks or append the trash pile and shuffle
    """
    #def shuffle_shoe(self):
        
    def remaining_cards(self):
        return int(len(self.decks) - self.pen)
    
    def payroll_amount(self, amount):
        for player in self.players:
            player.bankroll = amount
        
    def greet_message(self):
        for player in self.players:
            print("Welcome player " + player.name)
            
    def shoe_count(self):
        return len(self.decks) - self.pen
        
    def get_current_players(self):
        for player in self.players:
            print(player.get_name())
            
    def get_num_of_players(self):
        for count in range(len(self.players)):
            count += 1
            
        print("Number of players: " + str(count))
        
    def clear_cards(self, player):
        for i in range(len(player.hand)):
            self.trash_pile.append(player.hand.pop())

        for cards in player.hand:
            self.trash_pile.append(cards.pop())
    
    def reset(self):
        # handles clean up of player cards and removal of players in active_players list
        self.active_players.clear()
        
        # Discard cards from dealer and players at end of the round into trash_pile
        self.clear_cards(self.dealer)
        self.dealer.reset_hand()
        
        for player in self.players:
            self.clear_cards(player)
            player.reset_hand()
    
    def not_out(self, player):
        self.active_players.append(player)
        
    def decide_winner(self):
        dealer_hand = self.dealer.hand_value
        
        # If active_players list has no players, everyone has busted.
        if self.active_players:
            for player in self.active_players:
                
                player_hand = player.hand_value
                
                if self.dealer.bust or player_hand > dealer_hand:
                    player.win
                    print("{} wins with {} in their hand.".format(player.name, player_hand))
                elif player_hand < dealer_hand:
                    player.lose
                    print("{} loses with {} in their hand.".format(player.name, player_hand))
                else:
                    player.tie
                    print("{} ties with {} in their hand.".format(player.name, player_hand))
                    
                win, loss, tie = player.game_record()
                print("Record - W/L/T: {} {} {}".format(win, loss, tie))
        else:
            print("Everyone busted.")

    def decision_round(self):
        self.dealer.deal_cards()

        self.active_players = []
        
        dealer_card = self.dealer.hand[0].name
        
        if dealer_card == 'J' or dealer_card == 'Q' or dealer_card == 'K':
            dealer_face_up_card = str(self.dealer.hand[0].value)
        else:
            dealer_face_up_card = str(self.dealer.hand[0].name)
        
        for player in self.players:
            player.check_initial_hand()
            decision = None

            if player.has_blackjack:
                self.not_out(player)
                continue

            while not player.bust:
                if player.soft:
                    decision = player.strategy.soft_hand[player.hand_value][dealer_face_up_card]
                elif player.split:
                    decision = player.strategy.split_hand[player.hand[0].value][dealer_face_up_card]
                else:
                    decision = player.strategy.hard_hand[player.hand_value][dealer_face_up_card]

                if decision == 'H':
                    player.draw(self.decks)
                    print("{} chose to hit.".format(player.name))
                elif decision == 'S':
                    break
                elif decision == 'Dh' or decision == 'Ds':
                    #player.bet(2*betamount)
                    player.draw(self.decks)
                    print("suppose to double")
                elif decision == 'P':
                    #player.split_cards()
                    print("split here")
                    break
                elif decision == 'Rh':
                    #player.surrender()
                    # return half of player bet
                    print("surrender if applicable")
                    break
                elif decision == 'Ph':
                    #We treat this as a hit instead of doubling after splitting for now
                    player.draw(self.decks)
                    print("draw")
                    
                if player.hand_value > 21:
                    player.bust = True
                    player.lose
                    break
                elif player.hand_value == 21:
                    break
                    
            if not player.bust:
                self.active_players.append(player)
            else:
                print("{} busted.".format(player.name))

        print("")
        self.dealer.dealer_turn()
        self.dealer.show_hand()

        print("\nDealer's hand count: {}".format(self.dealer.hand_value))
        # print("{}'s hand count: {}".format(self.players[0].get_name(), card_value))

        self.decide_winner()
        print("\n{} cards remaining in the shoe.".format(self.remaining_cards()))

        self.reset()

        
    def start_game(self):
        # Players who haven't bust are placed in this list so when round is over
        # dealer will compare cards with players in this list
        self.active_players = []
        
        self.dealer.deal_cards()
        
        for player in self.players: 
            player_choice = None

            if player.has_blackjack:
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
        self.reset()
        
        print("\n{} cards remaining in the shoe.".format(self.remaining_cards()))
        
    def post_round(self):
        if self.remaining_cards() < 0:
            self.shuffle_shoe()
      
def main():
    decks = 8
    shoe_penetration = 25 # 25%
    
    list_of_players = []
    name = "Player "

    for i in range(1, 7):
        list_of_players.append(pl.Player(name + str(i)))
        
    g = Game(list_of_players, decks, shoe_penetration)
    g.payroll_amount(300)
    g.decision_round()
    
    while(input("play again? n to exit. ") != "n"):
        g.decision_round()
        
if __name__ == '__main__':                
    main()
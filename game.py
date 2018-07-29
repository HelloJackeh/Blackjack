import shoe as sh
import dealer as dl
import player as pl
from time import sleep

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
        self.set_deck_threshold()

        self.players = players
        self.confirm_players(self.players)
        
        # Holds cards cleared at the end of each round
        self.trash_pile = []

        # Average shoe penetration in Blackjack is usually 25% (0.25)
        self.pen = len(self.decks) * (pen_amount / 100)
                
    def confirm_players(self, players):
        self.dealer.add_players(players)
        
    def set_deck_threshold(self):
        """
        If there are 6 players, when there are less than 30 cards before the next round, shoe is reshuffled
        """
        self.deck_threshold = 6 * 5
        #self.deck_threshold = self.get_num_of_players() * 5
    
    def shuffle_shoe(self):
        self.decks.shoe += self.trash_pile
        self.trash_pile.clear()
        self.decks.shuffle()
        #sleep(3)
        
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
            print(player.name)
            
    def get_num_of_players(self):
        count = 0
        for player in self.players:
            count += 1
            
        return count
        
    def clear_cards(self, player):
        for i in range(len(player.hand)):
            self.trash_pile.append(player.hand.pop())
                
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
        for player in self.players:                
            player_hand = player.hand_value
            
            win, loss, tie = player.game_record()
                
            if player.bust:
                player.lose
                print("{} loses with {} in their hand.".format(player.name, player_hand))
            elif self.dealer.bust or player_hand > dealer_hand:
                player.win
                print("{} wins with {} in their hand.".format(player.name, player_hand))
            elif player_hand < dealer_hand:
                player.lose
                print("{} loses with {} in their hand.".format(player.name, player_hand))
            else:
                player.tie
                print("{} ties with {} in their hand.".format(player.name, player_hand))
                    
            print("Record - W/L/T: {} {} {}".format(win, loss, tie))

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
                elif decision == 'S':
                    break
                elif decision == 'Dh' or decision == 'Ds':
                    #player.bet(2*betamount)
                    player.draw(self.decks)
                    print("suppose to double")
                elif decision == 'P':
                    #player.split_cards()
                    break
                elif decision == 'Rh':
                    #player.surrender()
                    # return half of player bet
                    break
                elif decision == 'Ph':
                    #We treat this as a hit instead of doubling after splitting for now
                    player.draw(self.decks)
                    
                if player.hand_value > 21:
                    player.bust = True
                    break
                elif player.hand_value == 21:
                    break

        print("")
        self.dealer.dealer_turn()
        self.dealer.show_hand()

        print("\nDealer's hand count: {}".format(self.dealer.hand_value))
        # print("{}'s hand count: {}".format(self.players[0].get_name(), card_value))

        self.decide_winner()
        print("\n{} cards remaining in the shoe.".format(self.remaining_cards()))

        self.reset()
        
        if self.remaining_cards() < self.deck_threshold:
            self.shuffle_shoe()
        
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
    
    rounds = 0
    
    while(rounds < 10000):
        g.decision_round()
        rounds += 1
        
if __name__ == '__main__':                
    main()
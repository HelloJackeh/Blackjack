#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 21:39:42 2018
"""
import time
import shoe
from player import Player

class Game():
    
    def __init__(self, players):
        self.players = list(players)
        
        self.deck = shoe.Deck()
        self.shuffle_deck()
        
        self.dealer = Player("Dealer")
        self.dealer_cards = 0
        
        self.greet_message()
        self.deal_cards()
        
    def deal_cards(self):
        
        for x in range(2):
            self.dealer.draw(self.deck)
            
        print ("Dealer's face up card: {}".format(self.dealer.last_card_drawn()))
        
        for i in range(2):
            print("Dealing: ", end = "")
            for j in range(len(self.players)):
                self.players[j].draw(self.deck)
                print("{}".format(self.players[j].last_card_drawn()), end = " ")
        
    def greet_message(self):
        for i in range(len(self.players)):
            print("Welcome player " + self.players[i].get_name())
        
    def get_current_players(self):
        for player in self.players:
            print(player.get_name())
            
    def get_num_of_players(self):
        for count in range(len(self.players)):
            count = count + 1
            
        print("Number of players: " + str(count))
            
    def shuffle_deck(self):
        self.deck.shuffle()
        
    def blackjack_count(self, card_value):
        blackjack = 21
        return blackjack - card_value
    
    def dealer_turn(self):        
        self.dealer_bust = False
        
        while (self.dealer_cards <= 17):
            self.dealer.draw(self.deck)
            self.dealer_cards = self.dealer_cards + self.dealer.drawn_card_value()
            time.sleep(2)
            print("Dealer drew: {}".format(self.dealer.last_card_drawn()))
            
        if self.dealer_cards > 21:
            self.dealer_bust = True
            
    def get_dealer_hand(self):
        return self.dealer_cards
            
    def start_game(self):
        card_value = 0
        
        for i in range(len(self.players)): 
            player_choice = None
            print("\n" + self.players[i].get_name() + "'s turn.")
            
            while (player_choice != "stay"):
                card_value = self.players[i].get_value()
                player_choice = input("Type 'hit' (to draw), 'stay' (to stay), 'value' (calculate card value in hand). ")
                
                if player_choice == "hit":
                    self.players[i].draw(self.deck)
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
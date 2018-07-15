#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 21:39:42 2018
"""

import random

class Card():
    
    card_dict = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, 
                 '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 
                 'J': 10, 'Q': 10, 'K': 10}
    
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def show_card(self):
        return ("{} {}".format(self.suit, self.value))
        
    def show(self):
        #print("[" + str(self.suit) + " " + str(self.value) + "]", end = " ")
        print ("[ {} {} ]".format(self.suit, self.value), end = " ")
        
    def get_value(self):
        return self.value
    
    def get_suit(self):
        return self.suit
        
class Deck():
    
    def __init__(self):
        """
        utf-8 codes for card suits
        spade - ♠ - '\u2660'
        club - ♣ - '\u2663'
        diamond - ♦ - '\u2666'
        heart - ♥ - '\u2665'
        """
        spade = "\u2660"
        club = "\u2663"
        diamond = "\u2666"
        heart = "\u2665"
        
        self.cards = []
        values = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        
        for suits in [spade, diamond, heart, club]:
            for value in values:
                self.cards.append(Card(value, suits))
          
    def remaining(self):
        return "\n" + str(len(self.cards)) + " cards remaining in the deck."
        
    def give_card(self):
        return self.cards.pop()
    
    def shuffle(self):
        random.shuffle(self.cards)
        
    def show(self):
        for card in self.cards:
            print(card.show())

        
class Player():  
    
    def __init__(self, name):
        self.name = name
        self.hand = []
        print("Welcome player {}".format(self.name))
        
    def draw(self, deck):
        self.hand.append(deck.give_card())
        print("Drew {}".format(self.hand[-1].show_card()))

    def get_name(self):
        return self.name
        
    def show_hand(self):
        for card in self.hand:
            card.show()

    def value(self):
        value = 0
        for c in self.hand:
            value = value + c.card_dict[str(c.get_value())]
        
        print("Your hand's value is: " + str(value))
        
    def get_value(self):
        value = 0
        for c in self.hand:
            value = value + c.card_dict[str(c.get_value())]
            
        return value

class Game():
    
    def __init__(self, players, deck):
        self.players = list(players)
        self.deck = deck
        self.shuffle_deck()
        
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
            
    def start_game(self):
        while (input("go or end? ") != "end"):
            
            for i in range(len(self.players)): 
                player_choice = None
                print(self.players[i].get_name() + "'s turn.")
                
                while (player_choice != "stay"):   
                    
                    player_choice = input("Type 'hit' (to draw), 'stay' (to stay), 'value' (calculate card value in hand). ")
                    
                    if player_choice == "hit":
                        self.players[i].draw(self.deck)
                        card_value = self.players[i].get_value()
                        blackjack = 21

                        print("Your hand's value is " + str(card_value))
                        
                        if card_value <= blackjack:
                            print ("You need " + str(self.blackjack_count(card_value)) + " for blackjack")
                        else:
                            print("You busted.")
                            player_choice = "stay"
                    elif player_choice == "stay":
                        self.players[i].show_hand()
                    elif player_choice == "value":
                        self.players[i].value()   
                    else:
                        print("Please only type 'hit', 'stay', or 'value'.")
                
            print(self.deck.remaining())
            
                
p1 = Player("bob")
p2 = Player("dealer")
p3 = Player("ko")
list_player = [p1, p2, p3]
d = Deck()
g = Game(list_player, d)
#g.get_current_players()
#g.get_num_of_players()
g.start_game()
    
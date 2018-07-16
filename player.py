#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 16:22:45 2018

@author: jackeh
"""

class Player():
    """
    What can a player do?
    - Can draw cards from deck
    - Can return it's name
    - Show their hand
    - Get the value of cards in their hands
    """
    def __init__(self, name):
        self.name = name
        self.hand = []
        
    def draw(self, deck):
        self.hand.append(deck.give_card())
        #print("Drew {}".format(self.hand[-1].show_card()))
        
    def last_card_drawn(self):
        return self.hand[-1].show_card()
    
    def last_card(self):
        return self.hand[-1]
    
    def drawn_card_value(self):
        return self.last_card().card_dict[str(self.hand[-1].get_value())]

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
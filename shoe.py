#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 16:15:17 2018

A shoe (sometimes referred as dealing shoe or dealer's shoe)
holds multiple decks of cards (from 2-8 decks)
"""

import random

class Card():
    # TO-DO: Modify 'A' - Ace to interchange between value of '1' or '11' if the player wants their A to be 1 or 11.
    card_dict = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 
                 'J': 10, 'Q': 10, 'K': 10}
    
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def show_card(self):
        return ("[{} {}]".format(self.suit, self.value))
        
    def show(self):
        print ("[{} {}]".format(self.suit, self.value), end = " ")
        
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
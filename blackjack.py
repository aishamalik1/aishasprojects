#/usr/bin/python
# -*- coding: utf-8 -*-
"""
author: Aisha Malik

Blackjack game
"""

import random

class Card(object):  
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "{}{}".format(self.suit, self.rank)

    def value(self, total):
        cval = 0
        if type(self.rank) == int:
            cval = self.rank
        if self.rank == 'J' or self.rank == 'Q' or self.rank == 'K':
            cval = 10
        if self.rank == 'A':
            if total + 11 > 21: 
                cval = 1
            else:
                cval = 11
        return cval

def make_deck():
    listy = []
    suits = ['♠','♣','♦','♥']
    for i in suits:
        for j in range(2,11):
            newcard = Card(i, j)
            listy.append(newcard)
        listy.append(Card(i, 'A'))
        listy.append(Card(i, 'J'))
        listy.append(Card(i, 'Q'))
        listy.append(Card(i, 'K'))
    
    random.shuffle(listy)
    return listy
    
make_deck()
def main():
    deck = make_deck()
    ptotal = 0 #player total
    dtotal = 0 #dealer total
    playersturn = True
    while ptotal < 21 and playersturn:
        pcard = deck[0] #pcard = player card
        ptotal += pcard.value(ptotal)
        print("You drew {}".format(pcard))
        print("Your sum: {}".format(ptotal))
        
        if ptotal == 21:
            print("Yay! You're total is 21. You win! :)")
        elif ptotal > 21:
            print("Sorry, you lose. Your sum is greater than 21. :(")
        else:
            player = input("Would you like to draw another card? (y/n) ")
            if player.lower() == 'n':
                playersturn = False
        deck = deck[1:]
    
    if ptotal < 21 and playersturn == False:
        print("Now it's my turn.")
        while dtotal < 17:
            dcard = deck[0]
            dtotal += dcard.value(dtotal)
            print("I drew {}".format(dcard))
            print("My sum: {}".format(dtotal))
            
            deck = deck[1:]
        
        if dtotal == 21:
            print("I won! My sum is 21! Take that!")
        elif dtotal > 21:
            print("I guess you win. My total is greater than 21 :(")
        elif dtotal == player:
            print("The game is a push. It's a draw.")
        else:
            if dtotal > ptotal:
                print("I win because my total is greater than yours! Huzzah!")
            else:
                print("You win! Congratulations!")
                                

if __name__ == "__main__":
    main()

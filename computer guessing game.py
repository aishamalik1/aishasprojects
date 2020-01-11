#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 00:24:13 2019

@author: aishamalik
Computer guessing game
"""

low = 1
high = 10
attempts = 0

while attempts <3:
    mid = (low+high)//2
    print("I guess", + mid)
    user_hint = int(input("Is my guess 1) too big, 2) too small or 3) correct?: "))
    
    if user_hint == 3:
        print ("Yay! I'm amazing!")
        break
    elif user_hint == 2:
        low = mid +1
        attempts += 1
    elif user_hint == 1:
        high = mid - 1
        attempts += 1
else:
    print ("Oh no, I've run out of turns :( .")
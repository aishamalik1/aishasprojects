#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 22:39:04 2019

@author: aishamalik
#the guessing game
"""

import random


c_guess = random.randint(1,10)

attempts = 0

while attempts < 5:
    x = int(input("Guess a number between 1 and 10: "))
    if abs(x-c_guess) >5:
        print ("Not even close :(" ) #if the difference in the input and guess is bigger than 5
        attempts += 1
    elif abs (x-c_guess) >= 3 and abs(x-c_guess) <= 5: # if the diff is b/w 3 and 5
        print ("Close.")
        attempts += 1
    elif abs(x-c_guess) <5 and abs(x-c_guess) >= 1:
        print ("Almost there!")
        attempts +=1
    elif c_guess == x:
        print("Wow, you guessed my mind! Congrats!")
        break
else:
    print ("You weren't able to figure it out and have run out of tries. Better luck next time!")
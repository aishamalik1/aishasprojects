#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 10:35:00 2019

@author: aishamalik

#Translates words to piglatin
"""

def piggify(word):
    wordlist = []
    consonants = []
    wordlist.append(word)
    vowels = 'aeiou'
    l = len(word)-1
    
    if word[0] in vowels:
            wordlist.append("yay")
            pigl = wordlist[0] + wordlist[1]
            print(word, "in piglatin is", pigl)
    else:
        i = 0
        while i <= l and word[i] not in vowels:
            fl = word[i] #first letter
            consonants.append(fl)
            x = "".join(consonants)
            i+=1
        leftover = word[i:]
        piglc = leftover + x + "ay"
        print(word,"in piglatin is",piglc)
    
word = input("What word(s) would you like translated into pig latin? Type the last word with a period to stop. ")

for i in word:
    if "." not in word:
        piggify(word)
        word = input("What word(s) would you like translated into pig latin? Type the last word with a period to stop. ")
        continue

else:
    newword = word.replace(".","")
    piggify(newword)
    
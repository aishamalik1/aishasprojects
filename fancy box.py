#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 21:12:30 2019

@author: aishamalik
#prints out text in a fancy box
#am5080
"""

def print_box():
    linebreak = ' l '

    if linebreak in s:
        i=0
        x = s.split(' l ')
        maximumlength = max(x, key=len)
        list_length = len(x)
        l = len(maximumlength)
        i_total = list_length-1
        indiv =[]
        while i <= i_total:
            elem = x[i]
            sp = len(elem)
            topline = '*'*(l+4)
            m = (l-sp)//2 + 1
            if l%2 == 0:
                if sp%2 == 0:
                    indiv.append(" "*m + x[i] + " "*(m) + '*')
                else:
                    indiv.append(" "*m + x[i] + " "*(m+1) + '*')
            else:
                if sp%2 != 0:
                    indiv.append(" "*m + x[i] + " "*(m) + '*')
                else:
                    indiv.append(" "*m + x[i] + " "*(m+1) + '*')
            i+=1
        box = topline + '\n*' + "\n*".join(indiv) + ' \n' + topline
        print(box)
    
    else:
        line1 = "*"*(len(s) + 4)
        line2 = '* ' + s + ' *'
        space = "\n"
        y = (line1 + space + line2 + space + line1)
        print(y)

s = input(str("What would you like printed out fancy? (For multiline output, write input with the string \' L \' between linebreaks). "))
print_box()

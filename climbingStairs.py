#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 19:48:40 2020

@author: aishamalik

Prompt:
    You are climbing a staircase that has n steps.
    You can take the steps either 1 or 2 at a time. 
    Calculate how many distinct ways you can climb to the top of the staircase.
"""

def climbingStairs(n):
    if n == 1:
        return 1
    i, j = 1, 0
    for k in range(n):
        i, j = i+j, i
    return i
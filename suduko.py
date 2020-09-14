#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 19:55:38 2020
Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid 
with numbers in such a way that each column, each row, and each of the nine
 3 × 3 sub-grids that compose the grid all contain all of the numbers from 
 1 to 9 one time.

Implement an algorithm that will check whether the given grid of numbers
 represents a valid Sudoku puzzle according to the layout rules described
 above. Note that the puzzle represented by grid does not have to be solvable.
@author: aishamalik
"""

def repeat(line):
    s = set()
    for t in line:
        if t == '.':
            continue
        if t in s:
            return False
        s.add(t)
    return True

def sudoku2(grid):
    #check rows, columns and 3x3 grids
    for row in grid:
        if not repeat(row):
            return False
    for i in range(9):
        if not repeat([row[i] for row in grid]):
            return False
    for i in range(0,9,3):
        for j in range(0,9,3):
            if not repeat(grid[i][j:j+3]+ grid[i+1][j:j+3]+grid[i+2][j:j+3]):
                return False
    return True
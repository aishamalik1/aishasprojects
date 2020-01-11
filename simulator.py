"""
Author: Aisha Malik

"""


import random
import math
from matplotlib import pyplot as plt
import numpy as np


def normpdf(x, mean, sd):
    """
    Return the value of the normal distribution 
    with the specified mean and standard deviation (sd) at
    position x.
    You do not have to understand how this function works exactly. 
    """
    var = float(sd)**2
    denom = (2*math.pi*var)**.5
    num = math.exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom

def pdeath(x, mean, sd):
    start = x-0.5
    end = x+0.5
    step =0.01    
    integral = 0.0
    while start<=end:
        integral += step * (normpdf(start,mean,sd) + normpdf(start+step,mean,sd)) / 2
        start += step            
    return integral    
    
recovery_time = 4 # recovery time in time-steps
virality = 0.2    # probability that a neighbor cell is infected in 
                # each time step 
mean = 4
sd = 1                                                 

class Cell(object):

    def __init__(self,x, y):
        self.x = x
        self.y = y 
        self.state = "S" # can be "S" (susceptible), "R" (resistant = dead), or 
                         # "I" (infected)
        self.time = 0
    
    def __str__(self):
        return str(self.x) + ', ' + str(self.y)
    
    def infect(self):
        self.state = 'I'
        self.time = 0
    
    def process(self, adjacentcells):
        if self.state == 'I':
            rdm = random.random()
            if rdm > pdeath(self.time, mean, sd) and self.time >= recovery_time:
                self.state = 'S'
                self.time = 0
            elif rdm <= pdeath(self.time, mean, sd):
                self.state = 'R'
            else:
                for cell in adjacentcells:
                    if cell.state == 'S':
                        if rdm <= virality:
                            cell.infect()
                self.time +=1
        else:
            self.time +=1
            return self.time
                    
        
        
        
class Map(object):
    
    cells = dict()
    
    def __init__(self):
        self.height = 150
        self.width = 150           
        self.cells = {}

    def add_cell(self, cell):
        self.cell = cell
        key = (cell.x, cell.y)
        self.cells[key] = self.cell
        
    def display(self):
        red, green, blue = range(3)
        img = np.zeros((150, 150, 3))
        for x,y in self.cells:
            cell = self.cells[x,y]
            if cell.state == 'S':
                img[x,y,:] = (0.0, 1.0, 0.0) #green
            elif cell.state == 'I':
                img[x,y,:] = (1.0,0.0,0.0) #red
            elif cell.state == 'R':
                img[x,y,:] = (0.5,0.5,0.5) #grey
            else:
                img[x,y,:] = (0.0,0.0,0.0) #black
        plt.imshow(img)
    
    def adjacent_cells(self, x,y):
        adj = []
        
        n = (x, y+1)
        e = (x+1, y)
        s = (x, y-1)
        w = (x-1, y)
        
        tuple_adj = (n, e, s, w)
        for i in tuple_adj:
            if i in self.cells:
                adj.append(self.cells[i])
        return adj
    
    def time_step(self):
        # Update each cell on the map 
        # display the map.
        
        # ... cell.process(adjacent_cells... )
        for celltuple in self.cells:
            cell = self.cells[celltuple]
            cell.process(self.adjacent_cells(cell.x, cell.y))
        self.display()

            
def read_map(filename):
    
    m = Map()
    
    f = open(filename,'r')
    
    for line in f:
        coordinates = line.strip().split(',')
        c = Cell(int(coordinates[0]),int(coordinates[1]))
        Map.add_cell(m, c)

    return m

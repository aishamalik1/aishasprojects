#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 14:39:29 2019

@author: aishamalik

"""
orders = []
def select_meal():
    meal = input("Hello, would you like a pizza or salad? ")
    order = meal.lower()
    if order == "pizza":
        pizza()
    elif order == 'salad':
        salad()
    else:
        print("Your order has been placed! Goodbye.")

def pizza():
    siz = input("Small, medium or large? ")
    size = siz.lower()
    
    def toppings():
        top = input ("Add a topping: pepperoni, mushrooms, spinach, jalapenos or say 'done'.  ")
        topping = []
        while top != "done":
            topping.append(top)
            top = input ("Add a topping: pepperoni, mushrooms, spinach, jalapenos or say 'done'.  ")
        if topping == []:
            final = "one " + size + " pizza"
            orders.append(final)
            eat = " and ".join(orders)
            print("You ordered", "{}.".format(eat), "Place another order or say 'done' ")
        else:
            alltop = "with " + ' and '.join(topping) 
            final = "one " + size + " pizza "+ alltop
            orders.append(final)
            eat = " and ".join(orders)
            print("You ordered","{}.".format(eat), "Place another order or say 'done' ")
        select_meal()
    toppings()
           
def salad():
    salad = input("Would you like a garden salad or a greek salad? ")

    def dressing():
        dress = input("Please choose a dressing: vinaigrette, ranch, lemon or italian? ")
        salad_order = "one " + salad + " salad with " + dress + " dressing"
        orders.append(salad_order)
        eat = " and ".join(orders)
        print("You ordered", "{}.".format(eat), "Place another order or say 'done' ")
        select_meal()
    dressing()
#gotta make a nesting doll type whole function, write this on paper before writing the code.
select_meal()
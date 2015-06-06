#!/usr/bin/python

groceries = ["banana", "apple", "orange"]

stock = {"banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
    }
    
prices = {"banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
    }

def computeBill(groceries):
    total = 0
    for food in groceries:
        if stock[food] > 0:
            total += prices[food]
            stock[food] -= 1
            print stock[food]
        else:
            total = total
            continue
#            prices[food] = 0 these 2 lines work as well
#            total += prices[food]
    return total

print computeBill(groceries)
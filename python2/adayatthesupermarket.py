#!/usr/bin/python
"""#!/opt/local/bin/python3.3"""

groceries = ["banana", "orange", "apple"]

print groceries

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
    
#for food in groceries:
#	computeBill(food)

def computeBill(groceries):
	total = 0
	for food in groceries:
		total += (stock[food] * prices[food])
#		return total
	return total

print computeBill(groceries)

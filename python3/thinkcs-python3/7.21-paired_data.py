'''
paired data
'''

celebs = [("Brad Pitt", 1963), ("Jack Nicholson", 1937),
                                ("Justin Bieber", 1994)]

for (i, j) in celebs:
    if j < 1980:
        print(i)
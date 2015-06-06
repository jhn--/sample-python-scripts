'''
Add a print function to Newton’s sqrt function that prints out better each time it is calculated. Call your modified function with 25 as an argument and record the results.
'''

def newtonsqrt(n):
    approx = n/2.0            #lets just start somewhere
    while True:
        better = (approx + (n/approx))/2.0
        if abs(approx - better) < 0.001:
            return better
        print(better)
        approx = better

print(newtonsqrt(25.0))
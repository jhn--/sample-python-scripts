'''
11.16.Functions_that_produce_lists
'''

def is_prime(n):
    '''
    using trial division
    '''
    if n <= 3:                                  #(negative to 3)
        if n <= 1:                              #(negative to 1)
            return False
        return True                             #removed all negative numbers, 0 and 1. 2 and 3 remains and are prime numbers
    else:
        for i in range(2, n-1):
            if n % i == 0:
                return False
        return True

def primes_lessthan(n):
    result = []
    for i in range(2, n):
        if is_prime(i):
            result.append(i)
    return result

print(primes_lessthan(100))
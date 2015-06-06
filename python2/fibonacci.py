#!/opt/local/bin/python2.6

a = '123456789'

n=10

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

#print('%n.' % n '%n.' % fib(n))

print n 
print fib(n)
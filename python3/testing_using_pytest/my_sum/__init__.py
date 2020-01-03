#!/usr/bin/env python3

from sys import argv

def my_sum(args):
    # print(args)
    total = 0
    for i in args:
        try:
            total += float(i)
        except:
            raise Exception('Only numbers please!')
            # raise ValueError('Only numbers please!') # ValueError works as well.
    return total

if __name__ == '__main__':
    my_sum(argv[1:])
'''
11.22.5
'''

import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno     # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

'''
def add_vectors(u, v):
    """approach one"""
    answer = []
    for (i, val) in enumerate(u):
        answer.append(val + v[i])
    return answer
'''

def add_vectors(u, v):
    """approach two"""
    answer = []
    for i in zip(u, v):
        total = 0
        for (x, val) in enumerate(i):
            total += val
        answer.append(total)
    return answer

def scalar_mult(s, v):
    answer = []
    for i in v:
        answer.append(s*i)
    return answer

def dot_product(u, v):
    answer = 0
    for i in zip(u, v):
        xyz = 1
        for x in i:         #for each element (named x) in i
            xyz *= x        #multiply xyz to each of them 
        answer += xyz       #then add answer to each result of the multiplication
        print(xyz)
    print(answer)
    return answer

def cross_product(u, v):
    uxb = []
    uxb.append((u[1]*v[2])-(u[2]*v[1]))
    uxb.append((u[2]*v[0])-(u[0]*v[2]))
    uxb.append((u[0]*v[1])-(u[1]*v[0]))
    '''
    if len(uxb) == 0:
        uxb.append((u[1]*v[2])-(u[2]*v[1]))
    elif len(uxb) == 1:
        uxb.append((u[2]*v[0])-(u[0]*v[2]))
    else:
        uxb.append((u[0]*v[1])-(u[1]*v[0]))
    '''
    print(uxb)
    return uxb

'''
test(add_vectors([1, 1], [1, 1]) == [2, 2])
test(add_vectors([1, 2], [1, 4]) == [2, 6])
test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])

test(scalar_mult(5, [1, 2]) == [5, 10])
test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])

test(dot_product([1, 1], [1, 1]) ==  2)
test(dot_product([1, 2], [1, 4]) ==  9)
test(dot_product([1, 2, 1], [1, 4, 3]) == 12)
'''

test(cross_product([2,3,4],[5,6,7]) == [-3,6,-3])


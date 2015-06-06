'''
Write a function print_triangular_numbers(n) that prints out the first n triangular numbers. A call to print_triangular_numbers(5) would produce the following output:

1       1
2       3
3       6
4       10
5       15
(hint: use a web search to find out what a triangular number is.)
'''

def print_triangular_numbers(n):
    '''
    (n * (n + 1)) / 2
    '''
    for i in range(1, n+1):
        tri_num = int((i * (i + 1)) / 2)
        print(i, "\t", tri_num)

print_triangular_numbers(20)
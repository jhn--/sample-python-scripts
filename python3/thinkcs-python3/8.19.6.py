'''
8.19.6
Print a neat looking multiplication table like this:

        1   2   3   4   5   6   7   8   9  10  11  12
  :--------------------------------------------------
 1:     1   2   3   4   5   6   7   8   9  10  11  12
 2:     2   4   6   8  10  12  14  16  18  20  22  24
 3:     3   6   9  12  15  18  21  24  27  30  33  36
 4:     4   8  12  16  20  24  28  32  36  40  44  48
 5:     5  10  15  20  25  30  35  40  45  50  55  60
 6:     6  12  18  24  30  36  42  48  54  60  66  72
 7:     7  14  21  28  35  42  49  56  63  70  77  84
 8:     8  16  24  32  40  48  56  64  72  80  88  96
 9:     9  18  27  36  45  54  63  72  81  90  99 108
10:    10  20  30  40  50  60  70  80  90 100 110 120
11:    11  22  33  44  55  66  77  88  99 110 121 132
12:    12  24  36  48  60  72  84  96 108 120 132 144
'''

def mutiplication_table():
    layout = "{0:>3}:   {1:>3} {2:>3} {3:>3} {4:>3} {5:>3} {6:>3} {7:>3} {8:>3} {9:>4} {10:>4} {11:>4} {12:>4}"

    print("{0:>3}    {1:>3} {2:>3} {3:>3} {4:>3} {5:>3} {6:>3} {7:>3} {8:>3} {9:>4} {10:>4} {11:>4} {12:>4}".format("", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    print("   :"+("-"*54)) #might have a better way of doing this....
    for i in range(1,13):
        print(layout.format(i, i*1, i*2, i*3, i*4, i*5, i*6, i*7, i*8, i*9, i*10, i*11, i*12))

mutiplication_table()
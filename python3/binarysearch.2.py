class search:

    def __init__(self, array = [], searchitem = ""):
        self.array = array
        self.searchitem = searchitem
        #self.lower_index = 0
        #self.upper_index = len(self.array)
        #self.mid_index = len(self.array) // 2 #lower limit, eg 11//2 = 5, not 5.6

    def binarysearch(self):
        self.lower_index = 0
        self.upper_index = len(self.array)

        while True:
            if self.lower_index == self.upper_index:
                return "Not found."

            self.mid_index = (self.lower_index + self.upper_index) // 2

            if self.array[self.mid_index] == self.searchitem:
                return "Search item: {0}, is found.".format(self.searchitem)

            if self.array[self.mid_index] < self.searchitem:
                self.lower_index = self.mid_index + 1
            else:
                self.upper_index = self.mid_index


    def __str__(self):
        pass



a = [1,2,3,4,5,6,7,8,9,10]
b = 9
c = 5
d = 4
e = 20

s = search(a, b)
print(s.binarysearch())

t = search(a, c)
print(t.binarysearch())

u = search(a, d)
print(u.binarysearch())

v = search(a, e)
print(v.binarysearch())
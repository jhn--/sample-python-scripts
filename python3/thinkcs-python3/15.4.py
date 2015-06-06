#15.4

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def halfway(self, target):
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

def midpoint(p1, p2):
    mx = (p1.x + p2.x)/2
    my = (p1.y + p2.y)/2
    return Point(mx, my)

p = Point(4, 2)
q = Point(6, 3)
r = Point()
print(p.x, q.y, r.x)

print(str(p))
#str(q)
print(q)
#str(r)
print(r)

print("returns midpoint")
p = Point(3,4)
q = Point(5,12)
r = midpoint(p, q)
#str(r)
print(r)

print("returns halfway")
print(Point(3,4).halfway(Point(2,12)))
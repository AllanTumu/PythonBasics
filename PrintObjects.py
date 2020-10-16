# String representation of class objects
# Object Printing

class Test:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "a:%s b:%s" % (self.x, self.y)

    def __str__(self):
        return "value of a is %s and b is %s" % (self.x, self.y)


# Test code
t = Test(10, 20)
print(t)
